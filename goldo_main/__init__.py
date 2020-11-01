import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio
import math

import runpy

class MatchState:
    Idle = 0
    PreMatch = 1
    WaitForStartOfMatch = 2
    Match = 3
    MatchFinished = 4
    
class SensorsState:
    def __init__(self, robot):
        self._robot = robot
        for k,v in self._robot._config_proto.sensor_ids.items():
            setattr(self, k, False)
        
    def _update(self, msg):
        state = msg.gpio | (msg.fpga << 32 )
        for k,v in self._robot._config_proto.sensor_ids.items():
            setattr(self, k, bool(state & (1 << v)))
    
class RobotCommands:
    def __init__(self, robot):
        self._robot = robot
        self._propulsion_seq = 1
        
    def _publish(self, topic, msg=None):
        return self._robot._broker.publishTopic(topic, msg)
        
    def scoreSet(self, score):
        return self._publish('gui/in/score', _sym_db.GetSymbol('google.protobuf.Int32Value')(value=score))
        
    def lidarStart(self):
        return self._publish('rplidar/in/start')
        
    def lidarStop(self):
        return self._publish('rplidar/in/stop')
        
    def propulsionSetEnable(self, enable):
        return self._publish('nucleo/in/propulsion/enable/set', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=enable))
        
    def motorsSetEnable(self, enable):
        return self._publish('nucleo/in/propulsion/motors/enable/set', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=enable))
        
    def propulsionSetAccelerationLimits(self, accel, deccel, angular_accel, angular_deccel):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.AccelerationLimits')()
        msg.accel = accel
        msg.deccel = deccel
        msg.angular_accel = angular_accel
        msg.angular_deccel = angular_deccel
        return self._publish('nucleo/in/propulsion/motors/acceleration_limits/set', msg)
        
    async def propulsionTranslation(self, distance, speed):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteTranslation')(
            distance = distance,
            speed = speed)
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/translation', msg)
        #await fut
        
    async def propulsionMoveTo(self, pt, speed):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteMoveTo')()
        msg.speed = speed
        msg.point.x = pt[0]
        msg.point.y = pt[1]
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/move_to', msg)
        #await fut
        
    async def propulsionRotation(self, angle, yaw_rate):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteRotation')(
                yaw_delta = angle * math.pi/180,
                yaw_rate = yaw_rate)
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/rotation', msg)
        #await fut
        
    async def propulsionPointTo(self, pt, yaw_rate):
        seq = self._propulsion_seq
        self._propulsion_seq += 1
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecutePointTo')()
        msg.yaw_rate = yaw_rate
        msg.point.x = pt[0]
        msg.point.y = pt[1]
        msg.sequence_number = seq
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/point_to', msg)
        #await fut
        
    async def propulsionFaceDirection(self, yaw, yaw_rate):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteFaceDirection')()
        msg.yaw_rate = yaw_rate
        msg.yaw = yaw * math.pi/180
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/face_direction', msg)
        #await fut
        
    async def propulsionTrajectory(self, points, speed):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteTrajectory')()
        msg.speed = speed
        Point = _sym_db.GetSymbol('goldo.common.geometry.Point')
        msg.points.extend([Point(x=pt[0], y=pt[1])for pt in points])
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/trajectory', msg)
        #await fut
        
    async def propulsionSetPose(self, pt, yaw):
        msg = _sym_db.GetSymbol('goldo.common.geometry.Pose')()
        msg.yaw = yaw * math.pi/180
        msg.position.x = pt[0]
        msg.position.y = pt[1]
        await self._publish('nucleo/in/propulsion/pose/set', msg)
        
    def propulsionWaitForStop(self):
        fut = asyncio.Future()
        self._robot._futures_propulsion_wait_stopped.append(fut)
        return fut
        
    def waitForMatchTimer(self, t):
        fut = asyncio.Future()
        self._robot._futures_match_timer.append((t, fut))
        return fut
        
         
    async def servoMove(self, name, position, speed=100):
        servo_id = self._robot._config_proto.servo_ids[name]
        print(self._robot._config_proto.servo_ids)
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.Move')(servo_id=servo_id, position=position, speed=speed)
        await self._robot._broker.publishTopic('nucleo/in/servo/move', msg)
        
        
class RobotMain:
    def sequence(self, func):
        self._sequences[func.__name__] = func
        
    def snapGirouette(self):
        self.girouette = self._last_girouette
        
    def loadConfig(self, config_path):
        self._sequences = {}
        config = _pb2.get_symbol('goldo.nucleo.robot.Config')()
        config.ParseFromString(open(config_path + 'robot_config.bin', 'rb').read())
        self._config_proto = config
        self.sensors = SensorsState(self)
        runpy.run_path(config_path + 'sequences.py', {'robot': self, 'commands': self.commands, 'sensors': self.sensors})
             
    def _startPropulsionCmd(self):
        fut = asyncio.Future()
        self._futures_propulsion_ack.append(fut)
        return fut
        
    def __init__(self):
        config_path = f'config/test/'
        self._tasks = []
        self._simulation_mode = False
        self.side = 0        
        self._adversary_detection_enable = True
        self.commands = RobotCommands(self)
        self._sequences = {}
        self._match_state = MatchState.Idle
        self._current_task = None
        self._last_girouette = None
        self.girouette = None
        self._futures_propulsion_ack = []
        self._futures_propulsion_wait_stopped = []
        self._futures_match_timer = []
        self.loadConfig(config_path)
        
    async def configNucleo(self, msg):
        buff = self._config_proto.data
        await self._broker.publishTopic('nucleo/in/robot/config/load_begin', _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadBegin')(size=len(buff)))
        #Upload codes by packets        
        while len(buff) > 0:
            await self._broker.publishTopic('nucleo/in/robot/config/load_chunk', _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadChunk')(data=buff[0:32]))
            buff = buff[32:]
        #Finish programming
        await self._broker.publishTopic('nucleo/in/robot/config/load_end', _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadEnd')(crc=self._config_proto.crc)) 

        msg = _sym_db.GetSymbol('google.protobuf.FloatValue')(value = self._config_proto.rplidar_config.theta_offset * math.pi / 180)
        await self._broker.publishTopic('rplidar/in/config/theta_offset', msg)
        
        await self._broker.publishTopic('rplidar/in/config/distance_tresholds', self._config_proto.rplidar_config.tresholds)
        await self._broker.publishTopic('nucleo/in/propulsion/odrive/clear_errors')
        await self._broker.publishTopic('nucleo/in/propulsion/simulation/enable', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=self._simulation_mode) )
        for t in self._tasks:
            t.cancel()
        self._tasks = []
        
  
    async def onConfigStatus(self, msg):
        await self._broker.publishTopic('gui/in/nucleo_config_status', msg)
        
    async def onNucleoReset(self, msg):
        await self._broker.publishTopic('gui/in/nucleo_reset', msg)         
        
    async def onPreMatch(self, msg):
        config_path = f'config/test/'
        self.loadConfig(config_path)
        print("prematch started, side = {}".format({0: 'unset', 1: 'blue', 2:'yellow'}[self.side]))
        
        self._match_state = MatchState.PreMatch
        await self._broker.publishTopic('gui/in/match_state', _sym_db.GetSymbol('google.protobuf.Int32Value')(value=self._match_state))
        self._tasks.append(asyncio.create_task(self._prematchSequence()))
        
    async def _prematchSequence(self):
        await self._sequences['prematch']()
        self._match_state = MatchState.WaitForStartOfMatch
        await self._broker.publishTopic('gui/in/match_state', _sym_db.GetSymbol('google.protobuf.Int32Value')(value=self._match_state))
        print('prematch finished')
        
    async def _matchSequence(self):
        await self._sequences['match']()
        self._match_state = MatchState.MatchFinished
        await self._broker.publishTopic('gui/in/match_state', _sym_db.GetSymbol('google.protobuf.Int32Value')(value=self._match_state))
        print('match finished')

        
    async def onCameraDetections(self, msg):
        for d in msg.detections:
            if d.tag_id == 17:
                # south up
                if d.uy > 0:
                    self._last_girouette = 's'
                else:
                    self._last_girouette = 'n'
        
    async def onPropulsionTelemetry(self, msg):
        self.propulsion_telemetry = msg       
            
        if msg.state == 1:
            for f in self._futures_propulsion_wait_stopped:
                f.set_result(None)
            self._futures_propulsion_wait_stopped = []                    
        
    async def onPropulsionAck(self, msg):
        for f in self._futures_propulsion_ack:
            try:
                f.set_result(None)
            except:
                pass
        self._futures_propulsion_ack = []
        
    async def onSensorsState(self, msg):
        self.sensors._update(msg)
        await self._broker.publishTopic('gui/in/sensors/start_match', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=self.sensors.start_match)) 
        await self._broker.publishTopic('gui/in/sensors/emergency_stop', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=self.sensors.emergency_stop))
        if self.sensors.emergency_stop:
            await self.commands.lidarStop()
            await self.commands.motorsSetEnable(False)
            
        if self._match_state == MatchState.WaitForStartOfMatch and self.sensors.start_match:
            await self.startMatch()            
            
    async def startMatch(self):
        self._match_state = MatchState.Match
        await self._broker.publishTopic('nucleo/in/match/timer/start')
        self.match_timer = 100
        await self._broker.publishTopic('gui/in/match_state', _sym_db.GetSymbol('google.protobuf.Int32Value')(value=self._match_state)) 
        print('match started')
        self._tasks.append(asyncio.create_task(self._matchSequence()))
            
    async def onMatchTimer(self, msg):
        self.match_timer = msg.value
        futs = []
        for t, f in self._futures_match_timer:
            if msg.value > 0 and msg.value < t:
                try:
                    f.set_result(None)
                except:
                    pass
            else:
                futs.append((t, f))
        self._futures_match_timer = futs
            
        
    async def onRPLidarDetections(self, msg):
        if self._match_state == MatchState.Match and not self._simulation_mode:
            if msg.front_near or msg.left_near or msg.right_near or msg.front_far:
                await self.commands.motorsSetEnable(False)
        
    async def onODriveTelemetry(self, msg):
        if msg.axis0_error or msg.axis1_error or msg.axis0_motor_error or msg.axis1_motor_error:
            await self._broker.publishTopic('gui/in/odrive_error', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=True))
        else:
            await self._broker.publishTopic('gui/in/odrive_error', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=False))
            
        
        await self._broker.publishTopic('gui/in/odrive_state', _sym_db.GetSymbol('google.protobuf.StringValue')(value='{}{}'.format(msg.axis0_current_state, msg.axis1_current_state)))
        
    def _setBroker(self, broker):
        self._broker = broker
        broker.registerCallback('gui/out/side', self.onSetSide)
        broker.registerCallback('gui/out/commands/config_nucleo', self.configNucleo)
        broker.registerCallback('gui/out/commands/prematch', self.onPreMatch)
        broker.registerCallback('nucleo/out/robot/config/load_status', self.onConfigStatus)
        broker.registerCallback('nucleo/out/os/reset', self.onNucleoReset)
        broker.registerCallback('nucleo/out/propulsion/telemetry', self.onPropulsionTelemetry)
        broker.registerCallback('nucleo/out/propulsion/cmd_ack', self.onPropulsionAck)
        broker.registerCallback('camera/out/detections', self.onCameraDetections)
        broker.registerCallback('nucleo/out/sensors/state', self.onSensorsState)
        broker.registerCallback('nucleo/out/match/timer', self.onMatchTimer)
        broker.registerCallback('nucleo/out/odrive/telemetry', self.onODriveTelemetry)
        
        broker.registerCallback('rplidar/out/detections', self.onRPLidarDetections)
        
    async def onSetSide(self, msg):
        self.side = msg.value
        
robot = RobotMain()
import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio
import struct
import math

import runpy

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

    #temporary
    async def _dynamixelsWriteReg(self, id_, reg, payload):
        msg = _sym_db.GetSymbol('goldo.nucleo.dynamixels.RequestPacket')(
                sequence_number=0,
                protocol_version=1,
                id=id_,
                command=0x03,
                payload=struct.pack('B', reg) + payload
                )
        await self._publish('nucleo/in/dynamixels/request', msg)
    
    async def dynamixelsSetTorqueEnable(self, id_, enable):
        await self._dynamixelsWriteReg(id_, 24, struct.pack('<?', enable))
        
    async def dynamixelsSetPosition(self, id_, position):
        await self._dynamixelsWriteReg(id_, 30, struct.pack('<H', position))
        
    async def dynamixelsSetSpeed(self, id_, speed):
        await self._dynamixelsWriteReg(id_, 32, struct.pack('<H', speed))
        
    async def dynamixelsSetTorqueLimit(self, id_, torque):
        await self._dynamixelsWriteReg(id_, 34, struct.pack('<H', torque))
        
    
    async def servoMove(self, name, position, speed=100):
        servo_id = self._robot._config_proto.servo_ids[name]
        print(self._robot._config_proto.servo_ids)
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.Move')(servo_id=servo_id, position=position, speed=speed)
        await self._robot._broker.publishTopic('nucleo/in/servo/move', msg)


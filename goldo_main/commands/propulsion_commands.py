import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio
import functools
import math
import logging

from typing import Mapping


LOGGER = logging.getLogger(__name__)

class PropulsionCommand(object):
    def __init__(self, loop, sequence_number):
        self._sequence_number = sequence_number
        self._status = -1
        self._loop = loop
        self._future_begin = None
        self._future_end = None    
        
    @property
    def begin(self):
        if self._future_begin is None:
            self._future_begin = self._loop.create_future()   
            self._update_status()
        return self._future_begin
        
    @property
    def end(self):
        if self._future_end is None:
            self._future_end = self._loop.create_future()
            self._update_status()
        return self._future_end
        
    def _update_status(self, status = None):
        if status is not None:
            self._status = status
        if self._status == 0 and self._future_begin and not self._future_begin.done():
            self._future_begin.set_result(None)
        if self._status == 1 and self._future_end and not self._future_end.done():
            self._future_end.set_result(None)
            
        

class PropulsionCommands:
    _sequence_number: int
    _futures: Mapping[int, asyncio.Future]

    _broker: object
    _loop: object

    def __init__(self):
        self._sequence_number = 1
        self._loop = asyncio.get_event_loop()
        self._futures = {}
        self._commands = {}

    def setBroker(self, broker):
        self._broker = broker
        self._broker.registerCallback('nucleo/out/propulsion/cmd_event', self._on_cmd_event)

    def _create_future(self):
        #future = self._loop.create_future()
        sequence_number = self._sequence_number
        self._sequence_number = (self._sequence_number + 1) % (1 << 15)
        LOGGER.debug("PropulsionCommands: create future, sequence_number=%s", sequence_number)
        
        #self._futures[sequence_number] = (future, None)
        #future.add_done_callback(functools.partial(self._remove_future, sequence_number))
        #return sequence_number, future
        cmd = PropulsionCommand(self._loop, sequence_number)
        self._commands[sequence_number] = cmd
        return sequence_number, cmd

    def _remove_future(self, sequence_number: int, future: asyncio.Future):
        LOGGER.debug("Remove done future %r", sequence_number)
        self._futures.pop(sequence_number, None)

    def _publish(self, topic, msg=None):
        return self._broker.publishTopic(topic, msg)

    def setEnable(self, enable):
        return self._publish('nucleo/in/propulsion/enable/set', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=enable))

    def setMotorsEnable(self, enable):
        return self._publish('nucleo/in/propulsion/motors/enable/set', _sym_db.GetSymbol('google.protobuf.BoolValue')(value=enable))

    def setAccelerationLimits(self, accel, deccel, angular_accel, angular_deccel):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.AccelerationLimits')()
        msg.accel = accel
        msg.deccel = deccel
        msg.angular_accel = angular_accel
        msg.angular_deccel = angular_deccel
        return self._publish('nucleo/in/propulsion/motors/acceleration_limits/set', msg)
        
    def clearCommandQueue(self):
        return self._publish('nucleo/in/propulsion/clear_command_queue')
        
    async def setPose(self, pt, yaw):
        msg = _sym_db.GetSymbol('goldo.common.geometry.Pose')()
        msg.yaw = yaw * math.pi/180
        msg.position.x = pt[0]
        msg.position.y = pt[1]
        await self._publish('nucleo/in/propulsion/pose/set', msg)

    async def translation(self, distance, speed):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteTranslation')(
            distance = distance,
            speed = speed)
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/translation', msg)
        #await fut

    async  def moveTo(self, pt, speed):
        sequence_number, future = self._create_future()
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteMoveTo')()
        msg.sequence_number = sequence_number
        msg.speed = speed
        msg.point.x = pt[0]
        msg.point.y = pt[1]

        await self._publish('nucleo/in/propulsion/cmd/move_to', msg)
        return future

    async def rotation(self, angle, yaw_rate):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteRotation')(
                yaw_delta = angle * math.pi/180,
                yaw_rate = yaw_rate)
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/rotation', msg)
        #await fut

    async def pointTo(self, pt, yaw_rate):
        sequence_number, future = self._create_future()
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecutePointTo')()
        msg.yaw_rate = yaw_rate
        msg.point.x = pt[0]
        msg.point.y = pt[1]
        msg.sequence_number = sequence_number
        await self._publish('nucleo/in/propulsion/cmd/point_to', msg)
        return future

    async def faceDirection(self, yaw, yaw_rate):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteFaceDirection')()
        msg.yaw_rate = yaw_rate
        msg.yaw = yaw * math.pi/180
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/face_direction', msg)
        #await fut

    async def trajectory(self, points, speed):
        msg = _sym_db.GetSymbol('goldo.nucleo.propulsion.ExecuteTrajectory')()
        msg.speed = speed
        Point = _sym_db.GetSymbol('goldo.common.geometry.Point')
        msg.points.extend([Point(x=pt[0], y=pt[1])for pt in points])
        #fut = self._robot._startPropulsionCmd()
        await self._publish('nucleo/in/propulsion/cmd/trajectory', msg)
        #await fut

    async def setPose(self, pt, yaw):
        msg = _sym_db.GetSymbol('goldo.common.geometry.Pose')()
        msg.yaw = yaw * math.pi/180
        msg.position.x = pt[0]
        msg.position.y = pt[1]
        await self._publish('nucleo/in/propulsion/pose/set', msg)

    async def _on_cmd_event(self, msg):
        cmd = self._commands.get(msg.sequence_number)
        print(msg)
        if cmd is not None:
            cmd._update_status(msg.status)
            if msg.status > 0:
                del self._commands[msg.sequence_number]

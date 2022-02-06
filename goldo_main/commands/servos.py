import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio
import struct
import math
import functools

import runpy

class ServosCommands:
    def __init__(self, robot):
        self._robot = robot
        self._servos_ids = {}
        self._servos_names = []
        self._states_proto = self._robot._state_proto.servos
        self._loop = asyncio.get_event_loop()
        self._futures = {}
        self._futures_moving = {}
        self._futures_by_seq = {}
        self._sequence_number = 0

        self._robot._broker.registerCallback('nucleo/out/servo/ack', self._onMsgAck)
        self._robot._broker.registerCallback('nucleo/out/servo/status/moving', self._onMsgMoving)
        self._robot._broker.registerCallback('nucleo/out/servo/status/states', self._onServoStates)


    def loadConfig(self):
        self._servos_ids = {}
        self._servos_names = []
        servos_proto = self._robot._config_proto.nucleo.servos
        for i, servo_proto in enumerate(servos_proto):
            self._servos_ids[servo_proto.name] = i
            self._servos_names.append(servo_proto.name)

    async def disableAll(self):
        msg, future = self._create_command_msg('CmdDisableAll')
        await self._robot._broker.publishTopic('nucleo/in/servo/disable_all', msg)
        await future

    async def setEnable(self, name_or_servos, enable):
        if isinstance(name_or_servos, (str, bytes)):
            name_or_servos = [name_or_servos]
        ServoEnable = _sym_db.GetSymbol('goldo.nucleo.servos.ServoEnable')
        enables = [ServoEnable(servo_id=self._servos_ids[name], enable=enable) for name in name_or_servos]
        msg, future = self._create_command_msg('CmdSetEnable', enables=enables)
        await self._robot._broker.publishTopic('nucleo/in/servo/enable/set', msg)
        await future
        
    async def setMaxTorque(self, name_or_servos, torque):
        if isinstance(name_or_servos, (str, bytes)):
            name_or_servos = [name_or_servos]
        ServoTorque = _sym_db.GetSymbol('goldo.nucleo.servos.ServoTorque')
        torques = [ServoTorque(servo_id=self._servos_ids[name], torque=math.floor(torque * 255)) for name in name_or_servos]
        msg, future = self._create_command_msg('CmdSetMaxTorques', torques=torques)
        await self._robot._broker.publishTopic('nucleo/in/servo/set_max_torques', msg)
        await future

    async def move(self, name, position, speed=100):
        await self.moveMultiple({name: position}, speed * 0.01)

    async def moveMultiple(self, servos, speed = 1):
        speed = int(speed * 0x3ff)
        elts = []
        servos_mask = 0
        seq = self._get_sequence_number()

        for k, v in servos.items():
            id_ = self._servos_ids[k]
            elts.append(_sym_db.GetSymbol('goldo.nucleo.servos.ServoPosition')(servo_id=id_, position=v))
            servos_mask |= (1 << id_)
        msg, future = self._create_command_msg('CmdMoveMultiple', speed=speed, positions=elts)        

        await self._robot._broker.publishTopic('nucleo/in/servo/move_multiple', msg)
        await future
        # after the move is started, wait for the servos to stop moving        
        future = self._loop.create_future()
        self._futures_moving[id(future)] = [future, servos_mask]        
        future.add_done_callback(self._remove_future_moving)

    async def liftDoHoming(self, id_):
        seq = self._get_sequence_number()
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.CmdLiftDoHoming')(sequence_number=seq, lift_id=id_)
        await self._robot._broker.publishTopic('nucleo/in/lift/do_homing', msg)

    async def liftSetEnable(self, id_, enable):
        seq = self._get_sequence_number()
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.CmdLiftSetEnable')(sequence_number=seq, lift_id=id_, enable=enable)
        await self._robot._broker.publishTopic('nucleo/in/lift/set_enable', msg)

    async def _onMsgAck(self, msg):
        future = self._futures_by_seq.pop(msg.value, None)
        if future is not None:
            future.set_result(None)

    async def _onMsgMoving(self, msg):
        for e in self._futures_moving.values():
            if not(msg.value & e[1]):
                e[0].set_result(None)
                
    async def _onServoStates(self, msg):
        for i, s in enumerate(msg.servos):
            self._states_proto[self._servos_names[i]].CopyFrom(s)

    def _get_sequence_number(self):
        seq = self._sequence_number
        self._sequence_number = (self._sequence_number + 1) % 0x0fff
        return seq

    def _remove_future(self, id_, future):
        self._futures.pop(id_, None)
        
    def _remove_future_moving(self, future):
        self._futures_moving.pop(id(future), None)

    def _create_future(self):
        future = self._loop.create_future()
        sequence_number = self._get_sequence_number()
        future.add_done_callback(functools.partial(self._remove_future, sequence_number))
        self._futures[sequence_number] = future
        return sequence_number, future

    def _create_command_msg(self, name, **kwargs):
        sequence_number, future = self._create_future()
        self._futures_by_seq[sequence_number] = future
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.' + name)(**kwargs)
        msg.sequence_number = sequence_number
        return msg, future

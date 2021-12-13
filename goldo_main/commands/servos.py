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
        self._loop = asyncio.get_event_loop()
        self._futures = {}
        self._futures_by_seq = {}
        self._sequence_number = 0
        
        self._robot._broker.registerCallback('nucleo/out/servo/move_multiple', self._onMsgAck)
        self._robot._broker.registerCallback('nucleo/out/servo/status/moving', self._onMsgMoving)
    
        
    def loadConfig(self):
        self._servos_ids = {}
        servos_proto = self._robot._config_proto.nucleo.servos
        for i, servo_proto in enumerate(servos_proto):
            self._servos_ids[servo_proto.name] = i
            
    async def setEnable(self, name, enable):
        servo_id = self._servos_ids[name]
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.SetEnable')(servo_id=servo_id, enable=enable)
        await self._robot._broker.publishTopic('nucleo/in/servo/enable/set', msg)
        
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
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.CmdMoveMultiple')(sequence_number=seq, speed=speed, positions=elts)

        future = self._loop.create_future()
        self._futures[id(future)] = [future, False, seq, servos_mask]
        
        future.add_done_callback(functools.partial(self._remove_future, id(future)))

        await self._robot._broker.publishTopic('nucleo/in/servo/move_multiple', msg)
        await future
        
    async def liftDoHoming(self, id_):        
        seq = self._get_sequence_number()
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.CmdLiftDoHoming')(sequence_number=seq, lift_id=id_)
        await self._robot._broker.publishTopic('nucleo/in/lift/do_homing', msg)
        
    async def liftSetEnable(self, id_, enable):
        seq = self._get_sequence_number()
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.CmdLiftSetEnable')(sequence_number=seq, lift_id=id_, enable=enable)
        await self._robot._broker.publishTopic('nucleo/in/lift/set_enable', msg)
        
    async def _onMsgAck(self, msg):
        for e in self._futures.values():
            if e[2] == msg.value:
                e[1] = True
                print('servo ack')
        
    async def _onMsgMoving(self, msg):
        for e in self._futures.values():
            if e[1] and not(msg.value & e[3]):
                e[0].set_result(None)
        
    def _get_sequence_number(self):
        seq = self._sequence_number
        self._sequence_number = (self._sequence_number + 1) % 0x0fff
        print(seq)
        return seq
    #def _publish
    def _remove_future(self, id_, future):
        self._futures.pop(id_, None)
        
    def _create_future(self):
        future = self._loop.create_future()
        self._sequence_number = (self._sequence_number + 1) % (1 << 15)
        LOGGER.debug("PropulsionCommands: create future, sequence_number=%s", sequence_number)
        
        self._futures[sequence_number] = future
        future.add_done_callback(functools.partial(self._remove_future, sequence_number))
        return sequence_number, future
        cmd = PropulsionCommand(self._loop, sequence_number)
        self._commands[sequence_number] = cmd
        return sequence_number, cmd


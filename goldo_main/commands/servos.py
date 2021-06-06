import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio
import struct
import math

import runpy

class ServosCommands:
    def __init__(self, robot):
        self._robot = robot
        self._servos_ids = {}
        
    def loadConfig(self):
        self._servos_ids = {}
        servos_proto = self._robot._config_proto.nucleo.servos
        for i, servo_proto in enumerate(servos_proto):
            self._servos_ids[servo_proto.name] = i

    async def move(self, name, position, speed=100):
        servo_id = self._servos_ids[name]
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.Move')(servo_id=servo_id, position=position, speed=speed)
        await self._robot._broker.publishTopic('nucleo/in/servo/move', msg)


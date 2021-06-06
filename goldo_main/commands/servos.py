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

    def _publish(self, topic, msg=None):
        return self._robot._broker.publishTopic(topic, msg)        
    
    async def move(self, name, position, speed=100):
        servo_id = self._robot._config_proto.servo_ids[name]
        msg = _sym_db.GetSymbol('goldo.nucleo.servos.Move')(servo_id=servo_id, position=position, speed=speed)
        await self._publish.publishTopic('nucleo/in/servo/move', msg)


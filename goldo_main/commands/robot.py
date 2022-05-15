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

    def _publish(self, topic, msg=None):
        return self._robot._broker.publishTopic(topic, msg)

    def sequence(self, func):
        return self._robot.sequence(func)

    @property
    def score(self):
        return self._robot._state_proto.score

    async def setScore(self, score):
        self._robot._state_proto.score = score

        await self._publish('gui/in/score',
                            _sym_db.GetSymbol('google.protobuf.Int32Value')(value=self._robot._state_proto.score))

    @property
    def side(self):
        return self._robot.side

    @property
    def sensors(self):
        return self._robot._state_proto.sensors

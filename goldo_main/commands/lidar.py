import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio
import struct

class LidarCommands:
    def __init__(self, robot):
        self._robot = robot

    def _publish(self, topic, msg=None):
        return self._robot._broker.publishTopic(topic, msg)

    def start(self):
        return self._publish('rplidar/in/start')

    def stop(self):
        return self._publish('rplidar/in/stop')
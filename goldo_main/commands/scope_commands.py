import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio
import functools
import math
import logging
import struct

from typing import Mapping


LOGGER = logging.getLogger(__name__)

def _variableSize(encoding):
    if encoding == 4:
        return 1
    if encoding == 5:
        return 2
    if encoding == 6:
        return 4

def _variableFactor(encoding):
    if encoding == 4:
        return 1/((1 << 8) - 1)
    if encoding == 5:
        return 1/((1 << 16) - 1)
    if encoding == 6:
        return 1/((1 << 32) - 1)

def _variableCode(encoding):
    if encoding == 4:
        return 'B'
    if encoding == 5:
        return 'H'
    if encoding == 6:
        return 'I'


class ScopeCommands:
    _broker: object

    def __init__(self):
        self._config = None
        self._ref_timestamp = 0


    def setBroker(self, broker):
        self._broker = broker
        self._broker.registerCallback('nucleo/in/propulsion/scope/config/set', self.onConfig)
        self._broker.registerCallback('nucleo/out/propulsion/scope/data', self.onData)
        self._broker.registerCallback('nucleo/out/os/heartbeat', self.onHeartBeat)

    async def onHeartBeat(self, msg):
        self._ref_timestamp = msg.timestamp

    async def onConfig(self, msg):
        print(msg)
        self._config = msg
        self._total_size = sum([_variableSize(chan.encoding) for chan in self._config.channels])
        self._factors = [_variableFactor(chan.encoding) for chan in self._config.channels]
        self._struct = struct.Struct('<' + ''.join([_variableCode(chan.encoding) for chan in self._config.channels]))

    async def onData(self, msg):
        if self._config is None:
            return
        timestamp_delta = (msg.timestamp - self._ref_timestamp) % (1 << 16)
        if timestamp_delta > (1 <<15):
            timestamp_delta -= (1 << 16)
        timestamp_base = self._ref_timestamp + timestamp_delta
        print(timestamp_base)
        out_msg = _sym_db.GetSymbol('goldo.nucleo.ScopeValues')()
        out_msg.channels.extend([_sym_db.GetSymbol('goldo.nucleo.ScopeChannelValues')() for i in range(len(self._config.channels))])
        for i in range(len(msg.data) // self._total_size):
            out_msg.timestamps.append(1e-3 * (timestamp_base + self._config.period * i))
            vals = self._struct.unpack(msg.data[i * self._total_size:(i+1) * self._total_size])
            for j in range(len(self._config.channels)):
                chan = self._config.channels[j]
                val = vals[j] * self._factors[j]
                val = val * (chan.max_value - chan.min_value) + chan.min_value
                out_msg.channels[j].float_values.append(val)
        await self._broker.publishTopic('main/propulsion/scope/values', out_msg)

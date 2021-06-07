import asyncio
import zmq
import zmq.utils.monitor
from zmq.asyncio import Context, Poller
import struct
import logging
import re
import socket
import nucleo_topics
import struct
import setproctitle

import multiprocessing
from multiprocessing import Process, Pipe

import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()

_msg_type_struct = struct.Struct('<H')
_lidar_point_struct = struct.Struct('<ff')
_lidar_detection_message_struct = struct.Struct('<IIhhhhhhI')
 
import pb2 as _pb2


from .broker.broker_process import run_broker_process, ZmqBrokerCmd


class ZmqBroker():
    def __init__(self):
        ctx = multiprocessing.get_context('spawn')
        self._conn, child_conn = ctx.Pipe()
        self._process = ctx.Process(target=run_broker_process, args=(child_conn,))
        self._process.start()
        self._message_available = asyncio.Event()
        
        loop = asyncio.get_event_loop()
        loop.add_reader(self._conn.fileno(), self._message_available.set)        
        
        self._callbacks = []
        

    def registerCallback(self, pattern: str, callback):
        pattern = (
            pattern
            .replace('*', r'([^/]+)')
            .replace('/#', r'/([^/]+)*')
            .replace('#/', r'([^/]+)/*')
            )
        self._conn.send((ZmqBrokerCmd.REGISTER_CALLBACK, pattern, len(self._callbacks)))
        self._callbacks.append(callback)
        
    def registerForward(self, pattern: str, forward_str: str):
        pattern = (
            pattern
            .replace('*', r'([^/]+)')
            .replace('/#', r'/([^/]+)*')
            .replace('#/', r'([^/]+)/*')
            )
        self._conn.send((ZmqBrokerCmd.REGISTER_FORWARD, pattern, forward_str))

    async def run(self):
        while True:
            await self._message_available.wait()
            self._message_available.clear()
            topic, msg, callbacks_list = self._conn.recv()
            await self.onTopicReceived(topic, msg, callbacks_list)
            
    async def onTopicReceived(self, topic, msg, callbacks_list):
        if msg is None:
            msg = _sym_db.GetSymbol('google.protobuf.Empty')()          
        await asyncio.wait(tuple(self._callbacks[callback_id](*groups, msg) for callback_id, groups in callbacks_list))
        
    async def publishTopic(self, topic, msg = None):
        if msg is None:
            msg = _sym_db.GetSymbol('google.protobuf.Empty')()
        self._conn.send((ZmqBrokerCmd.PUBLISH_TOPIC, topic, msg))

        






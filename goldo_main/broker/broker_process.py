import asyncio
import zmq
import zmq.utils.monitor
from zmq.asyncio import Context, Poller
import struct
import logging
import re
import socket
import struct
import setproctitle
import enum

import multiprocessing
from multiprocessing import Process, Pipe

from .zmq_codecs import *


class ZmqBrokerCmd(enum.Enum):
    PUBLISH_TOPIC = 0
    REGISTER_CALLBACK = 1
    REGISTER_FORWARD = 2
        
class ZmqBrokerProcess(object):
    socket_types = {
        'pub': zmq.PUB,
        'sub': zmq.SUB,
        'req': zmq.REQ,
        'rep': zmq.REP
        }

    def __init__(self, conn):
        self._conn = conn
        self._context = Context.instance()
        self._poller = Poller()
        self._sockets = {}
        self._monitors = {}
        self._socket_codecs = {}
        self._callbacks = []
        self._forwards = []
        ip = 'robot01'
        self.register_socket('nucleo:pub', 'tcp://{}:3002'.format(ip), 'connect', NucleoCodec())
        self.register_socket('nucleo:sub', 'tcp://{}:3001'.format(ip), 'connect', NucleoCodec())
        
        self.register_socket('nucleo_ftdi:pub', 'tcp://{}:3004'.format(ip), 'connect', NucleoCodec())
        self.register_socket('nucleo_ftdi:sub', 'tcp://{}:3003'.format(ip), 'connect', NucleoCodec())
        
        self.register_socket('rplidar:pub', 'tcp://{}:3101'.format(ip), 'connect', RPLidarCodec())
        self.register_socket('rplidar:sub', 'tcp://{}:3102'.format(ip), 'connect', RPLidarCodec())
        
        self.register_socket('camera:sub', 'tcp://{}:3201'.format(ip), 'connect', ProtobufCodec())
        
        self.register_socket('gui:pub', 'tcp://{}:3901'.format(ip), 'connect', ProtobufCodec())
        self.register_socket('gui:sub', 'tcp://{}:3902'.format(ip), 'connect', ProtobufCodec())
        
        self.register_socket('debug:pub', 'tcp://*:3801', 'bind', ProtobufCodec())
        self.register_socket('debug:sub', 'tcp://*:3802', 'bind', ProtobufCodec())
        
        self.register_socket('main:rep', 'tcp://*:3301', 'bind', ProtobufCodec())
        
        self._poller.register(self._conn, zmq.POLLIN)
        self._socket_codecs[self._conn.fileno()] = ('parent', self.onBrokerCmd)
    
    async def run(self):
        while True:
            events = await self._poller.poll()
            await asyncio.wait([self._readSocket(s, self._socket_codecs[s]) for s, e in events if e & zmq.POLLIN])
            
    async def onBrokerCmd(self, cmd):
        if cmd[0] == ZmqBrokerCmd.REGISTER_CALLBACK:
            pattern = cmd[1]
            callback_id = cmd[2]
            self._callbacks.append((re.compile(f"^{pattern}$"), callback_id))
            return
        if cmd[0] == ZmqBrokerCmd.REGISTER_FORWARD:
            pattern = cmd[1]
            self._forwards.append((re.compile(f"^{pattern}$"), cmd[2]))
            return
        if cmd[0] == ZmqBrokerCmd.PUBLISH_TOPIC:
            msg = cmd[2]
            if msg is None:
                msg = _sym_db.GetSymbol('google.protobuf.Empty')()
            await self.publishTopic(cmd[1], cmd[2])
            return

    async def _readSocket(self, socket, codec):
        if codec[0] == 'monitor':
            return await self._readSocketMonitor(socket)
        if codec[0] == 'parent':
            return await self.onBrokerCmd(self._conn.recv())
        flags = socket.getsockopt(zmq.EVENTS)
        while flags & zmq.POLLIN:
            payload = await socket.recv_multipart()
            topic, msg = codec[0].deserialize(payload)
            if topic is not None:
                await codec[1](topic, msg)
            flags = socket.getsockopt(zmq.EVENTS)
            
    async def _readSocketMonitor(self, socket_):
        flags = socket_.getsockopt(zmq.EVENTS)
        while flags & zmq.POLLIN:
            descr, endpoint = await socket_.recv_multipart()
            event, value = struct.unpack('<HI', descr)
            if event == zmq.EVENT_ACCEPTED:
                try:
                    s = socket.socket(fileno=value)
                    print(s.getpeername())
                    print(event, value)
                    s.detach()
                except:
                    print('ERR')
            flags = socket_.getsockopt(zmq.EVENTS)

    async def _writeSocket(self, socket, topic, msg):
        payload = self._socket_codecs[socket][0].serialize(topic, msg)
        if payload is not None:
            await socket.send_multipart(payload)

    async def onTopicReceived(self, topic, msg = None):
        if msg is None:
            msg = _sym_db.GetSymbol('google.protobuf.Empty')()
        callback_matches = tuple((regexp.match(topic), callback) for regexp, callback in self._callbacks)
        callbacks_list = tuple((callback, tuple(match.groups())) for match, callback in callback_matches if match)
        if len(callbacks_list):
            self._conn.send((topic, msg, callbacks_list))
            
        forwards_matches = tuple((regexp.match(topic), forward_str) for regexp, forward_str in self._forwards)
        forwards = tuple(self.publishTopic(forward_str.format(*match.groups()), msg) for match, forward_str in forwards_matches if match)
        if len(forwards):
            await asyncio.wait(forwards)
        await self.publishTopic(topic, msg)
        
    async def publishTopic(self, topic, msg):
        if topic.startswith('camera/in/'):
            await self._writeSocket(self._sockets['camera:pub'], topic, msg)
        if topic.startswith('gui/in/'):
            await self._writeSocket(self._sockets['gui:pub'], topic, msg)
        if topic.startswith('nucleo/in/'):
            await self._writeSocket(self._sockets['nucleo:pub'], topic, msg)
        if topic.startswith('rplidar/in/'):
            await self._writeSocket(self._sockets['rplidar:pub'], topic, msg)
        await self._writeSocket(self._sockets['debug:pub'], topic, msg)
        
    async def _onRequestReceived(self, topic, msg = None):
        await self._writeSocket(self._sockets['main:rep'], topic + '/resp', msg)

    def register_socket(self, name, url, connection_type, codec):
        socket_type = self.__class__.socket_types.get(name.split(':')[-1])
        socket = self._context.socket(socket_type)
        func = None
        if socket_type == zmq.PUB:
            monitor = socket.get_monitor_socket()
            self._monitors[socket] = monitor
            self._socket_codecs[monitor] = ('monitor', None)
            self._poller.register(monitor, zmq.POLLIN)            
        if socket_type == zmq.SUB:           
            socket.setsockopt(zmq.SUBSCRIBE, b'')
            self._poller.register(socket, zmq.POLLIN)
            func = self.onTopicReceived
        if socket_type == zmq.REP:
            func = self._onRequestReceived
        if connection_type == 'connect':
            socket.connect(url)
        if connection_type == 'bind':
            socket.bind(url)
        self._sockets[name] = socket
        self._socket_codecs[socket] = (codec, func)

def run_broker_process(conn):
    setproctitle.setproctitle('goldo_main.broker')
    broker = ZmqBrokerProcess(conn)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(broker.run())
    


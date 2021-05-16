import asyncio
import zmq
from zmq.asyncio import Context, Poller
import struct
import logging
import re
import nucleo_topics

import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()

_msg_type_struct = struct.Struct('<H')
_lidar_point_struct = struct.Struct('<ff')

import pb2 as _pb2

class _NucleoCodec:
    def serialize(self, topic, msg):
        msg_type, encoder = nucleo_topics._in.get(topic, (None, None))
        if encoder is None:
             print('error', topic, msg_type)
             return None
        return  [_msg_type_struct.pack(msg_type), encoder(msg)]

    def deserialize(self, payload):
        msg_type, msg_body = payload[:2]
        
        msg_type = _msg_type_struct.unpack(msg_type)[0]
        topic, decoder = nucleo_topics._out.get(msg_type, (None, None))
        if topic is not None:
            try:
                msg = decoder(msg_body)
                if msg is None:
                    msg = _sym_db.GetSymbol('google.protobuf.Empty')()
            except Exception as e:
                logging.exception(e)
                return None, None
            return topic, msg
        else:
            return None, None

class _ProtobufCodec:
    def serialize(self, topic, msg):
        return [topic.encode('utf8'),
                msg.DESCRIPTOR.full_name.encode('utf8'),
                msg.SerializeToString()
                ]

    def deserialize(self, payload):
        topic, full_name, payload = payload
        topic = topic.decode('utf8')
        full_name = full_name.decode('utf8')
        msg_class = _sym_db.GetSymbol(full_name)
        if msg_class is not None:
            msg = msg_class()
            msg.ParseFromString(payload)
            return topic, msg
        else:
            return None, None

class _RPLidarCodec:
    def serialize(self, topic, msg):
        if topic == 'rplidar/in/start':
            return [struct.pack('<b', 1), b'']
        if topic == 'rplidar/in/stop':
            return [struct.pack('<b', 2), b'']
        if topic == 'rplidar/in/config/theta_offset':
            return [struct.pack('<b', 3), struct.pack('<f', msg.value)]
        if topic == 'rplidar/in/config/distance_tresholds':
            return [struct.pack('<b', 5), struct.pack('<fff', msg.near,msg.mid,msg.far)]
        if topic == 'rplidar/in/robot_pose':
            return [struct.pack('<b', 4), struct.pack('<fff', msg.position.x, msg.position.y, msg.yaw)]
        return None

    def deserialize(self, payload):
        msg_type = struct.unpack('<B', payload[0])[0]
        if msg_type == 1:
            msg = _sym_db.GetSymbol('goldo.common.geometry.PointCloud')()
            for i in range(len(payload[2])//8):
                pt = msg.points.add()
                pt.x, pt.y = _lidar_point_struct.unpack(payload[2][i*8:(i+1)*8])
            return 'rplidar/out/scan', msg
        if msg_type == 42:
            msg = _pb2.deserialize('goldo.rplidar.Zones', payload[1])
            return 'rplidar/out/detections', msg
        return None, None

class ZmqBroker():
    socket_types = {
        'pub': zmq.PUB,
        'sub': zmq.SUB,
        'req': zmq.REQ,
        'rep': zmq.REP
        }

    def __init__(self):
        self._context = Context.instance()
        self._poller = Poller()
        self._sockets = {}
        self._socket_codecs = {}
        self._callbacks = []
        ip = 'robot01'
        self.register_socket('nucleo:pub', 'tcp://{}:3002'.format(ip), 'connect', _NucleoCodec())
        self.register_socket('nucleo:sub', 'tcp://{}:3001'.format(ip), 'connect', _NucleoCodec())
        self.register_socket('rplidar:pub', 'tcp://{}:3101'.format(ip), 'connect', _RPLidarCodec())
        self.register_socket('rplidar:sub', 'tcp://{}:3102'.format(ip), 'connect', _RPLidarCodec())
        self.register_socket('camera:sub', 'tcp://{}:3201'.format(ip), 'connect', _ProtobufCodec())
        self.register_socket('gui:pub', 'tcp://{}:3901'.format(ip), 'connect', _ProtobufCodec())
        self.register_socket('gui:sub', 'tcp://{}:3902'.format(ip), 'connect', _ProtobufCodec())
        self.register_socket('debug:pub', 'tcp://*:3801', 'bind', _ProtobufCodec())
        self.register_socket('debug:sub', 'tcp://*:3802', 'bind', _ProtobufCodec())
        self.register_socket('main:rep', 'tcp://*:3301', 'bind', _ProtobufCodec())

    def registerCallback(self, pattern: str, callback):
        pattern = (
            pattern
            .replace('*', r'([^/]+)')
            .replace('/#', r'(/[^/]+)*')
            .replace('#/', r'([^/]+/)*')
            )
        self._callbacks.append((re.compile(f"^{pattern}$"), callback))

    async def run(self):
        while True:
            events = await self._poller.poll()
            await asyncio.gather(*(self._readSocket(s, self._socket_codecs[s]) for s, e in events if e & zmq.POLLIN))

    async def _readSocket(self, socket, codec):
        flags = socket.getsockopt(zmq.EVENTS)
        while flags & zmq.POLLIN:
            payload = await socket.recv_multipart()
            topic, msg = codec[0].deserialize(payload)
            if topic is not None:
                await codec[1](topic, msg)
            flags = socket.getsockopt(zmq.EVENTS)

    async def _writeSocket(self, socket, topic, msg):
        payload = self._socket_codecs[socket][0].serialize(topic, msg)
        if payload is not None:
            await socket.send_multipart(payload)

    async def publishTopic(self, topic, msg = None):
        if msg is None:
            msg = _sym_db.GetSymbol('google.protobuf.Empty')()
        callback_matches = ((regexp.match(topic), callback) for regexp, callback in self._callbacks)
        await asyncio.gather(*(callback(*match.groups(), msg) for match, callback in callback_matches if match))
        
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
        if socket_type == zmq.SUB:
            socket.setsockopt(zmq.SUBSCRIBE, b'')
            self._poller.register(socket, zmq.POLLIN)
            func = self.publishTopic
        if socket_type == zmq.REP:
            func = self._onRequestReceived
        if connection_type == 'connect':
            socket.connect(url)
        if connection_type == 'bind':
            socket.bind(url)
        self._sockets[name] = socket
        self._socket_codecs[socket] = (codec, func)





import zmq
from zmq.asyncio import Context, Poller
import struct
import nucleo_topics

import google.protobuf.wrappers_pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()


class ZmqBroker():
    socket_types = {
        'pub': zmq.PUB,
        'sub': zmq.SUB,
        'req': zmq.REQ
        }
        
    def __init__(self):
        self._context = Context.instance()
        self._poller = Poller()
        self._sockets = {}
        self._socket_decoders = {}
        ip = 'robot01'
        self.register_socket('nucleo:pub', 'tcp://{}:3002'.format(ip), 'connect')
        self.register_socket('nucleo:sub', 'tcp://{}:3001'.format(ip), 'connect')
        #self.register_socket('rplidar:req', 'tcp://{}:3012'.format(ip), 'connect')
        #self.register_socket('rplidar:sub', 'tcp://{}:3011'.format(ip), 'connect')
        self.register_socket('camera:sub', 'tcp://{}:3201'.format(ip), 'connect')
        self.register_socket('gui:pub', 'tcp://{}:3901'.format(ip), 'connect')
        self.register_socket('gui:sub', 'tcp://{}:3902'.format(ip), 'connect')
        #self.register_socket('camera:req', 'tcp://{}:3001'.format(ip), 'connect')
        self.register_socket('debug:pub', 'tcp://*:3801', 'bind')
        self.register_socket('debug:sub', 'tcp://*:3802', 'bind')
        
    async def run(self):
        while True:
            events = dict(await self._poller.poll())
            if events.get(self._sockets['nucleo:sub'],0) & zmq.POLLIN:
                msg_type, msg_body = await self._sockets['nucleo:sub'].recv_multipart()
                msg_type = struct.unpack('<H', msg_type)[0]
                topic, decoder = nucleo_topics._out.get(msg_type, (None, None))
                if topic is not None:
                    msg = decoder(msg_body)
                    await self.publishTopic(topic, msg)
            if events.get(self._sockets['debug:sub'],0) & zmq.POLLIN:
                await self._readSocket(self._sockets['debug:sub'])
            if events.get(self._sockets['camera:sub'],0) & zmq.POLLIN:
                await self._readSocket(self._sockets['camera:sub'])
            if events.get(self._sockets['gui:sub'],0) & zmq.POLLIN:
                await self._readSocket(self._sockets['gui:sub'])
                
    async def _readSocket(self, socket):
        flags = socket.getsockopt(zmq.EVENTS)        
        while flags & zmq.POLLIN:
            topic, full_name, payload = await socket.recv_multipart()
            topic = topic.decode('utf8')
            full_name = full_name.decode('utf8')
            msg_class = _sym_db.GetSymbol(full_name)
            if msg_class is not None:
                msg = msg_class()
                msg.ParseFromString(payload)
            else:
                msg = None
            await self.publishTopic(topic, msg)
            if topic == 'camera/out/image':
                await self.publishTopic('gui/in/camera/image', msg)
            flags = socket.getsockopt(zmq.EVENTS)
        
    async def _writeSocket(self, socket, topic, msg):
        await socket.send_multipart([topic.encode('utf8'),
                                     msg.DESCRIPTOR.full_name.encode('utf8'),
                                     msg.SerializeToString()])
                               
    async def publishTopic(self, topic, msg):
        # Forward nucleo topics to comm_uart socket while encoding message
        if topic.startswith('nucleo/in/'):
            msg_type, encoder = nucleo_topics._in.get(topic, (None, None))
            if encoder is None:
                print('error', topic, msg_type)
                return
            payload = encoder(msg)
            await self._sockets['nucleo:pub'].send_multipart([struct.pack('<H',msg_type), payload])     
        if topic.startswith('gui/in/'):
            await self._writeSocket(self._sockets['gui:pub'], topic, msg)
        await self._writeSocket(self._sockets['debug:pub'], topic, msg)
        
    def register_socket(self, name, url, connection_type):
        socket_type = self.__class__.socket_types.get(name.split(':')[-1])
            
        socket = self._context.socket(socket_type)
        if socket_type == zmq.SUB:
            socket.setsockopt(zmq.SUBSCRIBE,b'')
        if connection_type == 'connect':
            socket.connect(url)
        if connection_type == 'bind':
            socket.bind(url)
       
        self._sockets[name] = socket
        self._poller.register(socket, zmq.POLLIN)




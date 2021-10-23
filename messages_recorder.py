import zmq
import time
import struct
import pathlib

import google.protobuf.descriptor_pool
import google.protobuf.reflection
from google.protobuf.descriptor import MakeDescriptor
from google.protobuf.message_factory import MessageFactory
from google.protobuf.descriptor_pb2 import DescriptorProto,  FieldDescriptorProto, FileDescriptorProto
import struct

pool = google.protobuf.descriptor_pool.Default()

import pb2

def topological_sort(dependencies):
    vertices = list(dependencies.keys())
    visited = {k: False for k in vertices}
    edges = {k:list(v) for k,v in dependencies.items()}
    stack = []
    
    def sortUtil(v):
        visited[v] = True
        for n in edges[v]:
            if visited[n] == False:
                sortUtil(n)
        stack.append(v)
    for v in vertices:
        if visited[v] == False:
            sortUtil(v)
    return stack[::-1]
    

    
def write_rec_header(file):
    d = DescriptorProto(name='RecordFileHeader', field = [
    FieldDescriptorProto(
        name='data',
        number=1,
        label=FieldDescriptorProto.LABEL_REPEATED,
        type=FieldDescriptorProto.TYPE_BYTES)
    ])

    d = MakeDescriptor(d)
    message_factory = MessageFactory()
    RecFileHeader = message_factory.GetPrototype(d)

    file_descriptors_protos = {}

    for k, v in  pool._file_descriptors.items():
        if k.startswith('goldo/'):
            dp = FileDescriptorProto()
            v.CopyToProto(dp)
            file_descriptors_protos[k] = dp
            
    dependents = {}

    for k, v in file_descriptors_protos.items():
        dependents.setdefault(k, set())
        for d in v.dependency:
            if d.startswith('goldo/'):
                dependents.setdefault(d, set()).add(k)
            
    files = topological_sort(dependents)

    header = RecFileHeader(data=[file_descriptors_protos[n].SerializeToString() for n in files]).SerializeToString()
        
    file.write(b'goldo_rec' + struct.pack('<I', len(header)))
    file.write(header)
    file.flush()

def main():
    ip = 'robot01'
    
    #find next filename
    i = 0
    while True:        
        log_path = pathlib.Path('recordings/rec_{}.bin'.format(i))
        if not log_path.is_file():
            break
        i += 1
    
    #open log file
    file = open(log_path, 'wb')
    write_rec_header(file)
    start_ts = time.time()
    last_flush_ts = start_ts
    
    context = zmq.Context()    
    socket_sub = context.socket(zmq.SUB)
    socket_sub.connect('tcp://{}:3801'.format(ip))
    socket_sub.setsockopt(zmq.SUBSCRIBE,b'')
    
    while True:
        topic, full_name, payload = socket_sub.recv_multipart()
        ts = time.time()
        
        header = struct.pack('<IIII', int((ts - start_ts) * 1000), len(topic), len(full_name), len(payload))
        file.write(header)
        file.write(topic)
        file.write(full_name)
        file.write(payload)
        
        if ts - last_flush_ts >= 1:
            last_flush_ts = ts
            file.flush()
        
        
if __name__ == '__main__':
    main()
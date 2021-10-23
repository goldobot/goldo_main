import google.protobuf.descriptor_pool
import google.protobuf.reflection
from google.protobuf.descriptor import MakeDescriptor
from google.protobuf.message_factory import MessageFactory
from google.protobuf.descriptor_pb2 import DescriptorProto,  FieldDescriptorProto, FileDescriptorProto
import struct

pool = google.protobuf.descriptor_pool.Default()

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
    
d = DescriptorProto(name='RecordFileHeader', field = [
    FieldDescriptorProto(
        name='data',
        number=1,
        label=FieldDescriptorProto.LABEL_REPEATED,
        type=FieldDescriptorProto.TYPE_BYTES)
])


    
def write_rec_header(file):
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
    
    




    

import pb2 as _pb2
import struct

from goldo_main.nucleo.topics._registry import *

_sym_db = _pb2._sym_db

@nucleo_out('servo/ack', 40)
def servo_ack(payload):
    return _sym_db.GetSymbol('google.protobuf.UInt32Value')(value=struct.unpack('<H', payload)[0])
    
@nucleo_in('servo/disable_all', 45)
def servo_disable_all(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('servo/enable/set', 42)
def servo_set_enable(msg):
    return struct.pack('<H', msg.sequence_number) + b''.join([_pb2.serialize(enable) for enable in msg.enables])

@nucleo_in('servo/move_multiple', 41)
def servo_move_multiple(msg):
    return struct.pack('<HH', msg.sequence_number, msg.speed) + b''.join([_pb2.serialize(pos) for pos in msg.positions])

@nucleo_in('lift/do_homing', 48)
def lift_do_homing(msg):
    return _pb2.serialize(msg)

@nucleo_out('servo/status/moving', 44)
def servo_status_moving(payload):
    msg = _sym_db.GetSymbol('google.protobuf.UInt32Value')(value=struct.unpack('<I', payload)[0])
    return msg



import goldo_main.pb2 as _goldo_pb
import google.protobuf as _pb
import struct

_sym_db = _pb.symbol_database.Default()

_in = {}
_out = {}

def nucleo_out(topic, msg_type):
    def register_out(fn):
        _out[msg_type] = ('nucleo/out/' + topic, fn)
    return register_out

def nucleo_in(topic, msg_type):
    def register_in(fn):
        _in['nucleo/in/' + topic] = (msg_type, fn)
    return register_in
        
@nucleo_out('os/heartbeat', 2)
def heartbeat(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.Heartbeat')()
    msg.timestamp = struct.unpack('<I', payload)[0]
    return msg
    
@nucleo_out('robot/config/load_status', 9)
def robot_config_load_status(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadStatus')()
    msg.status = struct.unpack('<B', payload)[0]
    return msg
    
@nucleo_in('robot/config/load_begin', 6)
def robot_config_load_begin(msg):
    return struct.pack('<H', msg.size)
    
@nucleo_in('robot/config/load_chunk', 7)
def robot_config_load_chunk(msg):
    return msg.data
    
@nucleo_in('robot/config/load_end', 8)
def robot_config_load_end(msg):
    return struct.pack('<H', msg.crc)
    
@nucleo_in('nucleo/in/odrive/request', 10)
def odrive_request(msg):
    buff = struct.pack('<HHH', msg.sequence_number, msg.endpoint_id, msg.expected_response_size)
    buff += msg.payload
    buff += struct.pack('<H', msg.protocol_version)
    return buff
    
@nucleo_in('nucleo/in/propulsion/enable/set', 22)
def propulsion_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('nucleo/in/propulsion/motors/enable/set', 23)
def propulsion_motors_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('nucleo/in/propulsion/motors/velocity_setpoints/set', 24)
def propulsion_motors_velocity_setpoints_set(msg):
    return struct.pack('<ff', msg.left_vel, msg.right_vel)
    
@nucleo_in('nucleo/in/propulsion/execute_rotation', 28)
def propulsion_motors_velocity_setpoints_set(msg):
    return struct.pack('<ffff', msg.yaw_delta, msg.yaw_rate, msg.accel, msg.deccel)
    
@nucleo_in('nucleo/in/propulsion/execute_translation', 31)
def propulsion_motors_velocity_setpoints_set(msg):
    return struct.pack('<ffff', msg.distance, msg.speed, msg.accel, msg.deccel)
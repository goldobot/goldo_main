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
    
@nucleo_in('odrive/request', 10)
def odrive_request(msg):
    buff = struct.pack('<HHH', msg.sequence_number, msg.endpoint_id, msg.expected_response_size)
    buff += msg.payload
    buff += struct.pack('<H', msg.protocol_version)
    return buff

@nucleo_in('odometry/config/get', 40)
def odometry_config_get(msg):
    return b''
    
@nucleo_out('odometry/config', 41)
def odometry_config_get_status(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.odometry.Config')()
    vals = struct.unpack('<ffffffHH', payload) 
    msg.dist_per_count_left = vals[0]
    msg.dist_per_count_right = vals[1]
    msg.wheel_distance_left = vals[2]
    msg.wheel_distance_right = vals[3]
    msg.speed_filter_frequency = vals[4]
    msg.accel_filter_frequency = vals[5]
    msg.encoder_period = vals[6]
    return msg
        
@nucleo_in('odometry/config/set', 42)
def odometry_config_set(msg):
    return struct.pack('<ffffffHH', 
        msg.dist_per_count_left,
        msg.dist_per_count_right,
        msg.wheel_distance_left,
        msg.wheel_distance_right,
        msg.speed_filter_frequency,
        msg.accel_filter_frequency,
        msg.encoder_period,
        0        
        )
    
@nucleo_in('propulsion/enable/set', 22)
def propulsion_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('propulsion/motors/enable/set', 23)
def propulsion_motors_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('propulsion/motors/velocity_setpoints/set', 24)
def propulsion_motors_velocity_setpoints_set(msg):
    return struct.pack('<ffff', msg.left_vel, msg.right_vel, msg.left_current_feedforward, msg.right_current_feedforward)
    
@nucleo_in('propulsion/execute_rotation', 28)
def propulsion_motors_velocity_setpoints_set(msg):
    return struct.pack('<ffff', msg.yaw_delta, msg.yaw_rate, msg.accel, msg.deccel)
    
@nucleo_in('propulsion/execute_translation', 31)
def propulsion_motors_velocity_setpoints_set(msg):
    return struct.pack('<ffff', msg.distance, msg.speed, msg.accel, msg.deccel)
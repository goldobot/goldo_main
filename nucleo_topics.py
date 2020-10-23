import pb2 as _pb2
import google.protobuf as _pb
import struct
import math

_sym_db = _pb.symbol_database.Default()

_in = {}
_out = {}

_msg_propulsion_Telemetry =  _sym_db.GetSymbol('goldo.nucleo.propulsion.Telemetry')
_unpack_propulsion_Telemetry = struct.Struct('<hhhhhhhHHbbBB').unpack
_unpack_heartbeat = struct.Struct('<I').unpack

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
    msg.timestamp = _unpack_heartbeat(payload)[0]
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
    
@nucleo_out('odrive/response', 11)
def odrive_response(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.odrive.ResponsePacket')()
    msg.sequence_number = struct.unpack('<H', payload[0:2])[0] & 0x7fff
    msg.payload = payload[2:]    
    return msg

@nucleo_in('dynamixels/request/read', 42)
def dynamixels_request(msg):
    return _pb2.serialize(msg)
    
@nucleo_out('dynamixels/response', 20)
def dynamixels_response(payload):
    return _pb2.deserialize('goldo.nucleo.fpga.RegReadStatus', payload)

@nucleo_in('fpga/reg/read', 19)
def fpga_reg_read(msg):
    return _pb2.serialize(msg)
    
@nucleo_out('fpga/reg', 20)
def fpga_reg_read_status(payload):
    return _pb2.deserialize('goldo.nucleo.fpga.RegReadStatus', payload)
    
@nucleo_in('fpga/reg/write', 21)
def fpga_reg_write(msg):
    return _pb2.serialize(msg)

@nucleo_in('fpga/reg/write', 21)
def fpga_reg_read(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('odometry/config/get', 40)
def odometry_config_get(msg):
    return b''
    
@nucleo_out('odometry/config', 41)
def odometry_config_get_status(payload):
    return _pb2.deserialize('goldo.nucleo.propulsion.OdometryConfig', payload)

@nucleo_in('odometry/config/set', 42)
def odometry_config_set(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/config/get', 43)
def propulsion_config_get(msg):
    return b''
    
@nucleo_out('propulsion/config', 44)
def propulsion_config_get_status(payload):
    return _pb2.deserialize('goldo.nucleo.propulsion.PropulsionControllerConfig', payload)

@nucleo_in('propulsion/config/set', 45)
def propulsion_config_set(msg):
    return _pb2.serialize(msg)

@nucleo_in('propulsion/enable/set', 22)
def propulsion_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('propulsion/motors/enable/set', 23)
def propulsion_motors_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('propulsion/motors/velocity_setpoints/set', 24)
def propulsion_motors_velocity_setpoints_set(msg):
    return struct.pack('<ffff', msg.left_vel, msg.right_vel, msg.left_current_feedforward, msg.right_current_feedforward)
    
@nucleo_in('propulsion/pose/set', 27)
def propulsion_pose_set(msg):
    return struct.pack('<fff', msg.position.x, msg.position.y, msg.yaw)
    
@nucleo_in('propulsion/execute_rotation', 28)
def propulsion_execute_rotation(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/execute_translation', 31)
def propulsion_execute_translation(msg):
    return _pb2.serialize(msg)
    
@nucleo_out('propulsion/telemetry', 25)
def propulsion_telemetry(payload):
    msg = _msg_propulsion_Telemetry()
    vals = _unpack_propulsion_Telemetry(payload)
    msg.pose.position.x = vals[0] * 0.25e-3
    msg.pose.position.y = vals[1] * 0.25e-3
    msg.pose.yaw = vals[2] * math.pi / 32767
    msg.pose.speed = vals[3] * 1e-3
    msg.pose.yaw_rate = vals[4] * 1e-3
    msg.pose.acceleration = vals[5] * 1e-3
    msg.pose.angular_acceleration = vals[6] * 1e-3
    msg.left_encoder = vals[7]
    msg.right_encoder = vals[8]
    msg.left_pwm = vals[9] * 1e-2
    msg.right_pwm = vals[10] * 1e-2
    msg.state = vals[11]
    msg.error = vals[12]
    return msg

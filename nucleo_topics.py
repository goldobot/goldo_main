import pb2 as _pb2
import struct
import math

_sym_db = _pb2._sym_db

_in = {}
_out = {}

_msg_propulsion_Telemetry =  _sym_db.GetSymbol('goldo.nucleo.propulsion.Telemetry')
_unpack_propulsion_Telemetry = struct.Struct('<hhhhhhhHHbbBB').unpack

_msg_propulsion_TelemetryEx =  _sym_db.GetSymbol('goldo.nucleo.propulsion.TelemetryEx')
_unpack_propulsion_TelemetryEx = struct.Struct('<hhhhhhhhhh').unpack

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

@nucleo_in('os/ping', 1)
def ping(msg):
    return b''
    
@nucleo_out('os/heap_stats', 3)
def watchdog_state(payload):
    return _pb2.deserialize('goldo.nucleo.FreeRTOSHeapStats', payload[:8])  
    
@nucleo_out('os/reset', 4)
def os_reset(payload):
    return _sym_db.GetSymbol('google.protobuf.Empty')()
    
@nucleo_out('os/task_statistics/uart_comm', 300)
def os_task_statistics_uart_comm(payload):
    return _pb2.deserialize('goldo.nucleo.statistics.UARTCommTaskStatistics', payload)
    

@nucleo_out('os/task_statistics/odrive_comm', 301)
def os_task_statistics_odrive_comm(payload):
    return _pb2.deserialize('goldo.nucleo.statistics.ODriveCommTaskStatistics', payload)    
    
@nucleo_out('os/task_statistics/propulsion', 302)
def os_task_statistics_uart_comm(payload):
    return _pb2.deserialize('goldo.nucleo.statistics.PropulsionTaskStatistics', payload)
    
    
@nucleo_out('watchdog/state', 251)
def watchdog_state(payload):
    return _pb2.deserialize('goldo.nucleo.WatchdogState', payload[:6])    
    
@nucleo_out('sensors/state', 33)
def sensors_state(payload):
    return _pb2.deserialize('goldo.nucleo.SensorsState', payload)    
    
@nucleo_out('match/timer', 10)
def match_timer(payload):
    return _pb2.deserialize('google.protobuf.Int32Value', payload)
    
@nucleo_in('match/timer/start', 11)
def match_timer_start(msg):
    return b''    
    
@nucleo_out('match/end', 12)
def match_end(payload):
    return None
    
@nucleo_in('robot/config/load_begin', 200)
def robot_config_load_begin(msg):
    return struct.pack('<H', msg.size)
    
@nucleo_in('robot/config/load_chunk', 201)
def robot_config_load_chunk(msg):
    return msg.data
    
@nucleo_in('robot/config/load_end', 202)
def robot_config_load_end(msg):
    return struct.pack('<H', msg.crc)
    
@nucleo_out('robot/config/load_status', 203)
def robot_config_load_status(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadStatus')()
    msg.status = struct.unpack('<B', payload)[0]
    return msg
    
@nucleo_in('odrive/request', 50)
def odrive_request(msg):
    # bit 15 is reserved by odrive protocol, bit 14 is set to 0
    buff = struct.pack('<HHH', msg.sequence_number & 0x3fff, msg.endpoint_id, msg.expected_response_size)
    buff += msg.payload
    buff += struct.pack('<H', msg.protocol_version)
    return buff
    
@nucleo_out('odrive/response', 51)
def odrive_response(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.odrive.ResponsePacket')()
    msg.sequence_number = struct.unpack('<H', payload[0:2])[0] & 0x3fff
    msg.payload = payload[2:]    
    return msg
    
@nucleo_out('odrive/telemetry', 52)
def odrive_telemetry(payload):
    return _pb2.deserialize('goldo.nucleo.odrive.Telemetry', payload)
    
@nucleo_in('dynamixels/request', 60)
def dynamixels_request(msg):
    buff = struct.pack('<Hbbb',
        msg.sequence_number,
        msg.protocol_version,
        msg.id,
        msg.command
        )
    buff = buff + msg.payload
    return buff
    
@nucleo_out('dynamixels/response', 61)
def dynamixels_response(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.dynamixels.ResponsePacket')()
    vals = struct.unpack('<HBBB', payload[0:5])
    msg.sequence_number = vals[0]
    msg.protocol_version = vals[1]
    msg.id = vals[2]
    msg.error_flags = vals[3]
    msg.payload = payload[4:]
    return msg
    

@nucleo_in('fpga/reg/read', 30)
def fpga_reg_read(msg):
    return _pb2.serialize(msg)
    
@nucleo_out('fpga/reg', 31)
def fpga_reg_read_status(payload):
    return _pb2.deserialize('goldo.nucleo.fpga.RegReadStatus', payload)
    
@nucleo_in('fpga/reg/write', 32)
def fpga_reg_write(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('servo/move', 40)
def servo_move(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('servo/enable/set', 42)
def servo_move(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('servo/move_multiple', 41)
def servo_move_multiple(msg):
    return struct.pack('<HH', msg.sequence_number, msg.speed) + b''.join([_pb2.serialize(pos) for pos in msg.positions])
  
@nucleo_in('lift/set_enable', 46)
def lift_do_homing(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('lift/do_homing', 48)
def lift_do_homing(msg):
    return _pb2.serialize(msg)
    
    
@nucleo_out('servo/move_multiple', 41)
def servo_status_move_multiple(payload):
    msg = _sym_db.GetSymbol('google.protobuf.UInt32Value')(value=struct.unpack('<H', payload)[0])
    return msg
    
@nucleo_out('servo/status/moving', 44)
def servo_status_moving(payload):
    msg = _sym_db.GetSymbol('google.protobuf.UInt32Value')(value=struct.unpack('<I', payload)[0])
    return msg
    
@nucleo_in('odometry/config/get', 210)
def odometry_config_get(msg):
    return b''
    
@nucleo_out('odometry/config', 211)
def odometry_config_get_status(payload):
    return _pb2.deserialize('goldo.nucleo.propulsion.OdometryConfig', payload)

@nucleo_in('odometry/config/set', 212)
def odometry_config_set(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/config/get', 215)
def propulsion_config_get(msg):
    return b''
    
@nucleo_out('propulsion/config', 216)
def propulsion_config_get_status(payload):
    return _pb2.deserialize('goldo.nucleo.propulsion.PropulsionControllerConfig', payload)

@nucleo_in('propulsion/config/set', 217)
def propulsion_config_set(msg):
    return _pb2.serialize(msg)

@nucleo_in('propulsion/enable/set', 100)
def propulsion_enable_set(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/simulation/enable', 110)
def propulsion_simulation_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('propulsion/motors/enable/set', 101)
def propulsion_motors_enable_set(msg):
    return struct.pack('<B', msg.value)
    
@nucleo_in('propulsion/emergency_stop', 107)
def propulsion_emergency_stop(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/clear_error', 108)
def propulsion_clear_error(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/motors/velocity_setpoints/set', 102)
def propulsion_motors_velocity_setpoints_set(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/target_speed/set', 103)
def propulsion_target_speed_set(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/motors/acceleration_limits/set', 104)
def propulsion_acceleration_limits_set(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/motors/torque_limits/set', 112)
def propulsion_torque_limits_set(msg):
    return _pb2.serialize(msg)

@nucleo_in('propulsion/pose/set', 105)
def propulsion_pose_set(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/calibrate_odrive', 151)
def propulsion_calibrate_odrive(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/odrive/clear_errors', 152)
def propulsion_odrive_clear_errors(msg):
    return _pb2.serialize(msg)
    
@nucleo_out('propulsion/odrive/statistics', 180)
def propulsion_odrive_statistics(payload):
    return _pb2.deserialize('goldo.nucleo.odrive.ClientStatistics', payload[:9])

    
@nucleo_out('propulsion/odrive/axis_states', 181)
def propulsion_odrive_axis_states(payload):
    msg = _pb2.deserialize('goldo.nucleo.odrive.AxisStates', payload)
    return msg
    
@nucleo_out('propulsion/odrive/errors', 182)
def propulsion_odrive_errors(payload):
    msg = _pb2.deserialize('goldo.nucleo.odrive.AxisErrorStates', payload)
    return msg
    
@nucleo_in('propulsion/clear_command_queue', 109)
def propulsion_clear_command_queue(msg):
    return _pb2.serialize(msg)
 
@nucleo_in('propulsion/cmd/translation', 140)
def propulsion_execute_translation(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/reposition', 149)
def propulsion_execute_reposition(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/measure_normal', 146)
def propulsion_execute_reposition(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/move_to', 141)
def propulsion_execute_move_to(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/rotation', 142)
def propulsion_execute_rotation(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/point_to', 143)
def propulsion_execute_point_to(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/point_to_back', 153)
def propulsion_execute_point_to(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/face_direction', 144)
def propulsion_execute_face_direction(msg):
    return _pb2.serialize(msg)
    
@nucleo_in('propulsion/cmd/trajectory', 145)
def propulsion_execute_trajectory(msg):
    return struct.pack('<HHf', msg.sequence_number, 0, msg.speed) + b''.join([_pb2.serialize(p) for p in msg.points])
 
@nucleo_out('propulsion/cmd_event', 130)
def propulsion_cmd_ack(payload):
    return _pb2.deserialize('goldo.nucleo.propulsion.CommandStatus', payload)
    
@nucleo_out('propulsion/telemetry', 120)
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
    
@nucleo_out('propulsion/telemetry_ex', 121)
def propulsion_telemetry(payload):
    msg = _msg_propulsion_TelemetryEx()
    vals = _unpack_propulsion_TelemetryEx(payload)
    msg.target_pose.position.x = vals[0] * 0.25e-3
    msg.target_pose.position.y = vals[1] * 0.25e-3
    msg.target_pose.yaw = vals[2] * math.pi / 32767
    msg.target_pose.speed = vals[3] * 1e-3
    msg.target_pose.yaw_rate = vals[4] * 1e-3
    msg.error_longi = vals[5] * 0.25e-3
    msg.error_lateral = vals[6] * 0.25e-3
    msg.error_speed = vals[7] * 1e-3
    msg.error_yaw = vals[8]  * math.pi / 32767
    msg.error_yaw_rate = vals[9]    
    return msg
    
@nucleo_out('propulsion/odrive/telemetry', 124)
def propulsion_telemetry(payload):
    return _pb2.deserialize('goldo.nucleo.odrive.Telemetry', payload)
    
@nucleo_in('propulsion/scope/config/set', 111)
def propulsion_scope_config_set(msg):
    if len(msg.channels) > 8:
        raise RuntimeError('ScopeConfig channels count > 8')
    return struct.pack('<HH', msg.period, len(msg.channels)) + b''.join([_pb2.serialize(channel) for channel in msg.channels])

@nucleo_out('propulsion/scope/data', 125)
def propulsion_scope(payload):
    msg = _sym_db.GetSymbol('goldo.nucleo.ScopeData')()
    msg.timestamp = struct.unpack('<H', payload[0:2])[0]
    msg.data = payload[2:]
    return msg
    
@nucleo_in('dbg_goldo', 29)
def dbg_goldo_in(msg):
    #print ("in : {:x}".format(msg.value))
    return struct.pack('<I', msg.value)
    
@nucleo_out('dbg_goldo', 29)
def dbg_goldo_out(payload):
    val = struct.unpack("<I", payload)
    #print ("out : {:x}".format(val[0]))
    msg = _sym_db.GetSymbol('google.protobuf.UInt32Value')(value = val[0])
    return msg
    

import pb2 as _pb2

from goldo_main.nucleo.topics._registry import *

_sym_db = _pb2._sym_db

@nucleo_out('propulsion/controller/event', 131)
def propulsion_controller_event(payload):
    msg = _pb2.deserialize('goldo.nucleo.propulsion.PropulsionEvent', payload[:41])
    print(msg)
    return msg

@nucleo_in('propulsion/pose/transform', 113)
def propulsion_transform_pose(msg):
    return _pb2.serialize(msg)

@nucleo_in('propulsion/set_event_sensors_mask', 114)
def propulsion_set_event_sensors_mask(msg):
    return _pb2.serialize(msg)

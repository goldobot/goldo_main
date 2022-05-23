# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo/servos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo import pb2_options_pb2 as goldo_dot_pb2__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/nucleo/servos.proto',
  package='goldo.nucleo.servos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19goldo/nucleo/servos.proto\x12\x13goldo.nucleo.servos\x1a\x17goldo/pb2_options.proto\"\xe3\x01\n\x0bServoConfig\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32\x1e.goldo.nucleo.servos.ServoTypeB\x04\x80\xb5\x18\x03\x12\x10\n\x02id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08\x63w_limit\x18\x03 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tccw_limit\x18\x04 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tmax_speed\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x18\n\nmax_torque\x18\x06 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x16\n\x08reserved\x18\x64 \x01(\x05\x42\x04\x80\xb5\x18\x0c\x12\x12\n\x04name\x18@ \x01(\tB\x04\x80\xb5\x18\x0c\"\x8a\x01\n\nLiftConfig\x12\x10\n\x02kp\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x07\x12\x10\n\x02ki\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x07\x12\x10\n\x02kd\x18\x03 \x01(\x05\x42\x04\x80\xb5\x18\x07\x12\x13\n\x05range\x18\x04 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tpwm_clamp\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x18\n\nblock_trig\x18\x06 \x01(\x05\x42\x04\x80\xb5\x18\x05\"b\n\nServoState\x12\x16\n\x08position\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\x12\x1f\n\x11measured_position\x18\x03 \x01(\rB\x04\x80\xb5\x18\x05\x12\x1b\n\rmeasured_load\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x04\"W\n\x0bServoStates\x12\x17\n\ttimestamp\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12/\n\x06servos\x18\x04 \x03(\x0b\x32\x1f.goldo.nucleo.servos.ServoState\"?\n\rServoPosition\x12\x16\n\x08servo_id\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08position\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\";\n\x0bServoTorque\x12\x16\n\x08servo_id\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x14\n\x06torque\x18\x02 \x01(\rB\x04\x80\xb5\x18\x03\";\n\x0bServoEnable\x12\x16\n\x08servo_id\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x14\n\x06\x65nable\x18\x02 \x01(\x08\x42\x04\x80\xb5\x18\x03\".\n\rCmdDisableAll\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\"`\n\x0c\x43mdSetEnable\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x31\n\x07\x65nables\x18\x02 \x03(\x0b\x32 .goldo.nucleo.servos.ServoEnable\"G\n\x0f\x43mdLiftDoHoming\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x15\n\x07lift_id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\"\xd2\x01\n\x0b\x43mdLiftsRaw\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x1a\n\x0clift1_target\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x06\x12\x1a\n\x0clift1_bltrig\x18\x03 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x19\n\x0blift1_speed\x18\x04 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x1a\n\x0clift2_target\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x06\x12\x1a\n\x0clift2_bltrig\x18\x06 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x19\n\x0blift2_speed\x18\x07 \x01(\x05\x42\x04\x80\xb5\x18\x05\"^\n\x10\x43mdLiftSetEnable\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x15\n\x07lift_id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x14\n\x06\x65nable\x18\x03 \x01(\x08\x42\x04\x80\xb5\x18\x03\"|\n\x0f\x43mdMoveMultiple\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x13\n\x05speed\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x35\n\tpositions\x18\x03 \x03(\x0b\x32\".goldo.nucleo.servos.ServoPosition\"d\n\x10\x43mdSetMaxTorques\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x31\n\x07torques\x18\x02 \x03(\x0b\x32 .goldo.nucleo.servos.ServoTorque*^\n\tServoType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x12\n\x0e\x44YNAMIXEL_AX12\x10\x02\x12\x12\n\x0e\x44YNAMIXEL_MX28\x10\x03\x12\x0e\n\nGOLDO_LIFT\x10\x04\x62\x06proto3')
  ,
  dependencies=[goldo_dot_pb2__options__pb2.DESCRIPTOR,])

_SERVOTYPE = _descriptor.EnumDescriptor(
  name='ServoType',
  full_name='goldo.nucleo.servos.ServoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIXEL_AX12', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIXEL_MX28', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLDO_LIFT', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1578,
  serialized_end=1672,
)
_sym_db.RegisterEnumDescriptor(_SERVOTYPE)

ServoType = enum_type_wrapper.EnumTypeWrapper(_SERVOTYPE)
UNKNOWN = 0
STANDARD = 1
DYNAMIXEL_AX12 = 2
DYNAMIXEL_MX28 = 3
GOLDO_LIFT = 4



_SERVOCONFIG = _descriptor.Descriptor(
  name='ServoConfig',
  full_name='goldo.nucleo.servos.ServoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='goldo.nucleo.servos.ServoConfig.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='goldo.nucleo.servos.ServoConfig.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cw_limit', full_name='goldo.nucleo.servos.ServoConfig.cw_limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ccw_limit', full_name='goldo.nucleo.servos.ServoConfig.ccw_limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_speed', full_name='goldo.nucleo.servos.ServoConfig.max_speed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_torque', full_name='goldo.nucleo.servos.ServoConfig.max_torque', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved', full_name='goldo.nucleo.servos.ServoConfig.reserved', index=6,
      number=100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\014'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='goldo.nucleo.servos.ServoConfig.name', index=7,
      number=64, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\014'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=303,
)


_LIFTCONFIG = _descriptor.Descriptor(
  name='LiftConfig',
  full_name='goldo.nucleo.servos.LiftConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kp', full_name='goldo.nucleo.servos.LiftConfig.kp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ki', full_name='goldo.nucleo.servos.LiftConfig.ki', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kd', full_name='goldo.nucleo.servos.LiftConfig.kd', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='goldo.nucleo.servos.LiftConfig.range', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pwm_clamp', full_name='goldo.nucleo.servos.LiftConfig.pwm_clamp', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_trig', full_name='goldo.nucleo.servos.LiftConfig.block_trig', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=444,
)


_SERVOSTATE = _descriptor.Descriptor(
  name='ServoState',
  full_name='goldo.nucleo.servos.ServoState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='goldo.nucleo.servos.ServoState.position', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measured_position', full_name='goldo.nucleo.servos.ServoState.measured_position', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measured_load', full_name='goldo.nucleo.servos.ServoState.measured_load', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\004'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=544,
)


_SERVOSTATES = _descriptor.Descriptor(
  name='ServoStates',
  full_name='goldo.nucleo.servos.ServoStates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='goldo.nucleo.servos.ServoStates.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='servos', full_name='goldo.nucleo.servos.ServoStates.servos', index=1,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=633,
)


_SERVOPOSITION = _descriptor.Descriptor(
  name='ServoPosition',
  full_name='goldo.nucleo.servos.ServoPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servo_id', full_name='goldo.nucleo.servos.ServoPosition.servo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='goldo.nucleo.servos.ServoPosition.position', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=698,
)


_SERVOTORQUE = _descriptor.Descriptor(
  name='ServoTorque',
  full_name='goldo.nucleo.servos.ServoTorque',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servo_id', full_name='goldo.nucleo.servos.ServoTorque.servo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torque', full_name='goldo.nucleo.servos.ServoTorque.torque', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=759,
)


_SERVOENABLE = _descriptor.Descriptor(
  name='ServoEnable',
  full_name='goldo.nucleo.servos.ServoEnable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servo_id', full_name='goldo.nucleo.servos.ServoEnable.servo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='goldo.nucleo.servos.ServoEnable.enable', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=820,
)


_CMDDISABLEALL = _descriptor.Descriptor(
  name='CmdDisableAll',
  full_name='goldo.nucleo.servos.CmdDisableAll',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.servos.CmdDisableAll.sequence_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=822,
  serialized_end=868,
)


_CMDSETENABLE = _descriptor.Descriptor(
  name='CmdSetEnable',
  full_name='goldo.nucleo.servos.CmdSetEnable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.servos.CmdSetEnable.sequence_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enables', full_name='goldo.nucleo.servos.CmdSetEnable.enables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=870,
  serialized_end=966,
)


_CMDLIFTDOHOMING = _descriptor.Descriptor(
  name='CmdLiftDoHoming',
  full_name='goldo.nucleo.servos.CmdLiftDoHoming',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.servos.CmdLiftDoHoming.sequence_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift_id', full_name='goldo.nucleo.servos.CmdLiftDoHoming.lift_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1039,
)


_CMDLIFTSRAW = _descriptor.Descriptor(
  name='CmdLiftsRaw',
  full_name='goldo.nucleo.servos.CmdLiftsRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.servos.CmdLiftsRaw.sequence_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift1_target', full_name='goldo.nucleo.servos.CmdLiftsRaw.lift1_target', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\006'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift1_bltrig', full_name='goldo.nucleo.servos.CmdLiftsRaw.lift1_bltrig', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift1_speed', full_name='goldo.nucleo.servos.CmdLiftsRaw.lift1_speed', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift2_target', full_name='goldo.nucleo.servos.CmdLiftsRaw.lift2_target', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\006'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift2_bltrig', full_name='goldo.nucleo.servos.CmdLiftsRaw.lift2_bltrig', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift2_speed', full_name='goldo.nucleo.servos.CmdLiftsRaw.lift2_speed', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1042,
  serialized_end=1252,
)


_CMDLIFTSETENABLE = _descriptor.Descriptor(
  name='CmdLiftSetEnable',
  full_name='goldo.nucleo.servos.CmdLiftSetEnable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.servos.CmdLiftSetEnable.sequence_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lift_id', full_name='goldo.nucleo.servos.CmdLiftSetEnable.lift_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='goldo.nucleo.servos.CmdLiftSetEnable.enable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1254,
  serialized_end=1348,
)


_CMDMOVEMULTIPLE = _descriptor.Descriptor(
  name='CmdMoveMultiple',
  full_name='goldo.nucleo.servos.CmdMoveMultiple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.servos.CmdMoveMultiple.sequence_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='goldo.nucleo.servos.CmdMoveMultiple.speed', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positions', full_name='goldo.nucleo.servos.CmdMoveMultiple.positions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1350,
  serialized_end=1474,
)


_CMDSETMAXTORQUES = _descriptor.Descriptor(
  name='CmdSetMaxTorques',
  full_name='goldo.nucleo.servos.CmdSetMaxTorques',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.servos.CmdSetMaxTorques.sequence_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torques', full_name='goldo.nucleo.servos.CmdSetMaxTorques.torques', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1476,
  serialized_end=1576,
)

_SERVOCONFIG.fields_by_name['type'].enum_type = _SERVOTYPE
_SERVOSTATES.fields_by_name['servos'].message_type = _SERVOSTATE
_CMDSETENABLE.fields_by_name['enables'].message_type = _SERVOENABLE
_CMDMOVEMULTIPLE.fields_by_name['positions'].message_type = _SERVOPOSITION
_CMDSETMAXTORQUES.fields_by_name['torques'].message_type = _SERVOTORQUE
DESCRIPTOR.message_types_by_name['ServoConfig'] = _SERVOCONFIG
DESCRIPTOR.message_types_by_name['LiftConfig'] = _LIFTCONFIG
DESCRIPTOR.message_types_by_name['ServoState'] = _SERVOSTATE
DESCRIPTOR.message_types_by_name['ServoStates'] = _SERVOSTATES
DESCRIPTOR.message_types_by_name['ServoPosition'] = _SERVOPOSITION
DESCRIPTOR.message_types_by_name['ServoTorque'] = _SERVOTORQUE
DESCRIPTOR.message_types_by_name['ServoEnable'] = _SERVOENABLE
DESCRIPTOR.message_types_by_name['CmdDisableAll'] = _CMDDISABLEALL
DESCRIPTOR.message_types_by_name['CmdSetEnable'] = _CMDSETENABLE
DESCRIPTOR.message_types_by_name['CmdLiftDoHoming'] = _CMDLIFTDOHOMING
DESCRIPTOR.message_types_by_name['CmdLiftsRaw'] = _CMDLIFTSRAW
DESCRIPTOR.message_types_by_name['CmdLiftSetEnable'] = _CMDLIFTSETENABLE
DESCRIPTOR.message_types_by_name['CmdMoveMultiple'] = _CMDMOVEMULTIPLE
DESCRIPTOR.message_types_by_name['CmdSetMaxTorques'] = _CMDSETMAXTORQUES
DESCRIPTOR.enum_types_by_name['ServoType'] = _SERVOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServoConfig = _reflection.GeneratedProtocolMessageType('ServoConfig', (_message.Message,), dict(
  DESCRIPTOR = _SERVOCONFIG,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoConfig)
  ))
_sym_db.RegisterMessage(ServoConfig)

LiftConfig = _reflection.GeneratedProtocolMessageType('LiftConfig', (_message.Message,), dict(
  DESCRIPTOR = _LIFTCONFIG,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.LiftConfig)
  ))
_sym_db.RegisterMessage(LiftConfig)

ServoState = _reflection.GeneratedProtocolMessageType('ServoState', (_message.Message,), dict(
  DESCRIPTOR = _SERVOSTATE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoState)
  ))
_sym_db.RegisterMessage(ServoState)

ServoStates = _reflection.GeneratedProtocolMessageType('ServoStates', (_message.Message,), dict(
  DESCRIPTOR = _SERVOSTATES,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoStates)
  ))
_sym_db.RegisterMessage(ServoStates)

ServoPosition = _reflection.GeneratedProtocolMessageType('ServoPosition', (_message.Message,), dict(
  DESCRIPTOR = _SERVOPOSITION,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoPosition)
  ))
_sym_db.RegisterMessage(ServoPosition)

ServoTorque = _reflection.GeneratedProtocolMessageType('ServoTorque', (_message.Message,), dict(
  DESCRIPTOR = _SERVOTORQUE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoTorque)
  ))
_sym_db.RegisterMessage(ServoTorque)

ServoEnable = _reflection.GeneratedProtocolMessageType('ServoEnable', (_message.Message,), dict(
  DESCRIPTOR = _SERVOENABLE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoEnable)
  ))
_sym_db.RegisterMessage(ServoEnable)

CmdDisableAll = _reflection.GeneratedProtocolMessageType('CmdDisableAll', (_message.Message,), dict(
  DESCRIPTOR = _CMDDISABLEALL,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdDisableAll)
  ))
_sym_db.RegisterMessage(CmdDisableAll)

CmdSetEnable = _reflection.GeneratedProtocolMessageType('CmdSetEnable', (_message.Message,), dict(
  DESCRIPTOR = _CMDSETENABLE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdSetEnable)
  ))
_sym_db.RegisterMessage(CmdSetEnable)

CmdLiftDoHoming = _reflection.GeneratedProtocolMessageType('CmdLiftDoHoming', (_message.Message,), dict(
  DESCRIPTOR = _CMDLIFTDOHOMING,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdLiftDoHoming)
  ))
_sym_db.RegisterMessage(CmdLiftDoHoming)

CmdLiftsRaw = _reflection.GeneratedProtocolMessageType('CmdLiftsRaw', (_message.Message,), dict(
  DESCRIPTOR = _CMDLIFTSRAW,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdLiftsRaw)
  ))
_sym_db.RegisterMessage(CmdLiftsRaw)

CmdLiftSetEnable = _reflection.GeneratedProtocolMessageType('CmdLiftSetEnable', (_message.Message,), dict(
  DESCRIPTOR = _CMDLIFTSETENABLE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdLiftSetEnable)
  ))
_sym_db.RegisterMessage(CmdLiftSetEnable)

CmdMoveMultiple = _reflection.GeneratedProtocolMessageType('CmdMoveMultiple', (_message.Message,), dict(
  DESCRIPTOR = _CMDMOVEMULTIPLE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdMoveMultiple)
  ))
_sym_db.RegisterMessage(CmdMoveMultiple)

CmdSetMaxTorques = _reflection.GeneratedProtocolMessageType('CmdSetMaxTorques', (_message.Message,), dict(
  DESCRIPTOR = _CMDSETMAXTORQUES,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdSetMaxTorques)
  ))
_sym_db.RegisterMessage(CmdSetMaxTorques)


_SERVOCONFIG.fields_by_name['type']._options = None
_SERVOCONFIG.fields_by_name['id']._options = None
_SERVOCONFIG.fields_by_name['cw_limit']._options = None
_SERVOCONFIG.fields_by_name['ccw_limit']._options = None
_SERVOCONFIG.fields_by_name['max_speed']._options = None
_SERVOCONFIG.fields_by_name['max_torque']._options = None
_SERVOCONFIG.fields_by_name['reserved']._options = None
_SERVOCONFIG.fields_by_name['name']._options = None
_LIFTCONFIG.fields_by_name['kp']._options = None
_LIFTCONFIG.fields_by_name['ki']._options = None
_LIFTCONFIG.fields_by_name['kd']._options = None
_LIFTCONFIG.fields_by_name['range']._options = None
_LIFTCONFIG.fields_by_name['pwm_clamp']._options = None
_LIFTCONFIG.fields_by_name['block_trig']._options = None
_SERVOSTATE.fields_by_name['position']._options = None
_SERVOSTATE.fields_by_name['measured_position']._options = None
_SERVOSTATE.fields_by_name['measured_load']._options = None
_SERVOSTATES.fields_by_name['timestamp']._options = None
_SERVOPOSITION.fields_by_name['servo_id']._options = None
_SERVOPOSITION.fields_by_name['position']._options = None
_SERVOTORQUE.fields_by_name['servo_id']._options = None
_SERVOTORQUE.fields_by_name['torque']._options = None
_SERVOENABLE.fields_by_name['servo_id']._options = None
_SERVOENABLE.fields_by_name['enable']._options = None
_CMDDISABLEALL.fields_by_name['sequence_number']._options = None
_CMDSETENABLE.fields_by_name['sequence_number']._options = None
_CMDLIFTDOHOMING.fields_by_name['sequence_number']._options = None
_CMDLIFTDOHOMING.fields_by_name['lift_id']._options = None
_CMDLIFTSRAW.fields_by_name['sequence_number']._options = None
_CMDLIFTSRAW.fields_by_name['lift1_target']._options = None
_CMDLIFTSRAW.fields_by_name['lift1_bltrig']._options = None
_CMDLIFTSRAW.fields_by_name['lift1_speed']._options = None
_CMDLIFTSRAW.fields_by_name['lift2_target']._options = None
_CMDLIFTSRAW.fields_by_name['lift2_bltrig']._options = None
_CMDLIFTSRAW.fields_by_name['lift2_speed']._options = None
_CMDLIFTSETENABLE.fields_by_name['sequence_number']._options = None
_CMDLIFTSETENABLE.fields_by_name['lift_id']._options = None
_CMDLIFTSETENABLE.fields_by_name['enable']._options = None
_CMDMOVEMULTIPLE.fields_by_name['sequence_number']._options = None
_CMDMOVEMULTIPLE.fields_by_name['speed']._options = None
_CMDSETMAXTORQUES.fields_by_name['sequence_number']._options = None
# @@protoc_insertion_point(module_scope)

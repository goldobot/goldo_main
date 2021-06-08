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
  serialized_pb=_b('\n\x19goldo/nucleo/servos.proto\x12\x13goldo.nucleo.servos\x1a\x17goldo/pb2_options.proto\"\xe3\x01\n\x0bServoConfig\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32\x1e.goldo.nucleo.servos.ServoTypeB\x04\x80\xb5\x18\x03\x12\x10\n\x02id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08\x63w_limit\x18\x03 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tccw_limit\x18\x04 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tmax_speed\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x18\n\nmax_torque\x18\x06 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08reserved\x18\x64 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x12\n\x04name\x18@ \x01(\tB\x04\x80\xb5\x18\x0c\"\x8a\x01\n\nLiftConfig\x12\x10\n\x02kp\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x10\n\x02ki\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x10\n\x02kd\x18\x03 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x13\n\x05range\x18\x04 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tpwm_clamp\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x18\n\nblock_trig\x18\x06 \x01(\x05\x42\x04\x80\xb5\x18\x05\"9\n\tSetEnable\x12\x16\n\x08servo_id\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x14\n\x06\x65nable\x18\x02 \x01(\x08\x42\x04\x80\xb5\x18\x03\"?\n\rServoPosition\x12\x16\n\x08servo_id\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08position\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\"K\n\x04Move\x12\x16\n\x08servo_id\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08position\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\x12\x13\n\x05speed\x18\x03 \x01(\rB\x04\x80\xb5\x18\x05\"G\n\x0f\x43mdLiftDoHoming\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x15\n\x07lift_id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\"^\n\x10\x43mdLiftSetEnable\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x15\n\x07lift_id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x14\n\x06\x65nable\x18\x03 \x01(\x08\x42\x04\x80\xb5\x18\x03\"|\n\x0f\x43mdMoveMultiple\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x13\n\x05speed\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x35\n\tpositions\x18\x03 \x03(\x0b\x32\".goldo.nucleo.servos.ServoPosition*^\n\tServoType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x12\n\x0e\x44YNAMIXEL_AX12\x10\x02\x12\x12\n\x0e\x44YNAMIXEL_MX28\x10\x03\x12\x0e\n\nGOLDO_LIFT\x10\x04\x62\x06proto3')
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
  serialized_start=942,
  serialized_end=1036,
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
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved', full_name='goldo.nucleo.servos.ServoConfig.reserved', index=6,
      number=100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
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
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ki', full_name='goldo.nucleo.servos.LiftConfig.ki', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kd', full_name='goldo.nucleo.servos.LiftConfig.kd', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
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


_SETENABLE = _descriptor.Descriptor(
  name='SetEnable',
  full_name='goldo.nucleo.servos.SetEnable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servo_id', full_name='goldo.nucleo.servos.SetEnable.servo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='goldo.nucleo.servos.SetEnable.enable', index=1,
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
  serialized_start=446,
  serialized_end=503,
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
  serialized_start=505,
  serialized_end=568,
)


_MOVE = _descriptor.Descriptor(
  name='Move',
  full_name='goldo.nucleo.servos.Move',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servo_id', full_name='goldo.nucleo.servos.Move.servo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='goldo.nucleo.servos.Move.position', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='goldo.nucleo.servos.Move.speed', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=570,
  serialized_end=645,
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
  serialized_start=647,
  serialized_end=718,
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
  serialized_start=720,
  serialized_end=814,
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
  serialized_start=816,
  serialized_end=940,
)

_SERVOCONFIG.fields_by_name['type'].enum_type = _SERVOTYPE
_CMDMOVEMULTIPLE.fields_by_name['positions'].message_type = _SERVOPOSITION
DESCRIPTOR.message_types_by_name['ServoConfig'] = _SERVOCONFIG
DESCRIPTOR.message_types_by_name['LiftConfig'] = _LIFTCONFIG
DESCRIPTOR.message_types_by_name['SetEnable'] = _SETENABLE
DESCRIPTOR.message_types_by_name['ServoPosition'] = _SERVOPOSITION
DESCRIPTOR.message_types_by_name['Move'] = _MOVE
DESCRIPTOR.message_types_by_name['CmdLiftDoHoming'] = _CMDLIFTDOHOMING
DESCRIPTOR.message_types_by_name['CmdLiftSetEnable'] = _CMDLIFTSETENABLE
DESCRIPTOR.message_types_by_name['CmdMoveMultiple'] = _CMDMOVEMULTIPLE
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

SetEnable = _reflection.GeneratedProtocolMessageType('SetEnable', (_message.Message,), dict(
  DESCRIPTOR = _SETENABLE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.SetEnable)
  ))
_sym_db.RegisterMessage(SetEnable)

ServoPosition = _reflection.GeneratedProtocolMessageType('ServoPosition', (_message.Message,), dict(
  DESCRIPTOR = _SERVOPOSITION,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoPosition)
  ))
_sym_db.RegisterMessage(ServoPosition)

Move = _reflection.GeneratedProtocolMessageType('Move', (_message.Message,), dict(
  DESCRIPTOR = _MOVE,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.Move)
  ))
_sym_db.RegisterMessage(Move)

CmdLiftDoHoming = _reflection.GeneratedProtocolMessageType('CmdLiftDoHoming', (_message.Message,), dict(
  DESCRIPTOR = _CMDLIFTDOHOMING,
  __module__ = 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.CmdLiftDoHoming)
  ))
_sym_db.RegisterMessage(CmdLiftDoHoming)

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
_SETENABLE.fields_by_name['servo_id']._options = None
_SETENABLE.fields_by_name['enable']._options = None
_SERVOPOSITION.fields_by_name['servo_id']._options = None
_SERVOPOSITION.fields_by_name['position']._options = None
_MOVE.fields_by_name['servo_id']._options = None
_MOVE.fields_by_name['position']._options = None
_MOVE.fields_by_name['speed']._options = None
_CMDLIFTDOHOMING.fields_by_name['sequence_number']._options = None
_CMDLIFTDOHOMING.fields_by_name['lift_id']._options = None
_CMDLIFTSETENABLE.fields_by_name['sequence_number']._options = None
_CMDLIFTSETENABLE.fields_by_name['lift_id']._options = None
_CMDLIFTSETENABLE.fields_by_name['enable']._options = None
_CMDMOVEMULTIPLE.fields_by_name['sequence_number']._options = None
_CMDMOVEMULTIPLE.fields_by_name['speed']._options = None
# @@protoc_insertion_point(module_scope)

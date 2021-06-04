# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo/fpga.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo import pb2_options_pb2 as goldo_dot_pb2__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/nucleo/fpga.proto',
  package='goldo.nucleo.fpga',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17goldo/nucleo/fpga.proto\x12\x11goldo.nucleo.fpga\x1a\x17goldo/pb2_options.proto\"$\n\x07RegRead\x12\x19\n\x0b\x61pb_address\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\"C\n\rRegReadStatus\x12\x19\n\x0b\x61pb_address\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\x12\x17\n\tapb_value\x18\x02 \x01(\x07\x42\x04\x80\xb5\x18\x07\">\n\x08RegWrite\x12\x19\n\x0b\x61pb_address\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\x12\x17\n\tapb_value\x18\x02 \x01(\x07\x42\x04\x80\xb5\x18\x07\x62\x06proto3')
  ,
  dependencies=[goldo_dot_pb2__options__pb2.DESCRIPTOR,])




_REGREAD = _descriptor.Descriptor(
  name='RegRead',
  full_name='goldo.nucleo.fpga.RegRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apb_address', full_name='goldo.nucleo.fpga.RegRead.apb_address', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
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
  serialized_start=71,
  serialized_end=107,
)


_REGREADSTATUS = _descriptor.Descriptor(
  name='RegReadStatus',
  full_name='goldo.nucleo.fpga.RegReadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apb_address', full_name='goldo.nucleo.fpga.RegReadStatus.apb_address', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apb_value', full_name='goldo.nucleo.fpga.RegReadStatus.apb_value', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
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
  serialized_start=109,
  serialized_end=176,
)


_REGWRITE = _descriptor.Descriptor(
  name='RegWrite',
  full_name='goldo.nucleo.fpga.RegWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apb_address', full_name='goldo.nucleo.fpga.RegWrite.apb_address', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apb_value', full_name='goldo.nucleo.fpga.RegWrite.apb_value', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
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
  serialized_start=178,
  serialized_end=240,
)

DESCRIPTOR.message_types_by_name['RegRead'] = _REGREAD
DESCRIPTOR.message_types_by_name['RegReadStatus'] = _REGREADSTATUS
DESCRIPTOR.message_types_by_name['RegWrite'] = _REGWRITE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegRead = _reflection.GeneratedProtocolMessageType('RegRead', (_message.Message,), dict(
  DESCRIPTOR = _REGREAD,
  __module__ = 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.RegRead)
  ))
_sym_db.RegisterMessage(RegRead)

RegReadStatus = _reflection.GeneratedProtocolMessageType('RegReadStatus', (_message.Message,), dict(
  DESCRIPTOR = _REGREADSTATUS,
  __module__ = 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.RegReadStatus)
  ))
_sym_db.RegisterMessage(RegReadStatus)

RegWrite = _reflection.GeneratedProtocolMessageType('RegWrite', (_message.Message,), dict(
  DESCRIPTOR = _REGWRITE,
  __module__ = 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.RegWrite)
  ))
_sym_db.RegisterMessage(RegWrite)


_REGREAD.fields_by_name['apb_address']._options = None
_REGREADSTATUS.fields_by_name['apb_address']._options = None
_REGREADSTATUS.fields_by_name['apb_value']._options = None
_REGWRITE.fields_by_name['apb_address']._options = None
_REGWRITE.fields_by_name['apb_value']._options = None
# @@protoc_insertion_point(module_scope)

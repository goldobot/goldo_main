# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/log.proto',
  package='goldo.log',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fgoldo/log.proto\x12\tgoldo.log\"l\n\nLogMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08pathname\x18\x03 \x01(\t\x12\x0e\n\x06lineno\x18\x04 \x01(\x05\x12\x0f\n\x07levelno\x18\x05 \x01(\x05\x12\x0c\n\x04\x66unc\x18\x06 \x01(\tb\x06proto3')
)




_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='goldo.log.LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='goldo.log.LogMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='goldo.log.LogMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathname', full_name='goldo.log.LogMessage.pathname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lineno', full_name='goldo.log.LogMessage.lineno', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='levelno', full_name='goldo.log.LogMessage.levelno', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='func', full_name='goldo.log.LogMessage.func', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=30,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), dict(
  DESCRIPTOR = _LOGMESSAGE,
  __module__ = 'goldo.log_pb2'
  # @@protoc_insertion_point(class_scope:goldo.log.LogMessage)
  ))
_sym_db.RegisterMessage(LogMessage)


# @@protoc_insertion_point(module_scope)

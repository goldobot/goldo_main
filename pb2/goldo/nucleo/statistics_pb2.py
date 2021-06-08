# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo/statistics.proto

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
  name='goldo/nucleo/statistics.proto',
  package='goldo.nucleo.statistics',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dgoldo/nucleo/statistics.proto\x12\x17goldo.nucleo.statistics\x1a\x17goldo/pb2_options.proto\"y\n\x16MessageQueueStatistics\x12$\n\x16min_available_capacity\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12\x1a\n\x0c\x62ytes_pushed\x18\x02 \x01(\rB\x04\x80\xb5\x18\x07\x12\x1d\n\x0fmessages_pushed\x18\x03 \x01(\rB\x04\x80\xb5\x18\x07\"v\n\x18\x43ommSerializerStatistics\x12\x1b\n\rmessages_sent\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12\x18\n\nbytes_sent\x18\x02 \x01(\rB\x04\x80\xb5\x18\x07\x12#\n\x15\x62uffer_high_watermark\x18\x03 \x01(\rB\x04\x80\xb5\x18\x07\"\xb9\x01\n\x1a\x43ommDeserializerStatistics\x12\x1f\n\x11messages_received\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12\x1c\n\x0e\x62ytes_received\x18\x02 \x01(\rB\x04\x80\xb5\x18\x07\x12\x1d\n\x0fsequence_errors\x18\x03 \x01(\rB\x04\x80\xb5\x18\x07\x12\x18\n\ncrc_errors\x18\x04 \x01(\rB\x04\x80\xb5\x18\x07\x12#\n\x15\x62uffer_high_watermark\x18\x05 \x01(\rB\x04\x80\xb5\x18\x07\"v\n\x1cODriveStreamParserStatistics\x12\x1c\n\x0e\x62ytes_received\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12\x1f\n\x11messages_received\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\x12\x17\n\trx_errors\x18\x03 \x01(\rB\x04\x80\xb5\x18\x05\"q\n\x1cODriveStreamWriterStatistics\x12\x18\n\nbytes_sent\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12\x1b\n\rmessages_sent\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\x12\x1a\n\x0ctx_highwater\x18\x03 \x01(\rB\x04\x80\xb5\x18\x05\"\xb6\x04\n\x16UARTCommTaskStatistics\x12\x18\n\nmax_cycles\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12\x45\n\nserializer\x18\x02 \x01(\x0b\x32\x31.goldo.nucleo.statistics.CommSerializerStatistics\x12I\n\x0c\x64\x65serializer\x18\x03 \x01(\x0b\x32\x33.goldo.nucleo.statistics.CommDeserializerStatistics\x12J\n\x0fserializer_ftdi\x18\x04 \x01(\x0b\x32\x31.goldo.nucleo.statistics.CommSerializerStatistics\x12N\n\x11\x64\x65serializer_fdti\x18\x05 \x01(\x0b\x32\x33.goldo.nucleo.statistics.CommDeserializerStatistics\x12\x42\n\tqueue_out\x18\x06 \x01(\x0b\x32/.goldo.nucleo.statistics.MessageQueueStatistics\x12G\n\x0equeue_out_prio\x18\x07 \x01(\x0b\x32/.goldo.nucleo.statistics.MessageQueueStatistics\x12G\n\x0equeue_out_ftdi\x18\x08 \x01(\x0b\x32/.goldo.nucleo.statistics.MessageQueueStatistics\"\xe8\x01\n\x18ODriveCommTaskStatistics\x12\x45\n\x06parser\x18\x02 \x01(\x0b\x32\x35.goldo.nucleo.statistics.ODriveStreamParserStatistics\x12\x45\n\x06writer\x18\x03 \x01(\x0b\x32\x35.goldo.nucleo.statistics.ODriveStreamWriterStatistics\x12>\n\x05queue\x18\x04 \x01(\x0b\x32/.goldo.nucleo.statistics.MessageQueueStatistics\"\x82\x02\n\x18PropulsionTaskStatistics\x12\x18\n\nmax_cycles\x18\x01 \x01(\rB\x04\x80\xb5\x18\x07\x12>\n\x05queue\x18\x02 \x01(\x0b\x32/.goldo.nucleo.statistics.MessageQueueStatistics\x12\x45\n\x0curgent_queue\x18\x03 \x01(\x0b\x32/.goldo.nucleo.statistics.MessageQueueStatistics\x12\x45\n\x0codrive_queue\x18\x04 \x01(\x0b\x32/.goldo.nucleo.statistics.MessageQueueStatisticsb\x06proto3')
  ,
  dependencies=[goldo_dot_pb2__options__pb2.DESCRIPTOR,])




_MESSAGEQUEUESTATISTICS = _descriptor.Descriptor(
  name='MessageQueueStatistics',
  full_name='goldo.nucleo.statistics.MessageQueueStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_available_capacity', full_name='goldo.nucleo.statistics.MessageQueueStatistics.min_available_capacity', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_pushed', full_name='goldo.nucleo.statistics.MessageQueueStatistics.bytes_pushed', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages_pushed', full_name='goldo.nucleo.statistics.MessageQueueStatistics.messages_pushed', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=83,
  serialized_end=204,
)


_COMMSERIALIZERSTATISTICS = _descriptor.Descriptor(
  name='CommSerializerStatistics',
  full_name='goldo.nucleo.statistics.CommSerializerStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages_sent', full_name='goldo.nucleo.statistics.CommSerializerStatistics.messages_sent', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_sent', full_name='goldo.nucleo.statistics.CommSerializerStatistics.bytes_sent', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buffer_high_watermark', full_name='goldo.nucleo.statistics.CommSerializerStatistics.buffer_high_watermark', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=206,
  serialized_end=324,
)


_COMMDESERIALIZERSTATISTICS = _descriptor.Descriptor(
  name='CommDeserializerStatistics',
  full_name='goldo.nucleo.statistics.CommDeserializerStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages_received', full_name='goldo.nucleo.statistics.CommDeserializerStatistics.messages_received', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_received', full_name='goldo.nucleo.statistics.CommDeserializerStatistics.bytes_received', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_errors', full_name='goldo.nucleo.statistics.CommDeserializerStatistics.sequence_errors', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crc_errors', full_name='goldo.nucleo.statistics.CommDeserializerStatistics.crc_errors', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buffer_high_watermark', full_name='goldo.nucleo.statistics.CommDeserializerStatistics.buffer_high_watermark', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=327,
  serialized_end=512,
)


_ODRIVESTREAMPARSERSTATISTICS = _descriptor.Descriptor(
  name='ODriveStreamParserStatistics',
  full_name='goldo.nucleo.statistics.ODriveStreamParserStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes_received', full_name='goldo.nucleo.statistics.ODriveStreamParserStatistics.bytes_received', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages_received', full_name='goldo.nucleo.statistics.ODriveStreamParserStatistics.messages_received', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx_errors', full_name='goldo.nucleo.statistics.ODriveStreamParserStatistics.rx_errors', index=2,
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
  serialized_start=514,
  serialized_end=632,
)


_ODRIVESTREAMWRITERSTATISTICS = _descriptor.Descriptor(
  name='ODriveStreamWriterStatistics',
  full_name='goldo.nucleo.statistics.ODriveStreamWriterStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes_sent', full_name='goldo.nucleo.statistics.ODriveStreamWriterStatistics.bytes_sent', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages_sent', full_name='goldo.nucleo.statistics.ODriveStreamWriterStatistics.messages_sent', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_highwater', full_name='goldo.nucleo.statistics.ODriveStreamWriterStatistics.tx_highwater', index=2,
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
  serialized_start=634,
  serialized_end=747,
)


_UARTCOMMTASKSTATISTICS = _descriptor.Descriptor(
  name='UARTCommTaskStatistics',
  full_name='goldo.nucleo.statistics.UARTCommTaskStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_cycles', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.max_cycles', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serializer', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.serializer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deserializer', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.deserializer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serializer_ftdi', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.serializer_ftdi', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deserializer_fdti', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.deserializer_fdti', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue_out', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.queue_out', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue_out_prio', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.queue_out_prio', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue_out_ftdi', full_name='goldo.nucleo.statistics.UARTCommTaskStatistics.queue_out_ftdi', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=750,
  serialized_end=1316,
)


_ODRIVECOMMTASKSTATISTICS = _descriptor.Descriptor(
  name='ODriveCommTaskStatistics',
  full_name='goldo.nucleo.statistics.ODriveCommTaskStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parser', full_name='goldo.nucleo.statistics.ODriveCommTaskStatistics.parser', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writer', full_name='goldo.nucleo.statistics.ODriveCommTaskStatistics.writer', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue', full_name='goldo.nucleo.statistics.ODriveCommTaskStatistics.queue', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1319,
  serialized_end=1551,
)


_PROPULSIONTASKSTATISTICS = _descriptor.Descriptor(
  name='PropulsionTaskStatistics',
  full_name='goldo.nucleo.statistics.PropulsionTaskStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_cycles', full_name='goldo.nucleo.statistics.PropulsionTaskStatistics.max_cycles', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\007'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue', full_name='goldo.nucleo.statistics.PropulsionTaskStatistics.queue', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urgent_queue', full_name='goldo.nucleo.statistics.PropulsionTaskStatistics.urgent_queue', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='odrive_queue', full_name='goldo.nucleo.statistics.PropulsionTaskStatistics.odrive_queue', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1554,
  serialized_end=1812,
)

_UARTCOMMTASKSTATISTICS.fields_by_name['serializer'].message_type = _COMMSERIALIZERSTATISTICS
_UARTCOMMTASKSTATISTICS.fields_by_name['deserializer'].message_type = _COMMDESERIALIZERSTATISTICS
_UARTCOMMTASKSTATISTICS.fields_by_name['serializer_ftdi'].message_type = _COMMSERIALIZERSTATISTICS
_UARTCOMMTASKSTATISTICS.fields_by_name['deserializer_fdti'].message_type = _COMMDESERIALIZERSTATISTICS
_UARTCOMMTASKSTATISTICS.fields_by_name['queue_out'].message_type = _MESSAGEQUEUESTATISTICS
_UARTCOMMTASKSTATISTICS.fields_by_name['queue_out_prio'].message_type = _MESSAGEQUEUESTATISTICS
_UARTCOMMTASKSTATISTICS.fields_by_name['queue_out_ftdi'].message_type = _MESSAGEQUEUESTATISTICS
_ODRIVECOMMTASKSTATISTICS.fields_by_name['parser'].message_type = _ODRIVESTREAMPARSERSTATISTICS
_ODRIVECOMMTASKSTATISTICS.fields_by_name['writer'].message_type = _ODRIVESTREAMWRITERSTATISTICS
_ODRIVECOMMTASKSTATISTICS.fields_by_name['queue'].message_type = _MESSAGEQUEUESTATISTICS
_PROPULSIONTASKSTATISTICS.fields_by_name['queue'].message_type = _MESSAGEQUEUESTATISTICS
_PROPULSIONTASKSTATISTICS.fields_by_name['urgent_queue'].message_type = _MESSAGEQUEUESTATISTICS
_PROPULSIONTASKSTATISTICS.fields_by_name['odrive_queue'].message_type = _MESSAGEQUEUESTATISTICS
DESCRIPTOR.message_types_by_name['MessageQueueStatistics'] = _MESSAGEQUEUESTATISTICS
DESCRIPTOR.message_types_by_name['CommSerializerStatistics'] = _COMMSERIALIZERSTATISTICS
DESCRIPTOR.message_types_by_name['CommDeserializerStatistics'] = _COMMDESERIALIZERSTATISTICS
DESCRIPTOR.message_types_by_name['ODriveStreamParserStatistics'] = _ODRIVESTREAMPARSERSTATISTICS
DESCRIPTOR.message_types_by_name['ODriveStreamWriterStatistics'] = _ODRIVESTREAMWRITERSTATISTICS
DESCRIPTOR.message_types_by_name['UARTCommTaskStatistics'] = _UARTCOMMTASKSTATISTICS
DESCRIPTOR.message_types_by_name['ODriveCommTaskStatistics'] = _ODRIVECOMMTASKSTATISTICS
DESCRIPTOR.message_types_by_name['PropulsionTaskStatistics'] = _PROPULSIONTASKSTATISTICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageQueueStatistics = _reflection.GeneratedProtocolMessageType('MessageQueueStatistics', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEQUEUESTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.MessageQueueStatistics)
  ))
_sym_db.RegisterMessage(MessageQueueStatistics)

CommSerializerStatistics = _reflection.GeneratedProtocolMessageType('CommSerializerStatistics', (_message.Message,), dict(
  DESCRIPTOR = _COMMSERIALIZERSTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.CommSerializerStatistics)
  ))
_sym_db.RegisterMessage(CommSerializerStatistics)

CommDeserializerStatistics = _reflection.GeneratedProtocolMessageType('CommDeserializerStatistics', (_message.Message,), dict(
  DESCRIPTOR = _COMMDESERIALIZERSTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.CommDeserializerStatistics)
  ))
_sym_db.RegisterMessage(CommDeserializerStatistics)

ODriveStreamParserStatistics = _reflection.GeneratedProtocolMessageType('ODriveStreamParserStatistics', (_message.Message,), dict(
  DESCRIPTOR = _ODRIVESTREAMPARSERSTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.ODriveStreamParserStatistics)
  ))
_sym_db.RegisterMessage(ODriveStreamParserStatistics)

ODriveStreamWriterStatistics = _reflection.GeneratedProtocolMessageType('ODriveStreamWriterStatistics', (_message.Message,), dict(
  DESCRIPTOR = _ODRIVESTREAMWRITERSTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.ODriveStreamWriterStatistics)
  ))
_sym_db.RegisterMessage(ODriveStreamWriterStatistics)

UARTCommTaskStatistics = _reflection.GeneratedProtocolMessageType('UARTCommTaskStatistics', (_message.Message,), dict(
  DESCRIPTOR = _UARTCOMMTASKSTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.UARTCommTaskStatistics)
  ))
_sym_db.RegisterMessage(UARTCommTaskStatistics)

ODriveCommTaskStatistics = _reflection.GeneratedProtocolMessageType('ODriveCommTaskStatistics', (_message.Message,), dict(
  DESCRIPTOR = _ODRIVECOMMTASKSTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.ODriveCommTaskStatistics)
  ))
_sym_db.RegisterMessage(ODriveCommTaskStatistics)

PropulsionTaskStatistics = _reflection.GeneratedProtocolMessageType('PropulsionTaskStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PROPULSIONTASKSTATISTICS,
  __module__ = 'goldo.nucleo.statistics_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.statistics.PropulsionTaskStatistics)
  ))
_sym_db.RegisterMessage(PropulsionTaskStatistics)


_MESSAGEQUEUESTATISTICS.fields_by_name['min_available_capacity']._options = None
_MESSAGEQUEUESTATISTICS.fields_by_name['bytes_pushed']._options = None
_MESSAGEQUEUESTATISTICS.fields_by_name['messages_pushed']._options = None
_COMMSERIALIZERSTATISTICS.fields_by_name['messages_sent']._options = None
_COMMSERIALIZERSTATISTICS.fields_by_name['bytes_sent']._options = None
_COMMSERIALIZERSTATISTICS.fields_by_name['buffer_high_watermark']._options = None
_COMMDESERIALIZERSTATISTICS.fields_by_name['messages_received']._options = None
_COMMDESERIALIZERSTATISTICS.fields_by_name['bytes_received']._options = None
_COMMDESERIALIZERSTATISTICS.fields_by_name['sequence_errors']._options = None
_COMMDESERIALIZERSTATISTICS.fields_by_name['crc_errors']._options = None
_COMMDESERIALIZERSTATISTICS.fields_by_name['buffer_high_watermark']._options = None
_ODRIVESTREAMPARSERSTATISTICS.fields_by_name['bytes_received']._options = None
_ODRIVESTREAMPARSERSTATISTICS.fields_by_name['messages_received']._options = None
_ODRIVESTREAMPARSERSTATISTICS.fields_by_name['rx_errors']._options = None
_ODRIVESTREAMWRITERSTATISTICS.fields_by_name['bytes_sent']._options = None
_ODRIVESTREAMWRITERSTATISTICS.fields_by_name['messages_sent']._options = None
_ODRIVESTREAMWRITERSTATISTICS.fields_by_name['tx_highwater']._options = None
_UARTCOMMTASKSTATISTICS.fields_by_name['max_cycles']._options = None
_PROPULSIONTASKSTATISTICS.fields_by_name['max_cycles']._options = None
# @@protoc_insertion_point(module_scope)

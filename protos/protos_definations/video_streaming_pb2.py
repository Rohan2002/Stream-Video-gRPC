# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video-streaming.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='video-streaming.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15video-streaming.proto\x12\x06protos\",\n\rVideoMetaData\x12\x1b\n\x05value\x18\x01 \x01(\x0b\x32\x0c.protos.UUID\"\x15\n\x04UUID\x12\r\n\x05value\x18\x01 \x01(\t\">\n\x0bVideoFrames\x12\x10\n\x08\x62\x36\x34image\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x32\x92\x01\n\rVideoStreamer\x12@\n\x0egetVideoStream\x12\x15.protos.VideoMetaData\x1a\x13.protos.VideoFrames\"\x00\x30\x01\x12?\n\x0fsendVideoStream\x12\x13.protos.VideoFrames\x1a\x13.protos.VideoFrames\"\x00(\x01\x62\x06proto3'
)




_VIDEOMETADATA = _descriptor.Descriptor(
  name='VideoMetaData',
  full_name='protos.VideoMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.VideoMetaData.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=33,
  serialized_end=77,
)


_UUID = _descriptor.Descriptor(
  name='UUID',
  full_name='protos.UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.UUID.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=79,
  serialized_end=100,
)


_VIDEOFRAMES = _descriptor.Descriptor(
  name='VideoFrames',
  full_name='protos.VideoFrames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='b64image', full_name='protos.VideoFrames.b64image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='protos.VideoFrames.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='protos.VideoFrames.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=102,
  serialized_end=164,
)

_VIDEOMETADATA.fields_by_name['value'].message_type = _UUID
DESCRIPTOR.message_types_by_name['VideoMetaData'] = _VIDEOMETADATA
DESCRIPTOR.message_types_by_name['UUID'] = _UUID
DESCRIPTOR.message_types_by_name['VideoFrames'] = _VIDEOFRAMES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoMetaData = _reflection.GeneratedProtocolMessageType('VideoMetaData', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOMETADATA,
  '__module__' : 'video_streaming_pb2'
  # @@protoc_insertion_point(class_scope:protos.VideoMetaData)
  })
_sym_db.RegisterMessage(VideoMetaData)

UUID = _reflection.GeneratedProtocolMessageType('UUID', (_message.Message,), {
  'DESCRIPTOR' : _UUID,
  '__module__' : 'video_streaming_pb2'
  # @@protoc_insertion_point(class_scope:protos.UUID)
  })
_sym_db.RegisterMessage(UUID)

VideoFrames = _reflection.GeneratedProtocolMessageType('VideoFrames', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOFRAMES,
  '__module__' : 'video_streaming_pb2'
  # @@protoc_insertion_point(class_scope:protos.VideoFrames)
  })
_sym_db.RegisterMessage(VideoFrames)



_VIDEOSTREAMER = _descriptor.ServiceDescriptor(
  name='VideoStreamer',
  full_name='protos.VideoStreamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=167,
  serialized_end=313,
  methods=[
  _descriptor.MethodDescriptor(
    name='getVideoStream',
    full_name='protos.VideoStreamer.getVideoStream',
    index=0,
    containing_service=None,
    input_type=_VIDEOMETADATA,
    output_type=_VIDEOFRAMES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendVideoStream',
    full_name='protos.VideoStreamer.sendVideoStream',
    index=1,
    containing_service=None,
    input_type=_VIDEOFRAMES,
    output_type=_VIDEOFRAMES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VIDEOSTREAMER)

DESCRIPTOR.services_by_name['VideoStreamer'] = _VIDEOSTREAMER

# @@protoc_insertion_point(module_scope)

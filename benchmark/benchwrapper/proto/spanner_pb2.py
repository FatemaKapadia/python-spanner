# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: benchmark/benchwrapper/proto/spanner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*benchmark/benchwrapper/proto/spanner.proto\x12\rspanner_bench\"P\n\x06Singer\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x13\n\x0bsinger_info\x18\x04 \x01(\t\";\n\x05\x41lbum\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tsinger_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x61lbum_title\x18\x03 \x01(\t\"\x1a\n\tReadQuery\x12\r\n\x05query\x18\x01 \x01(\t\"[\n\x0bInsertQuery\x12&\n\x07singers\x18\x01 \x03(\x0b\x32\x15.spanner_bench.Singer\x12$\n\x06\x61lbums\x18\x02 \x03(\x0b\x32\x14.spanner_bench.Album\"\x1e\n\x0bUpdateQuery\x12\x0f\n\x07queries\x18\x01 \x03(\t\"\x0f\n\rEmptyResponse2\xe3\x01\n\x13SpannerBenchWrapper\x12@\n\x04Read\x12\x18.spanner_bench.ReadQuery\x1a\x1c.spanner_bench.EmptyResponse\"\x00\x12\x44\n\x06Insert\x12\x1a.spanner_bench.InsertQuery\x1a\x1c.spanner_bench.EmptyResponse\"\x00\x12\x44\n\x06Update\x12\x1a.spanner_bench.UpdateQuery\x1a\x1c.spanner_bench.EmptyResponse\"\x00\x42\x03\x90\x01\x01\x62\x06proto3')



_SINGER = DESCRIPTOR.message_types_by_name['Singer']
_ALBUM = DESCRIPTOR.message_types_by_name['Album']
_READQUERY = DESCRIPTOR.message_types_by_name['ReadQuery']
_INSERTQUERY = DESCRIPTOR.message_types_by_name['InsertQuery']
_UPDATEQUERY = DESCRIPTOR.message_types_by_name['UpdateQuery']
_EMPTYRESPONSE = DESCRIPTOR.message_types_by_name['EmptyResponse']
Singer = _reflection.GeneratedProtocolMessageType('Singer', (_message.Message,), {
  'DESCRIPTOR' : _SINGER,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.Singer)
  })
_sym_db.RegisterMessage(Singer)

Album = _reflection.GeneratedProtocolMessageType('Album', (_message.Message,), {
  'DESCRIPTOR' : _ALBUM,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.Album)
  })
_sym_db.RegisterMessage(Album)

ReadQuery = _reflection.GeneratedProtocolMessageType('ReadQuery', (_message.Message,), {
  'DESCRIPTOR' : _READQUERY,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.ReadQuery)
  })
_sym_db.RegisterMessage(ReadQuery)

InsertQuery = _reflection.GeneratedProtocolMessageType('InsertQuery', (_message.Message,), {
  'DESCRIPTOR' : _INSERTQUERY,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.InsertQuery)
  })
_sym_db.RegisterMessage(InsertQuery)

UpdateQuery = _reflection.GeneratedProtocolMessageType('UpdateQuery', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQUERY,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.UpdateQuery)
  })
_sym_db.RegisterMessage(UpdateQuery)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)

_SPANNERBENCHWRAPPER = DESCRIPTOR.services_by_name['SpannerBenchWrapper']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\220\001\001'
  _SINGER._serialized_start=61
  _SINGER._serialized_end=141
  _ALBUM._serialized_start=143
  _ALBUM._serialized_end=202
  _READQUERY._serialized_start=204
  _READQUERY._serialized_end=230
  _INSERTQUERY._serialized_start=232
  _INSERTQUERY._serialized_end=323
  _UPDATEQUERY._serialized_start=325
  _UPDATEQUERY._serialized_end=355
  _EMPTYRESPONSE._serialized_start=357
  _EMPTYRESPONSE._serialized_end=372
  _SPANNERBENCHWRAPPER._serialized_start=375
  _SPANNERBENCHWRAPPER._serialized_end=602
SpannerBenchWrapper = service_reflection.GeneratedServiceType('SpannerBenchWrapper', (_service.Service,), dict(
  DESCRIPTOR = _SPANNERBENCHWRAPPER,
  __module__ = 'benchmark.benchwrapper.proto.spanner_pb2'
  ))

SpannerBenchWrapper_Stub = service_reflection.GeneratedServiceStubType('SpannerBenchWrapper_Stub', (SpannerBenchWrapper,), dict(
  DESCRIPTOR = _SPANNERBENCHWRAPPER,
  __module__ = 'benchmark.benchwrapper.proto.spanner_pb2'
  ))


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ingestion/v1alpha/ingestion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from alignai.ingestion.v1alpha import event_pb2 as ingestion_dot_v1alpha_dot_event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ingestion/v1alpha/ingestion.proto\x12\x11ingestion.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1dingestion/v1alpha/event.proto\"s\n\x14\x43ollectEventsRequest\x12#\n\nrequest_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\trequestId\x12\x36\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x18.ingestion.v1alpha.EventB\x04\xe2\x41\x01\x02R\x06\x65vents2f\n\x10IngestionService\x12R\n\rCollectEvents\x12\'.ingestion.v1alpha.CollectEventsRequest\x1a\x16.google.protobuf.Empty\"\x00\x42\xdb\x01\n\x15\x63om.ingestion.v1alphaB\x0eIngestionProtoP\x01ZMgithub.com/coxwave/impaction-ai-api/gen/go/ingestion/v1alpha;ingestionv1alpha\xa2\x02\x03IXX\xaa\x02\x11Ingestion.V1alpha\xca\x02\x11Ingestion\\V1alpha\xe2\x02\x1dIngestion\\V1alpha\\GPBMetadata\xea\x02\x12Ingestion::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ingestion.v1alpha.ingestion_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.ingestion.v1alphaB\016IngestionProtoP\001ZMgithub.com/coxwave/impaction-ai-api/gen/go/ingestion/v1alpha;ingestionv1alpha\242\002\003IXX\252\002\021Ingestion.V1alpha\312\002\021Ingestion\\V1alpha\342\002\035Ingestion\\V1alpha\\GPBMetadata\352\002\022Ingestion::V1alpha'
  _COLLECTEVENTSREQUEST.fields_by_name['request_id']._options = None
  _COLLECTEVENTSREQUEST.fields_by_name['request_id']._serialized_options = b'\342A\001\002'
  _COLLECTEVENTSREQUEST.fields_by_name['events']._options = None
  _COLLECTEVENTSREQUEST.fields_by_name['events']._serialized_options = b'\342A\001\002'
  _globals['_COLLECTEVENTSREQUEST']._serialized_start=149
  _globals['_COLLECTEVENTSREQUEST']._serialized_end=264
  _globals['_INGESTIONSERVICE']._serialized_start=266
  _globals['_INGESTIONSERVICE']._serialized_end=368
# @@protoc_insertion_point(module_scope)

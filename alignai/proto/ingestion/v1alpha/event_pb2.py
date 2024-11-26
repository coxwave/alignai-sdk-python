# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ingestion/v1alpha/event.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dingestion/v1alpha/event.proto\x12\x11ingestion.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe4\x01\n\x05\x45vent\x12\x13\n\x02id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x02id\x12\x17\n\x04type\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x04type\x12@\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01R\ncreateTime\x12G\n\nproperties\x18\x04 \x01(\x0b\x32\".ingestion.v1alpha.EventPropertiesB\x03\xe0\x41\x02R\nproperties\x12\"\n\nproject_id\x18\x05 \x01(\tB\x03\xe0\x41\x02R\tprojectId\"\x9e\x11\n\x0f\x45ventProperties\x12\x65\n\x12session_properties\x18\x01 \x01(\x0b\x32\x34.ingestion.v1alpha.EventProperties.SessionPropertiesH\x00R\x11sessionProperties\x12\x65\n\x12message_properties\x18\x02 \x01(\x0b\x32\x34.ingestion.v1alpha.EventProperties.MessagePropertiesH\x00R\x11messageProperties\x12\\\n\x0fuser_properties\x18\x03 \x01(\x0b\x32\x31.ingestion.v1alpha.EventProperties.UserPropertiesH\x00R\x0euserProperties\x12h\n\x13\x66\x65\x65\x64\x62\x61\x63k_properties\x18\x04 \x01(\x0b\x32\x35.ingestion.v1alpha.EventProperties.FeedbackPropertiesH\x00R\x12\x66\x65\x65\x64\x62\x61\x63kProperties\x12j\n\x11\x63ustom_properties\x18\n \x03(\x0b\x32\x38.ingestion.v1alpha.EventProperties.CustomPropertiesEntryB\x03\xe0\x41\x01R\x10\x63ustomProperties\x1a\xf6\x01\n\x11SessionProperties\x12\"\n\nsession_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\tsessionId\x12(\n\rsession_title\x18\x02 \x01(\tB\x03\xe0\x41\x01R\x0csessionTitle\x12M\n\x12session_start_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01R\x10sessionStartTime\x12\x1c\n\x07user_id\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x06userId\x12&\n\x0c\x61ssistant_id\x18\x05 \x01(\tB\x03\xe0\x41\x01R\x0b\x61ssistantId\x1a\xbc\x03\n\x11MessageProperties\x12\"\n\nsession_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\tsessionId\x12-\n\x0fmessage_id_hint\x18\x02 \x01(\tB\x05\x18\x01\xe0\x41\x01R\rmessageIdHint\x12\x31\n\x12message_index_hint\x18\x03 \x01(\x05\x42\x03\xe0\x41\x02R\x10messageIndexHint\x12\x61\n\x0cmessage_role\x18\x04 \x01(\x0e\x32\x39.ingestion.v1alpha.EventProperties.MessageProperties.RoleB\x03\xe0\x41\x02R\x0bmessageRole\x12,\n\x0fmessage_content\x18\x05 \x01(\tB\x03\xe0\x41\x02R\x0emessageContent\x12O\n\x13message_create_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01R\x11messageCreateTime\"?\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\r\n\tROLE_USER\x10\x01\x12\x12\n\x0eROLE_ASSISTANT\x10\x02\x1a\xba\x03\n\x0eUserProperties\x12\x1c\n\x07user_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x06userId\x12\"\n\nuser_email\x18\x02 \x01(\tB\x03\xe0\x41\x01R\tuserEmail\x12\x1c\n\x07user_ip\x18\x03 \x01(\tB\x03\xe0\x41\x01R\x06userIp\x12\x64\n\ruser_location\x18\x04 \x01(\x0b\x32:.ingestion.v1alpha.EventProperties.UserProperties.LocationB\x03\xe0\x41\x01R\x0cuserLocation\x12I\n\x10user_create_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01R\x0euserCreateTime\x12/\n\x11user_display_name\x18\x06 \x01(\tB\x03\xe0\x41\x01R\x0fuserDisplayName\x1a\x66\n\x08Location\x12&\n\x0c\x63ountry_code\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0b\x63ountryCode\x12\x19\n\x05state\x18\x02 \x01(\tB\x03\xe0\x41\x01R\x05state\x12\x17\n\x04\x63ity\x18\x03 \x01(\tB\x03\xe0\x41\x01R\x04\x63ity\x1a\xba\x02\n\x12\x46\x65\x65\x64\x62\x61\x63kProperties\x12\"\n\nsession_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\tsessionId\x12\x31\n\x12message_index_hint\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01R\x10messageIndexHint\x12j\n\x0f\x66\x65\x65\x64\x62\x61\x63k_target\x18\x03 \x01(\x0e\x32<.ingestion.v1alpha.EventProperties.FeedbackProperties.TargetB\x03\xe0\x41\x02R\x0e\x66\x65\x65\x64\x62\x61\x63kTarget\x12\x17\n\x04type\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x04type\"H\n\x06Target\x12\x16\n\x12TARGET_UNSPECIFIED\x10\x00\x12\x12\n\x0eTARGET_SESSION\x10\x01\x12\x12\n\x0eTARGET_MESSAGE\x10\x02\x1a=\n\x13\x43ustomPropertyValue\x12&\n\x0cstring_value\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bstringValue\x1a{\n\x15\x43ustomPropertiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12L\n\x05value\x18\x02 \x01(\x0b\x32\x36.ingestion.v1alpha.EventProperties.CustomPropertyValueR\x05value:\x02\x38\x01\x42\x15\n\x13reserved_propertiesJ\x04\x08\x05\x10\nB\xd7\x01\n\x15\x63om.ingestion.v1alphaB\nEventProtoP\x01ZMgithub.com/coxwave/impaction-ai-api/gen/go/ingestion/v1alpha;ingestionv1alpha\xa2\x02\x03IXX\xaa\x02\x11Ingestion.V1alpha\xca\x02\x11Ingestion\\V1alpha\xe2\x02\x1dIngestion\\V1alpha\\GPBMetadata\xea\x02\x12Ingestion::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ingestion.v1alpha.event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.ingestion.v1alphaB\nEventProtoP\001ZMgithub.com/coxwave/impaction-ai-api/gen/go/ingestion/v1alpha;ingestionv1alpha\242\002\003IXX\252\002\021Ingestion.V1alpha\312\002\021Ingestion\\V1alpha\342\002\035Ingestion\\V1alpha\\GPBMetadata\352\002\022Ingestion::V1alpha'
  _globals['_EVENT'].fields_by_name['id']._options = None
  _globals['_EVENT'].fields_by_name['id']._serialized_options = b'\340A\002'
  _globals['_EVENT'].fields_by_name['type']._options = None
  _globals['_EVENT'].fields_by_name['type']._serialized_options = b'\340A\002'
  _globals['_EVENT'].fields_by_name['create_time']._options = None
  _globals['_EVENT'].fields_by_name['create_time']._serialized_options = b'\340A\001'
  _globals['_EVENT'].fields_by_name['properties']._options = None
  _globals['_EVENT'].fields_by_name['properties']._serialized_options = b'\340A\002'
  _globals['_EVENT'].fields_by_name['project_id']._options = None
  _globals['_EVENT'].fields_by_name['project_id']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['session_id']._options = None
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['session_id']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['session_title']._options = None
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['session_title']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['session_start_time']._options = None
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['session_start_time']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['user_id']._options = None
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['user_id']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['assistant_id']._options = None
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES'].fields_by_name['assistant_id']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['session_id']._options = None
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['session_id']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_id_hint']._options = None
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_id_hint']._serialized_options = b'\030\001\340A\001'
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_index_hint']._options = None
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_index_hint']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_role']._options = None
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_role']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_content']._options = None
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_content']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_create_time']._options = None
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES'].fields_by_name['message_create_time']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION'].fields_by_name['country_code']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION'].fields_by_name['country_code']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION'].fields_by_name['state']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION'].fields_by_name['state']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION'].fields_by_name['city']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION'].fields_by_name['city']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_id']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_id']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_email']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_email']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_ip']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_ip']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_location']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_location']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_create_time']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_create_time']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_display_name']._options = None
  _globals['_EVENTPROPERTIES_USERPROPERTIES'].fields_by_name['user_display_name']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['session_id']._options = None
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['session_id']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['message_index_hint']._options = None
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['message_index_hint']._serialized_options = b'\340A\001'
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['feedback_target']._options = None
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['feedback_target']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['type']._options = None
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES'].fields_by_name['type']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTYVALUE'].fields_by_name['string_value']._options = None
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTYVALUE'].fields_by_name['string_value']._serialized_options = b'\340A\002'
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTIESENTRY']._options = None
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_EVENTPROPERTIES'].fields_by_name['custom_properties']._options = None
  _globals['_EVENTPROPERTIES'].fields_by_name['custom_properties']._serialized_options = b'\340A\001'
  _globals['_EVENT']._serialized_start=119
  _globals['_EVENT']._serialized_end=347
  _globals['_EVENTPROPERTIES']._serialized_start=350
  _globals['_EVENTPROPERTIES']._serialized_end=2556
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES']._serialized_start=884
  _globals['_EVENTPROPERTIES_SESSIONPROPERTIES']._serialized_end=1130
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES']._serialized_start=1133
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES']._serialized_end=1577
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES_ROLE']._serialized_start=1514
  _globals['_EVENTPROPERTIES_MESSAGEPROPERTIES_ROLE']._serialized_end=1577
  _globals['_EVENTPROPERTIES_USERPROPERTIES']._serialized_start=1580
  _globals['_EVENTPROPERTIES_USERPROPERTIES']._serialized_end=2022
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION']._serialized_start=1920
  _globals['_EVENTPROPERTIES_USERPROPERTIES_LOCATION']._serialized_end=2022
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES']._serialized_start=2025
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES']._serialized_end=2339
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES_TARGET']._serialized_start=2267
  _globals['_EVENTPROPERTIES_FEEDBACKPROPERTIES_TARGET']._serialized_end=2339
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTYVALUE']._serialized_start=2341
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTYVALUE']._serialized_end=2402
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTIESENTRY']._serialized_start=2404
  _globals['_EVENTPROPERTIES_CUSTOMPROPERTIESENTRY']._serialized_end=2527
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: axes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\naxes.proto"\xcc\x01\n\tAxisProto\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x07 \x01(\t\x12\x11\n\tmin_value\x18\x02 \x01(\x02\x12\x15\n\rdefault_value\x18\x03 \x01(\x02\x12\x11\n\tmax_value\x18\x04 \x01(\x02\x12\x11\n\tprecision\x18\x05 \x01(\x05\x12 \n\x08\x66\x61llback\x18\x06 \x03(\x0b\x32\x0e.FallbackProto\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x15\n\rfallback_only\x18\t \x01(\x08"B\n\rFallbackProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t'
)


_AXISPROTO = DESCRIPTOR.message_types_by_name["AxisProto"]
_FALLBACKPROTO = DESCRIPTOR.message_types_by_name["FallbackProto"]
AxisProto = _reflection.GeneratedProtocolMessageType(
    "AxisProto",
    (_message.Message,),
    {
        "DESCRIPTOR": _AXISPROTO,
        "__module__": "axes_pb2"
        # @@protoc_insertion_point(class_scope:AxisProto)
    },
)
_sym_db.RegisterMessage(AxisProto)

FallbackProto = _reflection.GeneratedProtocolMessageType(
    "FallbackProto",
    (_message.Message,),
    {
        "DESCRIPTOR": _FALLBACKPROTO,
        "__module__": "axes_pb2"
        # @@protoc_insertion_point(class_scope:FallbackProto)
    },
)
_sym_db.RegisterMessage(FallbackProto)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _AXISPROTO._serialized_start = 15
    _AXISPROTO._serialized_end = 219
    _FALLBACKPROTO._serialized_start = 221
    _FALLBACKPROTO._serialized_end = 287
# @@protoc_insertion_point(module_scope)

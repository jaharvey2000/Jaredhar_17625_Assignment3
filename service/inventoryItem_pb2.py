# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryItem.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import book_pb2 as book__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13inventoryItem.proto\x12\x02\x61\x33\x1a\nbook.proto\"\xb1\x01\n\rInventoryItem\x12\x13\n\x06number\x18\x01 \x01(\x05H\x01\x88\x01\x01\x12\x18\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x08.a3.BookH\x00\x12-\n\x06status\x18\x03 \x01(\x0e\x32\x18.a3.InventoryItem.StatusH\x02\x88\x01\x01\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\x08\n\x06objectB\t\n\x07_numberB\t\n\x07_statusb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventoryItem_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INVENTORYITEM._serialized_start=40
  _INVENTORYITEM._serialized_end=217
  _INVENTORYITEM_STATUS._serialized_start=151
  _INVENTORYITEM_STATUS._serialized_end=185
# @@protoc_insertion_point(module_scope)

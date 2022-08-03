# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/x509/x509.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/x509/x509.proto',
  package='common',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x63ommon/x509/x509.proto\x12\x06\x63ommon\"N\n\x07X509Org\x12\t\n\x01\x43\x18\x01 \x01(\t\x12\t\n\x01O\x18\x02 \x01(\t\x12\n\n\x02OU\x18\x03 \x01(\t\x12\n\n\x02\x43N\x18\x04 \x01(\t\x12\t\n\x01L\x18\x05 \x01(\t\x12\n\n\x02ST\x18\x06 \x01(\t\"1\n\x08Validity\x12\x12\n\nnot_before\x18\x01 \x01(\x04\x12\x11\n\tnot_after\x18\x02 \x01(\x04\"K\n\x0fX509Fingerprint\x12\x1d\n\x15\x66ingerprint_algorithm\x18\x01 \x01(\t\x12\x19\n\x11\x66ingerprint_value\x18\x02 \x01(\t\"=\n\rX509Extension\x12\x0b\n\x03oid\x18\x01 \x01(\t\x12\x10\n\x08\x63ritical\x18\x02 \x01(\x08\x12\r\n\x05value\x18\x03 \x01(\t\"G\n\rX509PublicKey\x12\x1c\n\x14public_key_algorithm\x18\x01 \x01(\t\x12\x18\n\x10public_key_value\x18\x02 \x01(\t\"E\n\rX509Signature\x12\x1b\n\x13signature_algorithm\x18\x01 \x01(\t\x12\x17\n\x0fsignature_value\x18\x02 \x01(\t\"\xa3\x02\n\x08X509Cert\x12\x16\n\x0eversion_number\x18\x01 \x01(\r\x12\x15\n\rserial_number\x18\x02 \x01(\t\x12\x1f\n\x06issuer\x18\x03 \x01(\x0b\x32\x0f.common.X509Org\x12\"\n\x08validity\x18\x04 \x01(\x0b\x32\x10.common.Validity\x12 \n\x07subject\x18\x05 \x01(\x0b\x32\x0f.common.X509Org\x12)\n\npublic_key\x18\x06 \x01(\x0b\x32\x15.common.X509PublicKey\x12(\n\tsignature\x18\x07 \x01(\x0b\x32\x15.common.X509Signature\x12,\n\x0b\x66ingerprint\x18\x08 \x03(\x0b\x32\x17.common.X509Fingerprint'
)




_X509ORG = _descriptor.Descriptor(
  name='X509Org',
  full_name='common.X509Org',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='C', full_name='common.X509Org.C', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='O', full_name='common.X509Org.O', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OU', full_name='common.X509Org.OU', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CN', full_name='common.X509Org.CN', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='L', full_name='common.X509Org.L', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ST', full_name='common.X509Org.ST', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=112,
)


_VALIDITY = _descriptor.Descriptor(
  name='Validity',
  full_name='common.Validity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='not_before', full_name='common.Validity.not_before', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='not_after', full_name='common.Validity.not_after', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=163,
)


_X509FINGERPRINT = _descriptor.Descriptor(
  name='X509Fingerprint',
  full_name='common.X509Fingerprint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fingerprint_algorithm', full_name='common.X509Fingerprint.fingerprint_algorithm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fingerprint_value', full_name='common.X509Fingerprint.fingerprint_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=240,
)


_X509EXTENSION = _descriptor.Descriptor(
  name='X509Extension',
  full_name='common.X509Extension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='common.X509Extension.oid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='critical', full_name='common.X509Extension.critical', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.X509Extension.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=303,
)


_X509PUBLICKEY = _descriptor.Descriptor(
  name='X509PublicKey',
  full_name='common.X509PublicKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key_algorithm', full_name='common.X509PublicKey.public_key_algorithm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_key_value', full_name='common.X509PublicKey.public_key_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=376,
)


_X509SIGNATURE = _descriptor.Descriptor(
  name='X509Signature',
  full_name='common.X509Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_algorithm', full_name='common.X509Signature.signature_algorithm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature_value', full_name='common.X509Signature.signature_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=447,
)


_X509CERT = _descriptor.Descriptor(
  name='X509Cert',
  full_name='common.X509Cert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version_number', full_name='common.X509Cert.version_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='common.X509Cert.serial_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issuer', full_name='common.X509Cert.issuer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validity', full_name='common.X509Cert.validity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='common.X509Cert.subject', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='common.X509Cert.public_key', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='common.X509Cert.signature', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='common.X509Cert.fingerprint', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=741,
)

_X509CERT.fields_by_name['issuer'].message_type = _X509ORG
_X509CERT.fields_by_name['validity'].message_type = _VALIDITY
_X509CERT.fields_by_name['subject'].message_type = _X509ORG
_X509CERT.fields_by_name['public_key'].message_type = _X509PUBLICKEY
_X509CERT.fields_by_name['signature'].message_type = _X509SIGNATURE
_X509CERT.fields_by_name['fingerprint'].message_type = _X509FINGERPRINT
DESCRIPTOR.message_types_by_name['X509Org'] = _X509ORG
DESCRIPTOR.message_types_by_name['Validity'] = _VALIDITY
DESCRIPTOR.message_types_by_name['X509Fingerprint'] = _X509FINGERPRINT
DESCRIPTOR.message_types_by_name['X509Extension'] = _X509EXTENSION
DESCRIPTOR.message_types_by_name['X509PublicKey'] = _X509PUBLICKEY
DESCRIPTOR.message_types_by_name['X509Signature'] = _X509SIGNATURE
DESCRIPTOR.message_types_by_name['X509Cert'] = _X509CERT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

X509Org = _reflection.GeneratedProtocolMessageType('X509Org', (_message.Message,), {
  'DESCRIPTOR' : _X509ORG,
  '__module__' : 'common.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:common.X509Org)
  })
_sym_db.RegisterMessage(X509Org)

Validity = _reflection.GeneratedProtocolMessageType('Validity', (_message.Message,), {
  'DESCRIPTOR' : _VALIDITY,
  '__module__' : 'common.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:common.Validity)
  })
_sym_db.RegisterMessage(Validity)

X509Fingerprint = _reflection.GeneratedProtocolMessageType('X509Fingerprint', (_message.Message,), {
  'DESCRIPTOR' : _X509FINGERPRINT,
  '__module__' : 'common.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:common.X509Fingerprint)
  })
_sym_db.RegisterMessage(X509Fingerprint)

X509Extension = _reflection.GeneratedProtocolMessageType('X509Extension', (_message.Message,), {
  'DESCRIPTOR' : _X509EXTENSION,
  '__module__' : 'common.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:common.X509Extension)
  })
_sym_db.RegisterMessage(X509Extension)

X509PublicKey = _reflection.GeneratedProtocolMessageType('X509PublicKey', (_message.Message,), {
  'DESCRIPTOR' : _X509PUBLICKEY,
  '__module__' : 'common.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:common.X509PublicKey)
  })
_sym_db.RegisterMessage(X509PublicKey)

X509Signature = _reflection.GeneratedProtocolMessageType('X509Signature', (_message.Message,), {
  'DESCRIPTOR' : _X509SIGNATURE,
  '__module__' : 'common.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:common.X509Signature)
  })
_sym_db.RegisterMessage(X509Signature)

X509Cert = _reflection.GeneratedProtocolMessageType('X509Cert', (_message.Message,), {
  'DESCRIPTOR' : _X509CERT,
  '__module__' : 'common.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:common.X509Cert)
  })
_sym_db.RegisterMessage(X509Cert)


# @@protoc_insertion_point(module_scope)

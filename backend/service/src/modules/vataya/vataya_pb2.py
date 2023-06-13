# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vataya.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='vataya.proto',
    package='service',
    syntax='proto3',
    serialized_options=b'Z\010service/',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0cvataya.proto\x12\x07service\"\xbd\x01\n\nClientInfo\x12\x0e\n\x06\x61pikey\x18\x01 \x01(\t\x12\x10\n\x08\x63lientid\x18\x02 \x01(\t\x12#\n\x08sampling\x18\x03 \x01(\x0e\x32\x11.service.Sampling\x12-\n\rtexttransform\x18\x04 \x01(\x0e\x32\x16.service.TextTransform\x12\x11\n\tsingleutt\x18\x05 \x01(\x08\x12\x12\n\ndisablevad\x18\x06 \x01(\x08\x12\x12\n\nwordresult\x18\x07 \x01(\x08\"\x1d\n\x0b\x43onnectInfo\x12\x0e\n\x06status\x18\x01 \x01(\x05\")\n\tAudioData\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x0b\n\x03vad\x18\x02 \x01(\x08\"\"\n\tRecogData\x12\x15\n\rtranscription\x18\x01 \x01(\t*\x1a\n\x08Sampling\x12\x06\n\x02NB\x10\x00\x12\x06\n\x02WB\x10\x01*9\n\rTextTransform\x12\r\n\tTransform\x10\x00\x12\x0f\n\x0bLineSegment\x10\x01\x12\x08\n\x04None\x10\x03\x32~\n\rVatayaService\x12\x34\n\x07\x43onnect\x12\x13.service.ClientInfo\x1a\x14.service.ConnectInfo\x12\x37\n\tRecognize\x12\x12.service.AudioData\x1a\x12.service.RecogData(\x01\x30\x01\x42\nZ\x08service/b\x06proto3'
)

_SAMPLING = _descriptor.EnumDescriptor(
    name='Sampling',
    full_name='service.Sampling',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='NB', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='WB', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=327,
    serialized_end=353,
)
_sym_db.RegisterEnumDescriptor(_SAMPLING)

Sampling = enum_type_wrapper.EnumTypeWrapper(_SAMPLING)
_TEXTTRANSFORM = _descriptor.EnumDescriptor(
    name='TextTransform',
    full_name='service.TextTransform',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='Transform', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='LineSegment', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='None', index=2, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=355,
    serialized_end=412,
)
_sym_db.RegisterEnumDescriptor(_TEXTTRANSFORM)

TextTransform = enum_type_wrapper.EnumTypeWrapper(_TEXTTRANSFORM)
NB = 0
WB = 1
Transform = 0
LineSegment = 1
globals()['None'] = 3


_CLIENTINFO = _descriptor.Descriptor(
    name='ClientInfo',
    full_name='service.ClientInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='apikey', full_name='service.ClientInfo.apikey', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='clientid', full_name='service.ClientInfo.clientid', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='sampling', full_name='service.ClientInfo.sampling', index=2,
            number=3, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='texttransform', full_name='service.ClientInfo.texttransform', index=3,
            number=4, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='singleutt', full_name='service.ClientInfo.singleutt', index=4,
            number=5, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='disablevad', full_name='service.ClientInfo.disablevad', index=5,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='wordresult', full_name='service.ClientInfo.wordresult', index=6,
            number=7, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
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
    serialized_start=26,
    serialized_end=215,
)


_CONNECTINFO = _descriptor.Descriptor(
    name='ConnectInfo',
    full_name='service.ConnectInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='status', full_name='service.ConnectInfo.status', index=0,
            number=1, type=5, cpp_type=1, label=1,
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
    serialized_start=217,
    serialized_end=246,
)


_AUDIODATA = _descriptor.Descriptor(
    name='AudioData',
    full_name='service.AudioData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='content', full_name='service.AudioData.content', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='vad', full_name='service.AudioData.vad', index=1,
            number=2, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
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
    serialized_start=248,
    serialized_end=289,
)


_RECOGDATA = _descriptor.Descriptor(
    name='RecogData',
    full_name='service.RecogData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='transcription', full_name='service.RecogData.transcription', index=0,
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
    serialized_start=291,
    serialized_end=325,
)

_CLIENTINFO.fields_by_name['sampling'].enum_type = _SAMPLING
_CLIENTINFO.fields_by_name['texttransform'].enum_type = _TEXTTRANSFORM
DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.message_types_by_name['ConnectInfo'] = _CONNECTINFO
DESCRIPTOR.message_types_by_name['AudioData'] = _AUDIODATA
DESCRIPTOR.message_types_by_name['RecogData'] = _RECOGDATA
DESCRIPTOR.enum_types_by_name['Sampling'] = _SAMPLING
DESCRIPTOR.enum_types_by_name['TextTransform'] = _TEXTTRANSFORM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), {
    'DESCRIPTOR': _CLIENTINFO,
    '__module__': 'vataya_pb2'
    # @@protoc_insertion_point(class_scope:service.ClientInfo)
})
_sym_db.RegisterMessage(ClientInfo)

ConnectInfo = _reflection.GeneratedProtocolMessageType('ConnectInfo', (_message.Message,), {
    'DESCRIPTOR': _CONNECTINFO,
    '__module__': 'vataya_pb2'
    # @@protoc_insertion_point(class_scope:service.ConnectInfo)
})
_sym_db.RegisterMessage(ConnectInfo)

AudioData = _reflection.GeneratedProtocolMessageType('AudioData', (_message.Message,), {
    'DESCRIPTOR': _AUDIODATA,
    '__module__': 'vataya_pb2'
    # @@protoc_insertion_point(class_scope:service.AudioData)
})
_sym_db.RegisterMessage(AudioData)

RecogData = _reflection.GeneratedProtocolMessageType('RecogData', (_message.Message,), {
    'DESCRIPTOR': _RECOGDATA,
    '__module__': 'vataya_pb2'
    # @@protoc_insertion_point(class_scope:service.RecogData)
})
_sym_db.RegisterMessage(RecogData)


DESCRIPTOR._options = None

_VATAYASERVICE = _descriptor.ServiceDescriptor(
    name='VatayaService',
    full_name='service.VatayaService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=414,
    serialized_end=540,
    methods=[
        _descriptor.MethodDescriptor(
            name='Connect',
            full_name='service.VatayaService.Connect',
            index=0,
            containing_service=None,
            input_type=_CLIENTINFO,
            output_type=_CONNECTINFO,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='Recognize',
            full_name='service.VatayaService.Recognize',
            index=1,
            containing_service=None,
            input_type=_AUDIODATA,
            output_type=_RECOGDATA,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_VATAYASERVICE)

DESCRIPTOR.services_by_name['VatayaService'] = _VATAYASERVICE

# @@protoc_insertion_point(module_scope)

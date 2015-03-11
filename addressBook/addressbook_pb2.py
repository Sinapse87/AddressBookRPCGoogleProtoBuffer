# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='addressbook.proto',
  package='',
  serialized_pb=_b('\n\x11\x61\x64\x64ressbook.proto\"\xc8\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\"\n\x05phone\x18\x04 \x03(\x0b\x32\x13.Person.PhoneNumber\x1a\x44\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x02(\t\x12%\n\x04type\x18\x02 \x01(\x0e\x32\x11.Person.PhoneType:\x04HOME\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"&\n\x0b\x41\x64\x64ressBook\x12\x17\n\x06person\x18\x01 \x03(\x0b\x32\x07.Person\"0\n\x15getAddressBookRequest\x12\x17\n\x0f\x61\x64\x64ressBookName\x18\x01 \x01(\t\"8\n\x13getAddressBookReply\x12!\n\x0b\x61\x64\x64ressBook\x18\x01 \x02(\x0b\x32\x0c.AddressBook\"!\n\x0e\x61\x64\x64PersonReply\x12\x0f\n\x07message\x18\x01 \x02(\t\"+\n\x10\x61\x64\x64PersonRequest\x12\x17\n\x06person\x18\x01 \x02(\x0b\x32\x07.Person2\x89\x01\n\x12\x41\x64\x64ressBookService\x12\x31\n\taddPerson\x12\x11.addPersonRequest\x1a\x0f.addPersonReply\"\x00\x12@\n\x0egetAddressBook\x12\x16.getAddressBookRequest\x1a\x14.getAddressBookReply\"\x00\x42)\n\x14\x63om.example.tutorialB\x11\x41\x64\x64ressBookProtos')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PERSON_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='Person.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=179,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONETYPE)


_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='Person.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Person.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Person.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=177,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Person.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Person.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone', full_name='Person.phone', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_PHONENUMBER, ],
  enum_types=[
    _PERSON_PHONETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=222,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='AddressBook.person', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=262,
)


_GETADDRESSBOOKREQUEST = _descriptor.Descriptor(
  name='getAddressBookRequest',
  full_name='getAddressBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addressBookName', full_name='getAddressBookRequest.addressBookName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=312,
)


_GETADDRESSBOOKREPLY = _descriptor.Descriptor(
  name='getAddressBookReply',
  full_name='getAddressBookReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addressBook', full_name='getAddressBookReply.addressBook', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=370,
)


_ADDPERSONREPLY = _descriptor.Descriptor(
  name='addPersonReply',
  full_name='addPersonReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='addPersonReply.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=405,
)


_ADDPERSONREQUEST = _descriptor.Descriptor(
  name='addPersonRequest',
  full_name='addPersonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='addPersonRequest.person', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=450,
)

_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONETYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON.fields_by_name['phone'].message_type = _PERSON_PHONENUMBER
_PERSON_PHONETYPE.containing_type = _PERSON
_ADDRESSBOOK.fields_by_name['person'].message_type = _PERSON
_GETADDRESSBOOKREPLY.fields_by_name['addressBook'].message_type = _ADDRESSBOOK
_ADDPERSONREQUEST.fields_by_name['person'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
DESCRIPTOR.message_types_by_name['getAddressBookRequest'] = _GETADDRESSBOOKREQUEST
DESCRIPTOR.message_types_by_name['getAddressBookReply'] = _GETADDRESSBOOKREPLY
DESCRIPTOR.message_types_by_name['addPersonReply'] = _ADDPERSONREPLY
DESCRIPTOR.message_types_by_name['addPersonRequest'] = _ADDPERSONREQUEST

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(

  PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _PERSON_PHONENUMBER,
    __module__ = 'addressbook_pb2'
    # @@protoc_insertion_point(class_scope:Person.PhoneNumber)
    ))
  ,
  DESCRIPTOR = _PERSON,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  ))
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.PhoneNumber)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)

getAddressBookRequest = _reflection.GeneratedProtocolMessageType('getAddressBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETADDRESSBOOKREQUEST,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:getAddressBookRequest)
  ))
_sym_db.RegisterMessage(getAddressBookRequest)

getAddressBookReply = _reflection.GeneratedProtocolMessageType('getAddressBookReply', (_message.Message,), dict(
  DESCRIPTOR = _GETADDRESSBOOKREPLY,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:getAddressBookReply)
  ))
_sym_db.RegisterMessage(getAddressBookReply)

addPersonReply = _reflection.GeneratedProtocolMessageType('addPersonReply', (_message.Message,), dict(
  DESCRIPTOR = _ADDPERSONREPLY,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:addPersonReply)
  ))
_sym_db.RegisterMessage(addPersonReply)

addPersonRequest = _reflection.GeneratedProtocolMessageType('addPersonRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDPERSONREQUEST,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:addPersonRequest)
  ))
_sym_db.RegisterMessage(addPersonRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024com.example.tutorialB\021AddressBookProtos'))
import abc
from grpc.early_adopter import implementations
from grpc.early_adopter import utilities
class EarlyAdopterAddressBookServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def addPerson(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def getAddressBook(self, request, context):
    raise NotImplementedError()
class EarlyAdopterAddressBookServiceServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterAddressBookServiceStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def addPerson(self, request):
    raise NotImplementedError()
  addPerson.async = None
  @abc.abstractmethod
  def getAddressBook(self, request):
    raise NotImplementedError()
  getAddressBook.async = None
def early_adopter_create_AddressBookService_server(servicer, port, root_certificates, key_chain_pairs):
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  method_service_descriptions = {
    "addPerson": utilities.unary_unary_service_description(
      servicer.addPerson,
      addressbook_pb2.addPersonRequest.FromString,
      addressbook_pb2.addPersonReply.SerializeToString,
    ),
    "getAddressBook": utilities.unary_unary_service_description(
      servicer.getAddressBook,
      addressbook_pb2.getAddressBookRequest.FromString,
      addressbook_pb2.getAddressBookReply.SerializeToString,
    ),
  }
  return implementations.secure_server(method_service_descriptions, port, root_certificates, key_chain_pairs)
def early_adopter_create_AddressBookService_stub(host, port):
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  method_invocation_descriptions = {
    "addPerson": utilities.unary_unary_invocation_description(
      addressbook_pb2.addPersonRequest.SerializeToString,
      addressbook_pb2.addPersonReply.FromString,
    ),
    "getAddressBook": utilities.unary_unary_invocation_description(
      addressbook_pb2.getAddressBookRequest.SerializeToString,
      addressbook_pb2.getAddressBookReply.FromString,
    ),
  }
  return implementations.insecure_stub(method_invocation_descriptions, host, port)
# @@protoc_insertion_point(module_scope)
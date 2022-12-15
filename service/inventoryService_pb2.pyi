import book_pb2 as _book_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    def __init__(self, book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ...) -> None: ...

class GetBookReply(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    def __init__(self, book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

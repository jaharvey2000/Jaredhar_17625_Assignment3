from __future__ import print_function

import logging

import grpc
import book_pb2
import inventoryService_pb2
import inventoryService_pb2_grpc

def runCreateValid(stub):
    print('CREATEBOOK VALID TEST CASE')

    newBook = book_pb2.Book()
    newBook.ISBN = '4812162024'
    newBook.title = 'Book Title 4'
    newBook.author = 'Book Author 4'
    newBook.genre = newBook.Genre.NONFICTION
    newBook.publishedYear = 2022
    print('Book:\n' + str(newBook))

    response = stub.CreateBook(inventoryService_pb2.CreateBookRequest(book=newBook))
    print('Client received: ' + response.message)
    print()

def runCreateInvalid(stub):
    print('CREATEBOOK INVALID TEST CASE')

    newBook = book_pb2.Book()
    newBook.ISBN = '1234567890'
    print('Book:\n' + str(newBook))

    try:
        response = stub.CreateBook(inventoryService_pb2.CreateBookRequest(book=newBook))
    except grpc.RpcError as e:
        print('Client received error:')
        print(f'Error code: {e.code().name} ({e.code().value})')
        print(f'Details: {e.details()}')

def runGetValid(stub):
    validISBN = '4812162024'

    print('GETBOOK VALID TEST CASE')
    print(f'GetBook(ISBN={validISBN}): \n')

    response = stub.GetBook(inventoryService_pb2.GetBookRequest(ISBN=validISBN))
    print('Client received:\n' + str(response.book))
    print()

def runGetInvalid(stub):
    invalidISBN = '5101520253'

    print('GETBOOK INVALID TEST CASE')
    print(f'GetBook(ISBN={invalidISBN}): \n')

    try:
        response = stub.GetBook(inventoryService_pb2.GetBookRequest(ISBN=invalidISBN))
    except grpc.RpcError as e:
        print('Client received error:')
        print(f'Error code: {e.code().name} ({e.code().value})')
        print(f'Details: {e.details()}')


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)
        runCreateValid(stub)
        runCreateInvalid(stub)
        runGetValid(stub)
        runGetInvalid(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()
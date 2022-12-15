from __future__ import print_function

import logging

import grpc
import book_pb2
import inventoryService_pb2
import inventoryService_pb2_grpc

sectionBreak = '======================================================='

def runCreate(stub, caseName, newISBN, newTitle, newAuthor, newYear):
    print(sectionBreak)
    print(caseName + '\n')

    newBook = book_pb2.Book()
    if newISBN is not None:
        newBook.ISBN = newISBN
    if newTitle is not None:
        newBook.title = newTitle
    if newAuthor is not None:
        newBook.author = newAuthor
    if newYear is not None:
        newBook.publishedYear = newYear
    newBook.genre = newBook.Genre.NONFICTION
    print('Input Book:\n' + str(newBook))

    try:
        response = stub.CreateBook(inventoryService_pb2.CreateBookRequest(book=newBook))
        print('Client received: ' + response.message)
    except grpc.RpcError as e:
        print('Client received error:')
        print(f'Error code: {e.code().name} ({e.code().value})')
        print(f'Details: {e.details()}')
    print(sectionBreak)

def runGet(stub, caseName, searchISBN):
    print(sectionBreak)
    print(caseName + '\n')

    try:
        response = stub.GetBook(inventoryService_pb2.GetBookRequest(ISBN=searchISBN))
        print('Client received: ' + str(response.book))
    except grpc.RpcError as e:
        print('Client received error:')
        print(f'Error code: {e.code().name} ({e.code().value})')
        print(f'Details: {e.details()}')
    print(sectionBreak)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)
        # runCreateValid(stub)
        # runCreateInvalid(stub)
        runCreate(stub, '1. CREATEBOOK VALID CASE', '4812162024', 'Title 4', 'Author 4', 2022)
        runCreate(stub, '2. CREATEBOOK INVALID ISBN', '4812162024', None, None, None)
        # runGetValid(stub)
        # runGetInvalid(stub)
        runGet(stub, '3. GETBOOK VALID CASE', '4812162024')
        runGet(stub, '4. GETBOOK INVALID ISBN', '5101520253')

if __name__ == '__main__':
    logging.basicConfig()
    run()
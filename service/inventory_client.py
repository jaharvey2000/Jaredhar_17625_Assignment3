from __future__ import print_function

import logging

import grpc
import book_pb2
import inventoryService_pb2
import inventoryService_pb2_grpc

sectionBreak = '======================================================='

def runCreate(stub, caseName, newISBN, newTitle, newAuthor, newYear):
    '''
    Perform a test of the CreateBook RPC

    Parameters
    ----------
    stub : inventoryService_pb2_grpc.InventoryServiceStub
        the server stub to send the request to
    caseName : str
        the test case name
    newISBN : str
        the ISBN of the book to add
    newTitle : str
        the title of the book to add
    newAuthor : str
        the author of the book to add
    newYear : str
        the publication year of the book to add
    '''

    print(sectionBreak)
    print(caseName + '\n')

    # Create the new book object
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
        # If the request is successful, print the result
        response = stub.CreateBook(inventoryService_pb2.CreateBookRequest(book=newBook))
        print('Client received:\n' + response.message)
    except grpc.RpcError as e:
        # If an error occurs, print it
        print('Client received error:')
        print(f'Error code: {e.code().name} ({e.code().value})')
        print(f'Details: {e.details()}')
    print(sectionBreak)

def runGet(stub, caseName, searchISBN):
    '''
    Perform a test of the GetBook RPC

    Parameters
    ----------
    stub : inventoryService_pb2_grpc.InventoryServiceStub
        the server stub to send the request to
    caseName : str
        the test case name
    searchISBN : str
        the ISBN of the book to search for
    '''

    print(sectionBreak)
    print(caseName + '\n')

    try:
        # If the request is successful, print the result
        response = stub.GetBook(inventoryService_pb2.GetBookRequest(ISBN=searchISBN))
        print('Client received:\n' + str(response.book))
    except grpc.RpcError as e:
        # If an error occurs, print it
        print('Client received error:')
        print(f'Error code: {e.code().name} ({e.code().value})')
        print(f'Details: {e.details()}')
    print(sectionBreak)


def run():
    '''
    Runs a small suite of tests for the gRPC implementation.

    The following tests are performed:
        1. CreateBook "happy path"
        2. CreateBook error case: input is missing fields
        3. CreateBook error case: book with given ISBN already exists
        4. GetBook "happy path"
        5. GetBook error case: no book with given ISBN exists
    '''

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)
        runCreate(stub, '1. CREATEBOOK VALID CASE', '4812162024', 'Title 4', 'Author 4', 2022)
        runCreate(stub, '2. CREATEBOOK MISSING FIELDS', '6121824303', None, 'An Author', 2022)
        runCreate(stub, '3. CREATEBOOK INVALID ISBN', '4812162024', None, None, None)
        runGet(stub, '4. GETBOOK VALID CASE', '4812162024')
        runGet(stub, '5. GETBOOK INVALID ISBN', '5101520253')

if __name__ == '__main__':
    logging.basicConfig()
    run()
import grpc
import os
import sys

# Need to use a workaround to access protobuf/RPC files in ../service
sys.path.append(os.path.dirname(__file__) + '/..')
sys.path.append(os.path.dirname(__file__) + '/../service')
from service import book_pb2
from service import inventoryService_pb2
from service import inventoryService_pb2_grpc

class InventoryClient:
    def __init__(self, host, port):
        self.host = '{0}:{1}'.format(host, port)
        self.channel = grpc.insecure_channel(self.host)
        self.stub = inventoryService_pb2_grpc.InventoryServiceStub(self.channel)

    def getGenreFromString(self, newBook, newGenre):
        return 0

    def CreateBook(self, newISBN, newAuthor, newTitle, newGenre, newYear):
        if newISBN is None:
            raise Exception('Argument "newISBN" cannot be None')
        elif newAuthor is None:
            raise Exception('Argument "newAuthor" cannot be None')
        elif newTitle is None:
            raise Exception('Argument "newTitle" cannot be None')
        elif newGenre is None:
            raise Exception('Argument "newGenre" cannot be None')
        elif newYear is None:
            raise Exception('Argument "newYear" cannot be None')
            
        # Create a book object
        newBook = book_pb2.Book()
        newBook.ISBN = newISBN
        newBook.title = newTitle
        newBook.author = newAuthor
        newBook.genre = self.getGenreFromString(newBook, newGenre)
        newBook.publishedYear = newYear

        # Send the response
        try:
            # If the request is successful, print the result
            response = self.stub.CreateBook(
                inventoryService_pb2.CreateBookRequest(book=newBook))
            return response.message
        except grpc.RpcError as e:
            raise e

    def GetBook(self, searchISBN):
        if searchISBN is None:
            raise Exception('Argument "searchISBN" cannot be None')

        # Send the response
        try:
            # If the request is successful, print the result
            response = self.stub.GetBook(
                inventoryService_pb2.GetBookRequest(ISBN=searchISBN))
            return response.book
        except grpc.RpcError as e:
            raise e

from concurrent import futures
import logging

import grpc
import book_pb2
import inventoryService_pb2
import inventoryService_pb2_grpc

bookDb = dict()

class InventoryService(inventoryService_pb2_grpc.InventoryServiceServicer):
    # CreateBook
    def CreateBook(self, request, context):
        newBook = request.book
        if newBook.ISBN in bookDb.keys():
            # Book already exists; return an error
            msg = 'Book already exists with ISBN {}'.format(newBook.ISBN)
            context.set_details(msg)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return inventoryService_pb2.CreateBookReply()
        
        # Book doesn't exist; create it
        bookDb[newBook.ISBN] = newBook
        context.set_code(grpc.StatusCode.OK)
        return inventoryService_pb2.CreateBookReply(message='New book created with ISBN {}'.format(newBook.ISBN))

    # GetBook
    def GetBook(self, request, context):
        searchISBN = request.ISBN
        if searchISBN not in bookDb.keys():
            # Book not found; return an error
            msg = 'ISBN not found'
            context.set_details(msg)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return inventoryService_pb2.GetBookReply()
        
        # Book found; return it
        context.set_code(grpc.StatusCode.OK)
        return inventoryService_pb2.GetBookReply(book=bookDb[searchISBN])

# Configure server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    # Book 1
    book = book_pb2.Book()
    book.ISBN = '1234567890'
    book.title = 'Book Title 1'
    book.author = 'Book Author 1'
    book.genre = book.Genre.FANTASY
    book.publishedYear = 2000
    bookDb[book.ISBN] = book

    # Book 2
    book = book_pb2.Book()
    book.ISBN = '2468101214'
    book.title = 'Book Title 2'
    book.author = 'Book Author 2'
    book.genre = book.Genre.SCIFI
    book.publishedYear = 2005
    bookDb[book.ISBN] = book

    # Book 3
    book = book_pb2.Book()
    book.ISBN = '3691215182'
    book.title = 'Book Title 3'
    book.author = 'Book Author 3'
    book.genre = book.Genre.MYSTERY
    book.publishedYear = 2010
    bookDb[book.ISBN] = book

    print(bookDb)

    # Inititalize server
    logging.basicConfig()
    serve()
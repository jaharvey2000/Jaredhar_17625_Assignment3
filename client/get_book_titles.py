from inventory_client import InventoryClient

def getBookTitles(client, isbnList):
    '''
    Gets the book titles for a list of ISBNs

    Parameters
    ----------
    client : InventoryClient
        the client that interfaces with the Inventory gRPC API
    isbnList : List[str]
        a list of ISBNs to search for
    
    Returns
    -------
    A list of book titles corresponding to the ISBNs. If a book does not
    exist for a given ISBN, then None is returned for that book in the output
    array.
    '''

    # Handle invalid input
    if isbnList is None:
        return []
    
    allTitles = []

    # Try getting each book title
    for isbn in isbnList:
        try:
            book = client.GetBook(isbn)
            allTitles.append(book.title)
        except:
            allTitles.append(None)
    
    return allTitles

if __name__ == '__main__':
    # Instantiate client
    client = InventoryClient('localhost', '50051')

    # Get book titles (hard-coded list)
    isbnList = ['1234567890', '0000000000', '2468101214']
    titleList = getBookTitles(client, isbnList)

    # Output result
    print('Book titles:')
    for i,t in zip(isbnList, titleList):
        if t is None:
            print(f'\t{i}: NO BOOK EXISTS')
        else:
            print(f'\t{i}: "{t}"')

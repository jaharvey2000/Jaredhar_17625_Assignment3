from inventory_client import InventoryClient

def getBookTitles(client, isbnList):
    # Handle invalid input
    if isbnList is None:
        return []
    
    allTitles = []

    for isbn in isbnList:
        try:
            book = client.GetBook(isbn)
            allTitles.append(book.title)
        except:
            allTitles.append(None)
    
    return allTitles

if __name__ == '__main__':
    client = InventoryClient('localhost', '50051')
    isbnList = ['1234567890', '0000000000', '2468101214']

    titleList = getBookTitles(client, isbnList)

    print('Book titles:')
    for i,t in zip(isbnList, titleList):
        if t is None:
            print(f'\t{i}: NO BOOK EXISTS')
        else:
            print(f'\t{i}: "{t}"')

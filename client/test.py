from inventory_client import InventoryClient
from get_book_titles import getBookTitles

import unittest
from unittest.mock import Mock

# 1. Implement mock API client
mockClient = Mock(spec=InventoryClient)

# Basic Book object mock (for book.title access)
class Book:
    def __init__(self, title):
        self.title = title

# 2. Implement unit test using mock client
class TestMockClient(unittest.TestCase):
    def setUp(self):
        self.client = mockClient
    
    def testMockGetBooks(self):
        # Prepare mock behavior
        self.client.GetBook.reset_mock()
        mockValues = [Book('Book Title 1'), None, Book('Book Title 2')]
        self.client.GetBook.side_effect = mockValues

        # Call method
        isbns = ['1234567890', '0000000000', '2468101214']
        titles = getBookTitles(self.client, isbns)

        # Verify output
        expected = ['Book Title 1', None, 'Book Title 2']
        self.assertListEqual(expected, titles)

        # Verify mock behavior
        self.assertEqual(self.client.GetBook.call_count, 3)
        self.client.GetBook.assert_any_call(isbns[0])
        self.client.GetBook.assert_any_call(isbns[1])
        self.client.GetBook.assert_any_call(isbns[2])

    
    def testMockNoBooks(self):
        # Prepare mock behavior
        self.client.GetBook.reset_mock()
        self.client.GetBook.return_value = None

        # Call method
        isbns = []
        titles = getBookTitles(self.client, isbns)

        # Verify output
        expected = []
        self.assertListEqual(expected, titles)

        # Verify mock behavior
        self.assertEqual(self.client.GetBook.call_count, 0)

# 3. Implement unit test using live server
class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = InventoryClient('localhost', '50051')
    
    def testGetBooks(self):
        # Call method
        isbns = ['1234567890', '0000000000', '2468101214']
        titles = getBookTitles(self.client, isbns)

        # Verify output
        expected = ['Book Title 1', None, 'Book Title 2']
        self.assertListEqual(expected, titles)

    def testNoBooks(self):
        # Call method
        isbns = []
        titles = getBookTitles(self.client, isbns)

        # Verify output
        expected = []
        self.assertListEqual(expected, titles)

if __name__ == '__main__':
    unittest.main()
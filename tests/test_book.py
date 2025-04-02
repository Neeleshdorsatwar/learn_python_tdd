import unittest
from datetime import date
from src.book import Book
class TestBook(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_book_attributes(self):

        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        self.assertEqual(book1.isbn, "1234567890")
        self.assertEqual(book1.publication_date, date(2023, 1, 1))
        self.assertEqual(book1.title, "Sample Title")
        self.assertEqual(book1.author, "Sample Author")

    def test_book_is_equal(self):

        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        book2 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        
        self.assertEqual(book1, book2)





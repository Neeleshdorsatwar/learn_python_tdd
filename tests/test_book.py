import unittest
from datetime import date
class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")

    def test_book_attributes(self):
        self.assertEqual(self.book.isbn, "1234567890")
        self.assertEqual(self.book.publication_date, date(2023, 1, 1))
        self.assertEqual(self.book.title, "Sample Title")
        self.assertEqual(self.book.author, "Sample Author")

class Book:
    def __init__(self, isbn, publication_date, title, author):
        self.isbn = isbn
        self.publication_date = publication_date
        self.title = title
        self.author = author
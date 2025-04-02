import unittest
from datetime import date
from src.book import Book
from src.book_catalog import BookCatalog




class TestBookCatalog(unittest.TestCase):
    def test_add_book(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        book2 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        catalog.add_book(book1)
        self.assertIn(book1, catalog.get_books())
        catalog.add_book(book2)
        self.assertIn(book2, catalog.get_books())


    def test_get_books(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        book2 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        catalog.add_book(book1)
        catalog.add_book(book2)
        self.assertEqual(catalog.get_books(), [book1, book2])
    
    # create a test function to search for a book in the catalog using isbn number
    def test_search_book_by_isbn(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        book2 = Book(isbn="0987654321", publication_date=date(2023, 1, 1), title="Another Title", author="Another Author")
        catalog.add_book(book1)
        catalog.add_book(book2)
        # search for book1 in the catalog using isbn number
        result = catalog.search_book_by_isbn("1234567890")
        self.assertEqual(result, book1)
        # search for book2 in the catalog using isbn number
        result = catalog.search_book_by_isbn("11111111")
        self.assertIsNone(result)
    # remove a book from the catalog using isbn number
    
    def test_remove_book_by_isbn(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        
        catalog.add_book(book1)
        
        # remove book1 from the catalog using isbn number
        catalog.remove_book_by_isbn("1234567890")
        self.assertNotIn(book1, catalog.get_books())
        self.assertEqual(catalog.get_books(), [])



    # test remove book by isbn number not in catalog
    def test_remove_book_by_isbn_not_in_catalog(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        catalog.add_book(book1)
        
        # remove book1 from the catalog using isbn number
        message = catalog.remove_book_by_isbn("11111111")
        self.assertEqual(message, "book not found")
        
        self.assertIn(book1, catalog.get_books())


    # test search book by title 
    def test_search_book_by_title(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        book2 = Book(isbn="0987654321", publication_date=date(2023, 1, 1), title="Another Title", author="Another Author")
        catalog.add_book(book1)
        catalog.add_book(book2)
        # search for book1 in the catalog using title
        result = catalog.search_book_by_title("Sample Title")
        self.assertEqual(result, book1)
        
        # search for book2 in the catalog using title
        result = catalog.search_book_by_title("Another Title")
        self.assertEqual(result, book2)
        result = catalog.search_book_by_title("11111111")
        self.assertEqual("book not found", result)
        
    # test search book by author
    def test_search_book_by_author(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        book2 = Book(isbn="0987654321", publication_date=date(2023, 1, 1), title="Another Title", author="Another Author")
        book3 = Book(isbn="1111111111", publication_date=date(2023, 1, 1), title="Another Title", author="Another Author")
        catalog.add_book(book1)
        catalog.add_book(book2)
        catalog.add_book(book3)
        # search for book1 in the catalog using author name
        result = catalog.search_book_by_author("Sample Author")
        #check result is a list of books
        self.assertIsInstance(result, list)
        self.assertIn(book1, result)

        # search for book2 in the catalog using author name
        result = catalog.search_book_by_author("Another Author")
        self.assertIn(book2, result)
        self.assertIn(book3, result)
    # create a test fuction that searches with an empty catalog
    def test_search_book_by_author_empty_catalog(self):
        catalog = BookCatalog()
        result = catalog.search_book_by_author("Sample Author")
        self.assertIsNone(result)
    # create a test function that looks for all books in the catalog
    def test_search_all_books(self):
        catalog = BookCatalog()
        book1 = Book(isbn="1234567890", publication_date=date(2023, 1, 1), title="Sample Title", author="Sample Author")
        book2 = Book(isbn="0987654321", publication_date=date(2023, 1, 1), title="Another Title", author="Another Author")
        catalog.add_book(book1)
        catalog.add_book(book2)
        result = catalog.get_books()
        self.assertEqual(result, [book1, book2])
        
    

if __name__ == "__main__":
    unittest.main()
class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books
    
    def search_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    # create a search book by title method
    def search_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
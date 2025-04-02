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
        return "book not found"
    # create a search book by author method
    def search_book_by_author(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
                
        return books if books else None
    # remove a book from the catalog using isbn number
    def remove_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return "book not found"
    # create a fuction to list all books in the catalog
    def list_books(self):
        if not self.books:
            return "No books in the catalog"
        return [str(book) for book in self.books]
    
    
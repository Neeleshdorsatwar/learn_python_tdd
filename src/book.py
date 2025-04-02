import re
class Book:
    def __init__(self, isbn, publication_date, title, author):
        is_valid = self.is_valid_isbn(isbn)
        if not is_valid:
            raise ValueError("Invalid ISBN number")
        self.isbn = isbn
        self.publication_date = publication_date
        self.title = title
        self.author = author
    
    def is_valid_isbn(self,isbn):
        # Regular expression for ISBN-10 or ISBN-13
        isbn_pattern = r"^(?:\d{9}X|\d{10}|\d{13})$"
        return bool(re.match(isbn_pattern, isbn))

        # create equals method
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn and self.publication_date == other.publication_date and self.title == other.title and self.author == other.author
        return False
    # create str method
    def __str__(self):
        return f"Book(ISBN: {self.isbn}, Publication Date: {self.publication_date}, Title: {self.title}, Author: {self.author})"
        
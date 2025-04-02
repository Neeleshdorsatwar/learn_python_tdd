class Book:
    def __init__(self, isbn, publication_date, title, author):
        self.isbn = isbn
        self.publication_date = publication_date
        self.title = title
        self.author = author

        # create equals method
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn and self.publication_date == other.publication_date and self.title == other.title and self.author == other.author
        return False
    # create str method
    def __str__(self):
        return f"Book(ISBN: {self.isbn}, Publication Date: {self.publication_date}, Title: {self.title}, Author: {self.author})"
        
# Assignment 2: BookCatalog System

## Objective

Design and implement a **BookCatalog** system using Object-Oriented Programming (OOP) principles. The system should manage a collection of books, allowing users to add, remove, and search for books in the catalog. Each book will have properties such as **title**, **author**, **ISBN**, and **year of publication**.

---

## Requirements

### Class Definitions

#### Book Class

Create a class named `Book` with the following attributes:

- **title** (string): The title of the book.
- **author** (string): The author of the book.
- **isbn** (string): The ISBN (International Standard Book Number) of the book.
- **publication_year** (integer): The year the book was published.

The class should include:

- A constructor to initialize these attributes.
- A method `__str__()` to return a string representation of the book in the format:

    ```
    Title: <title>, Author: <author>, ISBN: <isbn>, Year: <publication_year>
    ```

#### BookCatalog Class

Create a class named `BookCatalog` to represent the collection of books. This class should include:

- **books** (list): A list to store all the `Book` objects in the catalog.

The following methods should be implemented:

1. **`add_book(book)`**: Adds a `Book` object to the catalog.
2. **`remove_book(isbn)`**: Removes a book from the catalog using its ISBN. If the book is not found, print an error message.
3. **`search_by_title(title)`**: Searches for books with a given title and returns a list of matching books. If no book is found, return a message indicating so.
4. **`search_by_author(author)`**: Searches for books by a specific author and returns a list of matching books. If no book is found, return a message indicating so.
5. **`search_by_isbn(isbn)`**: Searches for a book by ISBN and returns the matching book. If no book is found, return a message indicating so.
6. **`list_all_books()`**: Returns a list of all books currently in the catalog.

---

### Input Validation

Ensure that the methods handle invalid inputs appropriately, such as:

- Trying to remove a book that doesn’t exist.
- Invalid ISBN format.

---

### Edge Case Handling

Handle edge cases like:

- Removing a book that’s not in the catalog.
- Searching with an empty catalog.

---

## Example Usage

```python
# Example usage:

# Create some book objects
book1 = Book("1984", "George Orwell", "978-0451524935", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925)

# Create a book catalog and add books to it
catalog = BookCatalog()
catalog.add_book(book1)
catalog.add_book(book2)
catalog.add_book(book3)

# List all books in the catalog
catalog.list_all_books()

# Search for books by title
catalog.search_by_title("1984")

# Search for books by author
catalog.search_by_author("Harper Lee")

# Search by ISBN
catalog.search_by_isbn("978-0451524935")

# Remove a book by ISBN
catalog.remove_book("978-0451524935")

# Try removing a non-existing book
catalog.remove_book("978-0000000000")

# List all books after removal
catalog.list_all_books()
```

---

## Constraints

- Each `Book` object must have a unique ISBN.
- The `BookCatalog` class should allow the storage of an arbitrary number of books.
- The catalog should efficiently handle searches by title, author, and ISBN.
- The catalog should allow modifications (addition and removal) and retrieval (search and listing) operations.

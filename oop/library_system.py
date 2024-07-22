# library_system.py

class Book:
    """Represents a general book."""

    def __init__(self, title, author):
        """Initializes a Book object."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Represents an eBook."""

    def __init__(self, title, author, file_size):
        """Initializes an EBook object."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Represents a physical print book."""

    def __init__(self, title, author, page_count):
        """Initializes a PrintBook object."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """Represents a library containing books."""

    def __init__(self):
        """Initializes a Library object with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of all books in the library."""
        for book in self.books:
            print(book)
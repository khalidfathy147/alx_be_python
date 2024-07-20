class Book:
    """Represents a book in a library."""

    def __init__(self, title, author):
        """Initializes a Book object."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Represents a library with a collection of books."""

    def __init__(self):
        """Initializes a Library object with an empty list of books."""
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """Adds a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Book '{title}' checked out successfully.")
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """Lists all available books in the library."""
        print("Available books:")
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
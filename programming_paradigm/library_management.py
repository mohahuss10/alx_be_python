class Book:
    """represents a book in the library system"""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False # private attribute

    def check_out(self):
        """marks the book as checked_out"""
        if self._is_checked_out :
            return False
        self._is_checked_out = True

        return True
    
    def return_book(self):
        """mark the book as returned"""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True
    def is_available (self):
        """checks if the book  is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """string represatation of the book"""
        return f"{self.title} by {self.author}"
    



class Library:
    """manages collection of books"""
    def __init__(self):
        """initializes an emopty library"""
        self._books = []

    def add_book(self, book):
        """add book to the library"""
        if isinstance(book, Book):
            self._books.append(book)
    
    def check_out_book(self, title):
        """check out a book by title"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
            
    def return_book(self, title):
        """return a book by title"""
        for book in self._books:
            if book.title == title and not  book.is_available():
                book.return_book()
                return True
        return False
    


    def list_available_books(self):
        """Print all available books"""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available")
        else:
            for book in available_books:
                print(book)
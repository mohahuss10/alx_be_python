class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """EBook with additional file size attributes"""
        super().__init__(title, author)  # call base constructor
        self.file_size = file_size # in mb

    def __str__(self):
        return f"Book:{self.title} by {self.author} , file size:{self.file_size}"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author) # call base constructor
        self.page_count = page_count

    
    def __str__(self):
        return f"PrintBook:{self.title}, by {self.author}, pzages:{self.page_count}"
    


class Library:
    def __init__(self):
        """Library containing a collection of books"""
        self.books = []

    def add_book(self,book):
        """add a book to the library"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("only Book instances can be added to the library")
        

    def list_books(self):
        """List all the books in the library"""
        for book in self.books:
            print(book)
class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's title, author, and year"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to indicate when a book instance is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Readable string representation for humans"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Unambiguous string representation for developers"""
        return f"Book({self.title!r}, {self.author!r}, {self.year!r})"

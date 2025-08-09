class Book:
    def __init__(self,title,author,year):
        """constructor to initialize the book's title, author and year"""
        self.title =  title
        self.autor = author
        self.year = year

    def __del__(self):
        """destructor to indicate when a book instance is deleted"""
        print(f"Deleting{self.title}")

    def __str__(self):
        """Readable string represantation for humans"""
        return f"{self.title} by {self.autor}, published in {self.year}"
    
    def __repr__(self):
        return f"Book ({self.title} by {self.autor}, published in {self.year})"

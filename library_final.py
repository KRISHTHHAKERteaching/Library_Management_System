# library_final.py

class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return f"{self.title} has been borrowed."
        return f"{self.title} is currently unavailable."

    def return_book(self):
        self.available = True
        return f"{self.title} has been returned."

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {'Available' if self.available else 'Borrowed'}"


# Sample usage
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(book1)
    print(book1.borrow())
    print(book1)
    print(book1.return_book())
    print(book1)

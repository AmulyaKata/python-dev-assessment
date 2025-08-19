# Book class implementation

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2025
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage
if __name__ == "__main__":
    book1 = Book("Atomic Habits", "James Clear", "9780735211292", 2018)
    book2 = Book("1984", "George Orwell", "9780451524935", 1949)

    for book in (book1, book2):
        print("Title:", book.title)
        print("Author:", book.author)
        print("Age:", book.get_age())
        print("Summary:", book.get_summary())
        print("-" * 40)
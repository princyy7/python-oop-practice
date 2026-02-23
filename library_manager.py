class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Added "{book.title}" to {self.name}')

    def show_books(self):
        print(f"\nBooks in {self.name}:")
        if len(self.books) == 0:
            print("No books available.")
            return
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    print(f'"{book.title}" is already issued.')
                else:
                    book.is_issued = True
                    print(f'You issued "{book.title}".')
                return
        print(f'Book "{title}" not found.')

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_issued:
                    print(f'"{book.title}" was not issued.')
                else:
                    book.is_issued = False
                    print(f'You returned "{book.title}".')
                return
        print(f'Book "{title}" not found.')

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    print(f'Cannot remove "{book.title}" because it is currently issued.')
                else:
                    self.books.remove(book)
                    print(f'"{book.title}" removed from library.')
                return
        print(f'Book "{title}" not found.')


# Test
lib = Library("City Library")

b1 = Book("Atomic Habits", "James Clear")
b2 = Book("Python Crash Course", "Eric Matthes")
b3 = Book("The Alchemist", "Paulo Coelho")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.show_books()
lib.issue_book("Atomic Habits")
lib.issue_book("Atomic Habits")
lib.show_books()
lib.return_book("Atomic Habits")
lib.show_books()

# remove_book tests
lib.issue_book("Python Crash Course")
lib.remove_book("Python Crash Course")   # should not remove (issued)
lib.return_book("Python Crash Course")
lib.remove_book("Python Crash Course")   # should remove
lib.remove_book("Unknown Book")          # not found
lib.show_books()


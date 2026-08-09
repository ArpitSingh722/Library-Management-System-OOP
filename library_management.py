class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.patron_id} | {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        book = Book(book_id, title, author)
        self.books[book_id] = book
        print("Book added successfully!")

    def register_patron(self):
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        if patron_id in self.patrons:
            print("Patron ID already exists!")
            return

        patron = Patron(patron_id, name)
        self.patrons[patron_id] = patron
        print("Patron registered successfully!")

    def borrow_book(self):
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        if patron_id not in self.patrons:
            print("Patron not found!")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if not book.is_available:
            print("Book is already borrowed!")
            return

        book.is_available = False
        patron.borrowed_books.append(book)

        print(f"Book '{book.title}' borrowed successfully by {patron.name}.")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        if patron_id not in self.patrons:
            print("Patron not found!")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book not in patron.borrowed_books:
            print("This patron has not borrowed this book!")
            return

        book.is_available = True
        patron.borrowed_books.remove(book)

        print(f"Book '{book.title}' returned successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n--- BOOKS ---")
        for book in self.books.values():
            print(book)

    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return

        print("\n--- PATRONS ---")
        for patron in self.patrons.values():
            print(patron)

    def display_borrowed_books(self):
        patron_id = input("Enter Patron ID: ")

        if patron_id not in self.patrons:
            print("Patron not found!")
            return

        patron = self.patrons[patron_id]

        print(f"\nBooks borrowed by {patron.name}:")

        if not patron.borrowed_books:
            print("No books borrowed.")
        else:
            for book in patron.borrowed_books:
                print(book)


def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Register Patron")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Display All Patrons")
        print("7. Display Borrowed Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.register_patron()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.display_books()
        elif choice == "6":
            library.display_patrons()
        elif choice == "7":
            library.display_borrowed_books()
        elif choice == "8":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

# Library Management System using OOP

A simple menu-driven Library Management System developed in Python using Object-Oriented Programming (OOP) principles.

## Features

- Add new books
- Register library patrons
- Borrow books
- Return books
- Display all books
- Display all registered patrons
- Display books borrowed by a patron
- Prevent borrowing an already borrowed book
- Validate book and patron IDs
- Interactive menu-driven input

## OOP Concepts Used

- Classes and Objects
- Encapsulation
- Constructors (`__init__`)
- Methods
- Object interaction
- Magic method (`__str__`)
- Dictionaries for storing books and patrons

## Project Structure

```text
Library-Management-System-OOP/
│
├── library_management.py
├── README.md
├── Library Management System using OOP.md
├── Sample Output.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

Open a terminal in the project folder and run:

```bash
python library_management.py
```

## How It Works

1. Select an option from the menu.
2. Add books by entering Book ID, title, and author.
3. Register patrons using a Patron ID and name.
4. Borrow a book by entering the Book ID and Patron ID.
5. Return a borrowed book using the same IDs.
6. Display library information whenever required.
7. Select `8` to exit.

## Example

```text
========== LIBRARY MANAGEMENT SYSTEM ==========
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display All Books
6. Display All Patrons
7. Display Borrowed Books
8. Exit

Enter your choice: 1
Enter Book ID: B101
Enter Book Title: Python Programming
Enter Author Name: John Smith
Book added successfully!
```

## Author
Arpit Singh

''' NAME:- HARSHITA GAIKWAD 

LIBRARY MANAGMENT SYSTEM'''


class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, quantity):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, quantity)
        self.books.append(new_book)
        print(f"Book added successfully. Book ID: {book_id}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book in self.books:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Quantity: {book.quantity}")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.quantity > 0:
                    book.quantity -= 1
                    print(f"Book borrowed successfully. Remaining quantity: {book.quantity}")
                else:
                    print("Sorry, the book is currently unavailable.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.quantity += 1
                print(f"Book returned successfully. Updated quantity: {book.quantity}")
                return
        print("Book not found.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            quantity = int(input("Enter the quantity: "))
            library.add_book(title, author, quantity)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_id = int(input("Enter the Book ID to borrow: "))
            library.borrow_book(book_id)

        elif choice == '4':
            book_id = int(input("Enter the Book ID to return: "))
            library.return_book(book_id)

        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

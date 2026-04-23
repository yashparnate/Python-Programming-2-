class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    # Display books
    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            print("Books in Library:")
            for book in self.books:
                print(book)

    # Issue a book
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully.")
        else:
            print("Book not available.")

    # Return a book
    def return_book(self, book):
        self.books.append(book)
        print("Book returned successfully.")

    # Search for a book
    def search_book(self, book):
        if book in self.books:
            print("Book is available in library.")
        else:
            print("Book not found.")


library = Library()

while True:
    print("\n----- Library Menu -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == 4:
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == 5:
        book = input("Enter book name to search: ")
        library.search_book(book)

    elif choice == 6:
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice")
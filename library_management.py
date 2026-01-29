class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True   # availability status

    def checkout_book(self):
        if self.available:
            self.available = False
            print(self.book_name, "has been checked out.")
        else:
            print(self.book_name, "is not available.")

    def return_book(self):
        self.available = True
        print(self.book_name, "has been returned.")

    def display_book(self):
        status = "Available" if self.available else "Not Available"
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)
        print("--------------------")


# Creating objects
book1 = Library("Python Basics", "Guido van Rossum")
book2 = Library("Data Structures", "Mark Allen Weiss")

# Display available books
book1.display_book()
book2.display_book()

# Checkout and return operations
book1.checkout_book()
book1.display_book()

book1.return_book()
book1.display_book()
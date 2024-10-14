# Book class written here. Gives book details and shows availability
class Book:
    def __init__ (self, title, author, isbn):
    #Title of book
        self.title = title
    #Author of book
        self.author = author
    #ISBN of book
        self.isbn = isbn
    #Availability of book
        self.availability_status = True
    def __str__(self):
        availability = self.availability_status
        if self.availability_status:
            print("Book is available")
        else:
            print("Book has been checked out")
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {availability}")




# Library class written here. Manages and stores a collection of books
class Library:
    def __init__(self):
        self.books = []
    #Adds a book to collection
    def add_books(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} has been added.")
    #Displays availability of books
    def displayAvailableBooks(self):
        if not self.books:
            print("No books found in Library.")
        else:
            for book in self.books:
                print(book)
    #Searches up book by title
    def searchBookTitle(self, title):
        for book in self.books:
            if book.title.lower()==title.lower():
                print(book)
            else:
                print("No books found or was spelled incorrectly.")

    #Checks out the book by using ISBN
    def check_out(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.availability_status:
                    book.availability_status = False
                    print(f"'{book.title}' has been checked out.")
                else:
                    print(f"'{book.title}' may not be avaible or is already checked out.")

    #Checks in the book using ISBN
    def check_in(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.availability_status:
                    book.availability_status = True
                    print(f"'{book.title}' has been checked in.")
                else:
                    print(f"'{book.title}' not found and was not checked out.")




# User interface used to interact with the library.
def main():
    library = Library()

# Displays options on menu screen.
    while True:
        print("Welcome to the Library Management System!")
        print("-Search for a book (Type search)")
        print("-Add a new book (Type add)")
        print("-Display Books (Type display)")
        print("-Check out (Type check out)")
        print("-Check in (Type check in)")
        print("-Exit")

        Option = input("Enter one of the options listed above: ")

        if Option == 'search':
            title = input("Enter the book title to search: ")
            library.searchBookTitle(title)

        elif Option == 'add':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the ISBN: ")
            book = Book(title, author, isbn)
            library.add_books(book)

        elif Option == 'display':
            library.displayAvailableBooks()


        elif Option == 'check out':
            isbn = input("Enter the book ISBN to check out: ")
            library.check_out(isbn)

        elif Option == 'check in':
            isbn = input("Enter the book ISBN to check in: ")
            library.check_in(isbn)

        elif Option == 'exit':
            print("You are now exiting the library management system.")
            break

        else:
            print("Invalid option. Please enter one of the given choices.")


# Runs the Library Management System
if __name__ == '__main__':
    main()
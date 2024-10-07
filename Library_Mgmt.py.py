class Library:
    # Constructor to initialize the book list, library name, and lending dictionary
    def __init__(self, booksList, name):
        self.booksList = booksList  # List of available books in the library
        self.name = name  # Name of the library
        self.lendDict = {}  # Dictionary to track which user has borrowed which book

    # Method to display all books in the library
    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        # Iterating through the list of books and displaying each one
        for book in self.booksList:
            print(book)

    # Method to add a new book to the library
    def addBook(self, book):
        # Check if the book already exists in the library
        if book in self.booksList:
            print("Book already exists")
        else:
            # Add the book to the list and append it to the database file
            self.booksList.append(book)
            with open(databaseName, "a") as bookDatabase:
                bookDatabase.write(book + "\n")  # Add new line after each book
            print("Book added to the library and the database")
    
    # Method to lend a book to a user
    def lendBook(self, book, user):
        # Check if the book is available in the library
        if book in self.booksList:
            # Check if the book is already lent to someone else
            if book not in self.lendDict.keys():
                # Add the book and the user's name to the lendDict
                self.lendDict.update({book: user})
                print(f"Book has been lent to {user}. Database updated.")
            else:
                # Inform the user that the book is already lent out
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            # Notify the user that the book is not available in the library
            print("Apologies! We don't have this book in our library")

    # Method to return a borrowed book to the library
    def returnBook(self, book):
        # Check if the book is in the lending dictionary
        if book in self.lendDict.keys():
            # Remove the book from the lending dictionary
            self.lendDict.pop(book)
            print("Book returned successfully and removed from lending database")
        else:
            # Notify the user if the book is not found in the lending database
            print("The book does not exist in the Book Lending Database")

# Main function to interact with the user and provide library options
def main():
    while(True):
        # Display welcome message and menu options
        print(f"Welcome to the {library.name} library. Following are the options:")
        choice = '''
        1. Display Books
        2. Lend a Book 
        3. Add a Book
        4. Return a Book
        '''
        print(choice)

        # Ask the user if they want to continue or quit
        userInput = input("Press Q to quit and C to continue: ").upper()
        if userInput == "C":
            # Ask the user to choose an option
            userChoice = int(input("Select an option to continue: "))
            
            # If user selects option 1, display books
            if userChoice == 1:
                library.displayBooks()
            
            # If user selects option 2, lend a book to the user
            elif userChoice == 2:
                book = input("Enter the name of the book you want to lend: ")
                user = input("Enter the name of the user: ")
                library.lendBook(book, user)
            
            # If user selects option 3, add a new book to the library
            elif userChoice == 3:
                book = input("Enter the name of the book you want to add: ")
                library.addBook(book)
            
            # If user selects option 4, return a book to the library
            elif userChoice == 4:
                book = input("Enter the name of the book you want to return: ")
                library.returnBook(book)

            else:
                # If the user enters an invalid option
                print("Please choose a valid option")

        elif userInput == "Q":
            # Exit the loop and terminate the program
            break

        else:
            # If the user enters an invalid input for continuation
            print("Please enter a valid option")

# Entry point of the program
if __name__ == '__main__':
    # Initialize an empty list to store the books from the database
    bookList = []
    
    # Ask the user for the name of the database file where books are stored
    databaseName = input("Enter the name of the database file with extension: ")
    
    # Open the book database file and read all books into the bookList
    with open(databaseName, 'r') as bookDatabase:
        for book in bookDatabase:
            bookList.append(book.strip())  # Remove any extra whitespace/newline characters
    
    # Create an instance of the Library class using the book list and library name
    library = Library(bookList, "PythonX")
    
    # Start the main function to interact with the user
    main()

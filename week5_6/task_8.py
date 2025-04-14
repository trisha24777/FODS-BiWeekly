import csv

class Book:
    """
    Represents a book in the library.
    """
    def __init__(self, book_id, title, author, is_available=True):
        """
        Initializes a Book object.
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    def get_details(self):
        """
        Returns the book details as a list.
        """
        return [self.book_id, self.title, self.author, self.is_available]

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        availability = "Available" if self.is_available else "Issued"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {availability}"

class Library:
    """
    Manages the collection of books in the library.
    """
    def __init__(self, filename="books.csv"):
        """
        Initializes the Library object and loads books from the CSV file.
        """
        self.filename = filename
        self.books = self._load_books()

    def _load_books(self):
        """
        Loads book data from the CSV file into a dictionary.
        """
        books = {}
        try:
            with open(self.filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader, None)  # Skip header row
                if header:
                    # Loop through the rows and create Book objects
                    for row in reader:
                        try:
                            book_id = int(row[0])  # Parse book ID as integer
                            title = row[1]
                            author = row[2]
                            is_available = row[3].lower() == 'true'  # Check availability status
                            books[book_id] = Book(book_id, title, author, is_available)  # Add to dictionary
                        except (ValueError, IndexError) as e:
                            print(f"Error reading book data: {row} - {e}")
        except FileNotFoundError:
            print(f"Warning: '{self.filename}' not found. A new file will be created.")
        except Exception as e:
            print(f"An error occurred while loading books: {e}")
        return books

    def _save_books(self):
        """
        Saves the book data to the CSV file.
        """
        try:
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["BookID", "Title", "Author", "IsAvailable"])  # Write header row
                # Write details of each book
                for book in self.books.values():
                    writer.writerow(book.get_details())
            print("Book data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving books: {e}")

    def add_book(self, book):
        """
        Adds a new book to the library and saves it to the file.
        """
        if book.book_id not in self.books:  # Ensure unique book ID
            self.books[book.book_id] = book
            self._save_books()  # Save the updated book data to file
            print(f"Book '{book.title}' added successfully.")
        else:
            print(f"Error: Book with ID '{book.book_id}' already exists.")

    def issue_book(self, book_id):
        """
        Issues a book (marks it as unavailable).
        """
        if book_id in self.books:
            if self.books[book_id].is_available:
                self.books[book_id].is_available = False  # Mark as issued
                self._save_books()  # Save changes
                print(f"Book '{self.books[book_id].title}' issued successfully.")
            else:
                print(f"Error: Book with ID '{book_id}' is already issued.")
        else:
            print(f"Error: Book with ID '{book_id}' not found.")

    def return_book(self, book_id):
        """
        Returns a book (marks it as available).
        """
        if book_id in self.books:
            if not self.books[book_id].is_available:
                self.books[book_id].is_available = True  # Mark as available
                self._save_books()  # Save changes
                print(f"Book '{self.books[book_id].title}' returned successfully.")
            else:
                print(f"Error: Book with ID '{book_id}' is already available.")
        else:
            print(f"Error: Book with ID '{book_id}' not found.")

    def search_book(self, search_term):
        """
        Searches for books by title or author and displays results.
        """
        results = []
        search_term = search_term.lower()  # Convert search term to lowercase for case-insensitive comparison
        # Loop through books and find matching books
        for book in self.books.values():
            if search_term in book.title.lower() or search_term in book.author.lower():
                results.append(book)

        if results:
            print("\nSearch Results:")
            # Print the details of each matched book
            for book in results:
                print(book)
        else:
            print(f"No books found matching '{search_term}'.")

def main():
    """
    Main function to run the library management system.
    """
    library = Library()  # Initialize the Library object

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            # Handle user input for each option
            if choice == '1':
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Book Author: ")
                new_book = Book(book_id, title, author)  # Create a new Book object
                library.add_book(new_book)
            elif choice == '2':
                book_id = int(input("Enter Book ID to issue: "))
                library.issue_book(book_id)  # Issue the selected book
            elif choice == '3':
                book_id = int(input("Enter Book ID to return: "))
                library.return_book(book_id)  # Return the selected book
            elif choice == '4':
                search_term = input("Enter title or author to search: ")
                library.search_book(search_term)  # Search for books
            elif choice == '5':
                print("Exiting the library management system.")
                break  # Exit the system
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for Book ID.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()  # Run the library management system

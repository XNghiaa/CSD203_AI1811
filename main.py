from AddBook import add_book
from ViewBooks import view_books
from DeleteBook import delete_book
from BorrowedBook import borrow_book
from ReturnBook import return_book

def display_menu():
    print("===== Library Management System Menu =====")
    print("1. Add a book")
    print("2. View all books")
    print("3. Delete a book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Exit")

def main():
    books_list = LinkedList()
    borrowed_list = LinkedList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books_list)
        elif choice == '2':
            view_books(books_list)
        elif choice == '3':
            bid = input("Enter the book ID to delete: ")
            delete_book(books_list, bid)
        elif choice == '4':
            bid = input("Enter the book ID to borrow: ")
            borrow_book(books_list, borrowed_list, bid)
        elif choice == '5':
            bid = input("Enter the book ID to return: ")
            return_book(books_list, borrowed_list, bid)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

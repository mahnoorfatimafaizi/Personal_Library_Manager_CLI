library = []

def menu():
    print("\n📚 Personal Library Manager")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. Display All Books")
    print("5. Display Statistics")
    print("6. Exit")


def add_book():
    """Function to add a book to the library"""
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()

    while True:
        try:
            year = int(input("Enter the year of publication: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    genre = input("Enter the genre of the book: ").strip()

    while True:
        read_status = input("Have you read the book? (yes/no): ").strip().lower()
        if read_status in ["yes", "no"]:
            break
        else: 
            print("Invalid input. Please enter 'yes' or 'no'.")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status == "yes"  
    }

    library.append(book)
    print(f"\n✅ '{title}' by {author} added successfully!\n")


def remove_book():
    """Function to remove a book from the library"""
    title = input("Enter the title of the book you want to remove: ").strip().lower()

    for book in library:
        if book["title"].lower() == title:  
            library.remove(book)
            print(f"\n✅ '{book['title']}' removed successfully!\n")
            return
    
    print(f"\n❌ '{title}' not found in the library.\n")


def search_book():
    """Function to search for a book by title or author."""
    print("\n🔎 Search for a Book")
    search_type = input("Search by (title/author)?: ").strip().lower()

    if search_type not in ["title", "author"]:
        print("\n❌ Invalid choice. Please enter 'title' or 'author'.")
        return  # Exit the function if input is invalid

    search_query = input(f"Enter the {search_type}: ").strip().lower()

    # Search for matching books
    found_books = [
        book for book in library if search_query == book[search_type].strip().lower()
    ]

    if found_books:
        print("\n📖 Matching Books:")
        for book in found_books:
            print(f"📌 Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")
    else:
        print(f"\n❌ No books found for '{search_query}'.")

def display_books():
    """Function to display all books in the library"""
    print("\n📚 All Books:")
    if not library:
        print("\n❌No books in the library.")
        return
    print("\n📚 Library Collection:")
    for book in library:
        print(f"📌 Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")

def display_statistics():
    """Function to display statistics of the library"""
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"])
    unread_books = total_books - read_books

    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"✅ Read: {read_books} | ❌ Unread: {unread_books}")


while True:
    menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_book() 
    elif choice == "2":
        remove_book()  
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        print("\nExiting program. Goodbye! 👋")
        break
    else:
        print("\nInvalid choice. Please try again.")


            
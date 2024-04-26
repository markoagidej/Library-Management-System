
import os
import book
import user
import author
import genre

def load_file(filename):
    if os.path.exists(f"\\Files\\{filename}"):
        try:
            with open(f"\\Files\\{filename}", "r") as file:
                if filename == "books.txt":
                    book_dict = {}
                    for line in file:
                        title = 
                        author = 
                        ISBN = 
                        genre = 
                        publication_date = 
                        book.book_collection_add(book_dict, title, author, ISBN, genre, publication_date)
                        return book_dict
                elif filename == "user.txt":
                    user_dict = {}
                    return user_dict
                elif filename == "authors.txt":
                    authors_dict = []
                    return authors_dict
                elif filename == "genres.txt":
                    user_dict = {}
                    return user_dict
        except:
            print(f"File error for \'{filename}\'")
    else:
        try:
            with open(f"\\Files\\{filename}", "w") as file:
                pass
        except:
            print(f"Path issue for \'\\Files\\{filename}\'")

        if filename == "books.txt":
            return {}
        elif filename == "users.txt":
            return {}
        elif filename == "authors.txt":
            return []
        elif filename == "genres.txt":
            return set()

def main():
    book_collection = load_file("books.txt") # {ISBN : Book}
    user_collection = load_file("users.txt") # {UUID : User}
    author_collection = load_file("authors.txt") # [Author]
    genre_collection = load_file("genres.txt") # (Genre)

    while True:
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        try:
            choice = int(input())
        except ValueError:
            print("Only enter a number 1-5")
            continue

        if choice == 1:
            menu_book_ops()
        elif choice == 2:
            menu_user_ops()
        elif choice == 3:
            menu_author_ops()
        elif choice == 4:
            menu_genre_ops()
        elif choice == 5:
            print("Thank you, goodbye!")
            exit()

def menu_book_ops():
    while True:
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Borrow/Reserve a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")

        try:
            choice = int(input())
        except ValueError:
            print("Only enter a number 1-5")
            continue

        if choice == 1:
            title = 
            author = 
            ISBN = 
            genre = 
            publication_date = 
            book_collection = book.book_collection_add(book_collection, title, author, ISBN, genre, publication_date)
        elif choice == 2:
            book_borrow()
        elif choice == 3:
            book_return()
        elif choice == 4:
            book_search()
        elif choice == 5:
            book_disaply_all()

def menu_user_ops():
    while True:
        print("User Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")

        try:
            choice = int(input())
        except ValueError:
            print("Only enter a number 1-3")
            continue

        if choice == 1:
            user_add()
        elif choice == 2:
            user_view_details()
        elif choice == 3:
            user_display_all()

def menu_author_ops():
    while True:
        print("Author Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")

        try:
            choice = int(input())
        except ValueError:
            print("Only enter a number 1-3")
            continue

        if choice == 1:
            author_add()
        elif choice == 2:
            author_view_details()
        elif choice == 3:
            author_display_all()

def menu_genre_ops():
    while True:
        print("Genre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")

        try:
            choice = int(input())
        except ValueError:
            print("Only enter a number 1-3")
            continue

        if choice == 1:
            genre_add()
        elif choice == 2:
            genre_view_details()
        elif choice == 3:
            genre_display_all()


if __name__ == "__main__":
    main()
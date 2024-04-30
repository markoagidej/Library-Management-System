
import os
import re
import book
import user
import author
import genre

book_collection = {} # {ISBN : Book}
user_collection = {} # {UUID : User}
author_collection = [] # [Author]
genre_collection = set() # (Genre)
text_deliniator = "|"

def load_file(filename):
    if os.path.exists(f"Files\\{filename}"):
        # try:
        with open(f"Files\\{filename}", "r") as file:
            if filename == "books.txt":
                book_dict = {}
                for line in file:
                    title, author, ISBN, genre, publication_date, available, res_list = line.split(text_deliniator)
                    match = re.search("\\[(.*)\\]", res_list)
                    if match.group(1):
                        res_list_parsed = match.group(1).split(",")
                    else:
                        res_list_parsed = []
                    book_dict = book.book_collection_add(title, author, ISBN, genre, publication_date, book_dict, bool(available), res_list_parsed)
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
        # except:
        #     print(f"File error for \'{filename}\'")
    else:
        try:
            with open(f"Files\\{filename}", "w") as file:
                pass
        except:
            print(f"Path issue for \'Files\\{filename}\'")

        if filename == "books.txt":
            return {}
        elif filename == "users.txt":
            return {}
        elif filename == "authors.txt":
            return []
        elif filename == "genres.txt":
            return set()

def save_books_file():
    global book_collection
    with open(f"Files\\books.txt", 'w') as file:
        for book in book_collection.values():
            # title = str(book.get_title)
            # author = str(book.get_author)
            # ISBN = str(book.get_ISBN)
            # genre = str(book.get_genre)
            # pub_date = str(book.get_publication_date)
            # available = str(book.available)
            # res_list = str(book.reserve_list)
            title = book.title
            author = book.author
            ISBN = book.ISBN
            genre = book.genre
            pub_date = book.publication_date
            available = str(book.available)
            res_list = "[" + ",".join(book.reserve_list) + "]"
            info_list = [title, author, ISBN, genre, pub_date, available, res_list]
            final_line = "|".join(info_list)
            file.write(final_line)
            
def save_users_file():
    global user_collection
    with open(f"Files\\users.txt", "w") as file:
        for user in user_collection:
            file.write(text_deliniator.join(user.get_name, user.get_UUID, user.get_borrow_history))

def main():
    global book_collection
    global user_collection
    global author_collection
    global genre_collection
    book_collection = load_file("books.txt")
    user_collection = load_file("users.txt")
    author_collection = load_file("authors.txt")
    genre_collection = load_file("genres.txt")

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
    global book_collection
    global user_collection
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

        if choice == 1: #  Add a new book
            print("Adding a new book to the library!")
            title = input("Enter the title for the new book: ")
            author = input("Enter the author for the new book: ")
            ISBN = input("Enter the ISBN for the new book: ")
            genre = input("Enter the genre for the new book: ")
            publication_date = input("Enter the publication date for the new book: ")
            book_collection = book.book_collection_add(title, author, ISBN, genre, publication_date, book_collection)
            save_books_file()
            break
        elif choice == 2: # Borrow/Reserve a book
            userID = input("Enter the user ID who would like to borrow a book: ")
            try:
                user_to_borrow = user_collection[userID]
            except KeyError:
                print("No user found with that ID!")
                continue

            ISBN = input("Enter the ISBN of the book you wish to borrow: ")
            try:
                book_to_borrow = book_collection[ISBN]
            except KeyError:
                print("No book found with that ISBN!")
                continue
            
            book_collection[ISBN] = book_to_borrow.borrow_book(user_to_borrow)
            if not book_collection[ISBN].reserve_list:
                user_collection[userID] = user_collection[userID].add_to_borrow_history(book_collection[ISBN])
            save_books_file()
            save_users_file()
            break
        elif choice == 3: # Return a book
            book_returned_ISBN = input("Enter the ISBN of the book to return: ")
            try:
                book_to_return = book_collection[book_returned_ISBN]
            except KeyError:
                print("No book found with that ISBN!")
                continue

            book_collection[book_returned_ISBN], next_reserved_user = book_to_return.return_book()
            if next_reserved_user:
                book_collection[book_returned_ISBN] = book_collection[book_returned_ISBN].borrow_book(next_reserved_user)
            save_books_file()
            save_users_file()
            break
        elif choice == 4: # Search for a book
            search = input("Enter part of the title of the book you would like to search: ")
            search_lower = search.lower()
            print(f"Here are all the books with {search} in the title:")
            book_counter = 0
            for book in book_collection.values():
                if search_lower in book.title.lower():
                    book_counter += 1
                    print(f"{book.title}, {book.author}, {book.ISBN}, {book.genre}, {book.publication_date}, {book.available}, {book.reserve_list}")
            if book_counter == 0:
                print(f"No books found with {search} in the title!")                    
            break
        elif choice == 5: # Display all books
            for book in book_collection.values():
                print(f"{book.title}, {book.author}, {book.ISBN}, {book.genre}, {book.publication_date}, {book.available}, {book.reserve_list}")
            break

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

        if choice == 1: # Add a new user
            pass
        elif choice == 2: # View user details
            pass
        elif choice == 3: # Display all users
            pass

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

        if choice == 1: # Add a new author
            pass
        elif choice == 2: # View author details
            pass
        elif choice == 3: # Display all authors
            pass

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

        if choice == 1: # Add a new genre
            pass
        elif choice == 2: # View genre details
            pass
        elif choice == 3: # Display all genres
            for genre in genre_collection:
                pass



if __name__ == "__main__":
    main()
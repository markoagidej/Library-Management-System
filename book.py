
class Book:
    def __init__(self, title, author, ISBN, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__genre = genre
        self.__publication_date = publication_date
        self.available = True
        self.reserve_list = []

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_ISBN(self):
        return self.__ISBN

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date
    
    def borrow_book(self, user_ID):
        if self.available:
            self.available = False
        else:
            choice = input("Would you like to be put on the reserve list for this book? (y/n)")
            if choice == "y":
                self.reserve_list.append(user_ID)
        return self

    def return_book(self):
        if self.reserve_list:
            new_borrower = self.reserve_list.pop(0)
        else:
            new_borrower = ""
            self.available = True
        return self, new_borrower

def book_collection_add(collection, title, author, ISBN, genre, publication_date):
    new_book = Book(title, author, ISBN, genre, publication_date)
    collection[ISBN] = new_book
    return collection
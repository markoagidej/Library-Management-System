
class Book:
    def __init__(self, title, author, ISBN, genre, publication_date, available = True, reserve_list = []):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.publication_date = publication_date
        self.available = available
        self.reserve_list = reserve_list

        # self.__title = title
        # self.__author = author
        # self.__ISBN = ISBN
        # self.__genre = genre
        # self.__publication_date = publication_date
        # self.__available = available
        # self.__reserve_list = reserve_list

    # def get_title(self):
    #     return self.__title

    # def get_author(self):
    #     return self.__author

    # def get_ISBN(self):
    #     return self.__ISBN

    # def get_genre(self):
    #     return self.__genre

    # def get_publication_date(self):
    #     return self.__publication_date
    
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
            next_reserved_user = self.reserve_list.pop(0)
        else:
            next_reserved_user = ""
        self.available = True
        return self, next_reserved_user

def book_collection_add(title, author, ISBN, genre, publication_date, collection = {}, available = True, res_list = []):
    new_book = Book(title, author, ISBN, genre, publication_date, available, res_list)
    if collection:
        collection[ISBN] = new_book
    else:
        collection = {ISBN: new_book}
    return collection
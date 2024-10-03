

class Book ():

    # Encapsulation
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True  # initially, book is available
    

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def is_available(self):
        return self.__is_available

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"{self.__title} has been borrowed.")

    def return_book(self):
        self.__is_available = True
        print(f"{self.__title} has been returned.")
        
    def get_status(self):
        return f"'{self.__title}' by {self.__author} (ISBN: {self.__isbn}) - {'Available' if self.__is_available else 'Not Available'}"    
            

class Library():

    def __init__(self) -> None:
        self.books = []

    def add_book(self, book:Book):
        self.books.append(book)
        print(f'{book.get_title()} was added in the library.')

    def get_books_status(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book.get_status())

# Abstraction
class User ():
    
    def __init__(self,name) -> None:
        self.name = name
        self.borrowed_books = []

    def get_borrowed_books(self):
        return [book.get_title() for book in self.borrowed_books]

    def borrow_book(book):
        raise NotImplementedError("This method should be overridden in subclasses")

    def return_book(self,book:Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{book.get_title()} not borrowed by {self.name}.")

# Inheritane
class Student(User):

    def __init__(self,name) -> None:
        super().__init__(name)
        self.__borrow_limit = 5
    
    # Override
    def borrow_book(self,book:Book):
        if len(self.borrowed_books) < self.__borrow_limit:
            if book.is_available():
                book.borrow_book()
                self.borrowed_books.append(book)
            else:
                print(f'{book.get_title()} is not available')
        else:
            print(f"Student {self.name} has reached the borrowing limit.")

# Inheritane
class Teacher(User):
    
    def __init__(self, name) -> None:
        
        super().__init__(name)
        self.__borrow_limit = 10

    # Override
    def borrow_book(self,book:Book):
        if len(self.borrowed_books) < self.__borrow_limit:
            if book.is_available():
                book.borrow_book()
                self.borrowed_books.append(book)
            else:
                print(f'{book.get_title()} is not available')
        else:
            print(f"Teacher {self.name} has reached the borrowing limit.")

class Admin(User):
    def __init__(self, name, library:Library) -> None:
        super().__init__(name)
        self.__library = library
    
    def view_all_books(self):
        print(f"Admin {self.name} is viewing all books in the library:")
        self.__library.get_books_status()


book1 = Book("1984", "George Orwell", "123-456")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "789-101")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "111-222")

library = Library()

print("-------------------- Add Book --------------------")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
print("-"*50)

print("------------------- Admin View -------------------")
a_bob = Admin("Bob",library)
a_bob.view_all_books()
print("-"*50)

print("------------------ Borrow Book ------------------")
t_smith = Teacher("Smith")
t_smith.borrow_book(book1)
t_smith.borrow_book(book2)
print("-"*50)

print("------------------- Admin View -------------------")
a_bob = Admin("Bob",library)
a_bob.view_all_books()
print("-"*50)
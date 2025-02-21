#Project: Library Management System

# fruits = ["orange","banana","grapes","strawberry"]

#can you use a loop to show the number of fruits with a serial number?

# 1. orange
# 2. banana

# counter = 1

# for i in fruits:
#     print(counter,i)
#     counter +=1

# #enumerate function 

# for i,fruit in enumerate(fruits,start =1):
#     print(i,fruit)

class Author:
    def __init__(self,name):
        self.name = name

class Book:
    def __init__(self,title,author):
        self.title = title 
        self.author = author 
        self.is_borrowed = False # is borrowed? False

    def borrowing(self):
        if not self.is_borrowed: # Checks if the book isnt borrowed
            self.is_borrowed = True # is borrowed? Yes
            return True # Success
        return False # Wasn't a success, the book is already borrowed
    def returning(self):
        if self.is_borrowed: # checks if the book is currently borrowed
            self.is_borrowed = False # is borrowed? not anymore!
            return True # Success
        return False # Wasn't a success, the book isn't borrowed so you can't return it
    

class Library:
    def __init__(self):
        self.books = [
            Book("Matilda",Author("Roald Dahl")),
            Book("Restart", Author("Gordon Korman")),
            Book("Tumtum & Nutmeg: Adventures Beyond Nutmouse Hall ",Author("Emily Bearn")),
            Book("Hatchet", Author("Gary Paulsen")),
            Book("Fish in a Tree", Author("Linda Mullaly Hunt"))
        ]
    def addbook(self, book):
        self.books.append(Book(book.title, Author(book.author)))
    def display_books(self):
        for i, book in enumerate(self.books):
            if not book.is_borrowed:
                Status = "Available"
            else:
                Status = "Borrowed"
            print(f"{i+1}. {book.title} by {book.author.name} -- {Status}")
    def borrow_book(self, book_number):
        book_number -= 1
        if 0 < book_number < len(self.books):
            if not self.books[book_number].is_borrowed:
                print(f"You have borrowed {self.books[book_number].title} by {self.books[book_number].author.name}")
                return True
            else:
                print(f"Sorry, {self.books[book_number].title} is already borrowed")
                return False
        else:
            print("Invalid book number")
            return False
    def return_book(self, book_number):
        if book_number < 0 or book_number >= len(self.books):
            print("Invalid book number")
            return False
        else:
            if self.books[book_number].is_borrowed:
                print(f"You have returned {self.books[book_number].title} by {self.books[book_number].author.name}")
                return True
            else:
                print(f"Sorry, {self.books[book_number].title} is not borrowed")
                return False
library = Library()
library.borrow_book(5)
while True:
    input = input("Choose the following:\n 1. Display Books (1)\n")
    if input == "1":
        print("Here are the status of all books:")
        library.display_books()
        input = input()

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
        if not self.is_borrowed:
            self.is_borrowed = True # is borrowed? Yes
            return True
        return False



class Library:
    def __init__(self):
        self.books = [
            Book("Matilda",Author("Roald Dahl")),
            Book("Restart", Author("Gordon Korman")),
            Book("Tumtum & Nutmeg: Adventures Beyond Nutmouse Hall ",Author("Emily Bearn")),
            Book("Hatchet", Author("Gary Paulsen")),
            Book("Fish in a Tree", Author("Linda Mullaly Hunt"))
        ]
    def addbook(self, Book):
        self.books.append(Book)
        
book1 = Book("Matlida","Roald Dahl") 

print(book1.borrowing())
print(book1.borrowing())
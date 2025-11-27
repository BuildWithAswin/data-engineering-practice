class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_borrowed = False

    def __str__(self):
        return (f"{self.title} , {self.author} , {self.ISBN}")



book1 = Book("Rich Dad Poor Dad", "Robert T Kiyosaki", "I245")
book2 = Book("Lean In", "Sheryl Sanderberg", "3456")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        #print(f"Added {book}")
    
    def show_books(self):
        if not self.books:
            print ("There are no books in the library")
        else:
            for b in self.books:
                print (b)
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:                #“If the book is currently  borrowed, then set to borrow it now.”
                    book.is_borrowed = True
                    print(f"You have borrowed the book: {book.title}")
                    return
                else: 
                    print(f"{book.title} is already borrowed..!")
                    return
        print(f"{title} not found in the library!")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:                
                    book.is_borrowed = False
                    print(f"You have successfully returned the title {title}")
                    return
                else:
                    print(f"Seems you have not borrowed this book..!")
        print(f"{title} not found in library..!")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.show_books()

library.borrow_book("Lean in")
library.borrow_book("Lean in")
library.return_book("Lean in")
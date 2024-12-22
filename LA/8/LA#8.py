print("LA#8")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("JuJutsu Kaisen", "Gege Akutami")
print(book1.title,book1.author)

del book1.author

#print(book1.title,book1.author)

print(book2.title,book2.author)

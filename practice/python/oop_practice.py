class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def show_info(self):
        print(f"{self.title} {self.author} {self.price}")
    def discount(self,rate):
        self.price=self.price*rate

book = Book("Python基础", "Tom", 100)

book.show_info()

book.discount(0.8)

book.show_info()
class EBook(Book):
    def __init__(self, title, author, price,file_size):
        super().__init__(title,author,price)
        self.file_size=file_size
    def show_info(self):
        print(f"{self.title} {self.author} {self.price} {self.file_size}MB")
    



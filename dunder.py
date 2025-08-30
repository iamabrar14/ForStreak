class Book:
    def __init__(self,title,page):
        self.title=title
        self.page=page
    def __str__(self): #Magic Method
        return f"Name of the book {self.title} and it has {self.page} pages"
    def __len__(self):
        return self.page
b=Book("Python OOP",350)
print(b) #calls str
print(len(b)) #calls __len__
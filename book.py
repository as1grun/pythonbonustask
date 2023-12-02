class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# Создание экземпляров класса Book
book1 = Book("Title1", "Author1", "ISBN1")
book2 = Book("Title2", "Author2", "ISBN2")

# Вывод информации о каждой книге
print(f"Book 1: {book1.title}, {book1.author}, {book1.isbn}")
print(f"Book 2: {book2.title}, {book2.author}, {book2.isbn}")

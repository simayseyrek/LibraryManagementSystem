class Book:
    def __init__(self, name, author, publish_year, category, page_number):
        self.name = name
        self.author = author
        self.publish_year = publish_year
        self.category = category
        self.page_number = page_number

    def __str__(self):
        return "Book Name: {}\nAuthor: {}\nPublish Year: {}\nCategory: {}\nPage Number: {}\n".format(
            self.name, self.author, self.publish_year, self.category, self.page_number)

    def book_fcn(self):
        book1 = Book("kavuşamayanlar", "simay seyrek", "2020", "dram", 90)  #TODO: reach books from database
        print(book1.publish_year)
        print(book1.author)
        print(book1.name)
        print(book1.category)
        print(book1.page_number)
        print(book1)
        print(book1.str)
        print(book1.repr())
class Book:
    def __init__(self, isbn, title, author, publish_year, category, page_number):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.category = category
        self.page_number = page_number
     
    def __str__(self):
        return "Book ISBN: {}\nBook Title: {}\nAuthor: {}\nPublish Year: {}\nCategory: {}\nPage Number: {}\n".format(
            self.isbn, self.title, self.author, self.publish_year, self.category, self.page_number)

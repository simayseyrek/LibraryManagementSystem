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

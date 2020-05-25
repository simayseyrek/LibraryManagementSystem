import mysql.connector


class Library_DB:
    def __init__(self):
      # connect to database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="bunebe01"
        )

        self.mycursor = self.mydb.cursor()

        # create db if not exists
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS Library")
        # using library db
        self.mycursor.execute('use Library')
        # create book table
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS books (isbn INT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), publish_year INT, category VARCHAR(255), page_number INT)")
        # create user table
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), level INT)")

    def add_book(self, book):
        # func addBook
        sql = "INSERT INTO books (isbn, title, author, publish_year, category, page_number) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (book.isbn, book.title, book.author, book.publish_year, book.category, book.page_number)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
           
    def get_all_books(self):
        # show all books from database
        self.mycursor.execute("SELECT * FROM books")

        return self.mycursor.fetchall()


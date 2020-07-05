import mysql.connector
import hashlib


class Library:
    def __init__(self):
      # connect to database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="bunebe01"
        )
        self.db_name = "Library1234"
        self.cursor = self.mydb.cursor()

        # create db if not exists
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.db_name) 
        # using library db
        self.cursor.execute('use ' + self.db_name)
        
        # create users table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), level INT)")
        # create books table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (isbn INT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), publish_year INT, category VARCHAR(255), page_number INT, total_number INT, available_number INT)")
        # create settings table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS settings (number INT PRIMARY KEY AUTO_INCREMENT, student_book_limit INT, student_book_time INT)")
        # create checkouts table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS checkouts (number INT PRIMARY KEY AUTO_INCREMENT, id INT, isbn INT, date VARCHAR(255))")
        # create checkin_approvals table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS checkin_approvals (number INT PRIMARY KEY AUTO_INCREMENT, id INT, isbn INT)")
        # create teacher_approvals table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS teacher_approvals (number INT PRIMARY KEY AUTO_INCREMENT, id INT)")

    def add_book(self, isbn, title, author, publish_year, category, page_number):
        try:
            sql = "SELECT * FROM books WHERE isbn = {}".format(isbn)
            self.cursor.execute(sql)
            books = self.cursor.fetchall()
            if len(books) == 0:
                total_number = 1
                available_number = 1
                sql = "INSERT INTO books (isbn, title, author, publish_year, category, page_number, total_number, available_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (isbn, title, author, publish_year, category, page_number, total_number, available_number)
                self.cursor.execute(sql, val)
                self.mydb.commit()
            else:
                total_number = books[0][6] + 1
                available_number = books[0][7] + 1
                sql = "UPDATE books SET total_number = {}, available_number = {} WHERE isbn = {}".format(total_number, available_number, isbn)
                self.cursor.execute(sql)
                self.mydb.commit()
        except:
            return False
        return True

    def add_user(self, id, name, email, password, level):
        hash_password = self.hash_password(password)
        try:
            sql = "INSERT INTO users (id, name, email, password, level) VALUES (%s, %s, %s, %s, %s)"
            val = (id, name, email, hash_password, level)
            self.cursor.execute(sql, val)
            self.mydb.commit()
        except:
            return False
        return True

    def add_teacher_approval(self, id):
        try:
            sql = "INSERT INTO teacher_approvals (number, id) VALUES (DEFAULT, {})".format(id)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

    def get_teacher_approval(self):
        self.cursor.execute("SELECT * FROM teacher_approvals")
        return self.cursor.fetchall()

    def approve_teacher_approval(self, id):
        try:
            sql = "UPDATE users SET level = 2 WHERE id = {}".format(id)
            self.cursor.execute(sql)
            self.mydb.commit()
            sql = "DELETE FROM teacher_approvals WHERE id = {}".format(id)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

    def reject_teacher_approval(self, id):
        try:
            sql = "DELETE FROM teacher_approvals WHERE id = {}".format(id)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

    @staticmethod
    def hash_password(password):
        encoded_password = password.encode('utf-8')
        hash = hashlib.sha256(encoded_password)
        return hash.hexdigest()

    def login(self, input, password):
        # check if input is id or email
        if input.isnumeric():
            sql = "SELECT * FROM users WHERE id = {}".format(input)
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            if len(user) == 0:
                return False
        else:
            sql = "SELECT * FROM users WHERE email = '{}'".format(input)
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            if len(user) == 0:
                return False

        # check password
        actual_password = user[0][3]
        verify_password = self.hash_password(password)
        if actual_password == verify_password:
            return True
        return False

    def search_book(self, ):
    def get_all_books(self):
        # show all books from database
        self.cursor.execute("SELECT * FROM books")

        return self.cursor.fetchall()

    def get_all_users(self):
        # show all users from database
        self.cursor.execute("SELECT * FROM users")

        return self.cursor.fetchall()

    def is_exist_book(self, book):
        # ....
        pass

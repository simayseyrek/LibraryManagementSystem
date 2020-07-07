import mysql.connector
import hashlib
import time


class Library:
    def __init__(self):
      # connect to database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="bunebe01"
        )
        self.db_name = "Library6"
        self.cursor = self.mydb.cursor()

        # create db if not exists
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.db_name) 
        # using library db
        self.cursor.execute('use ' + self.db_name)
        
        # create users table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), level INT)")
        # create books table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (isbn INT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), publish_year INT, category VARCHAR(255), page_number INT, total_number INT, available_number INT)")
        # create checkouts table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS checkouts (number INT PRIMARY KEY AUTO_INCREMENT, id INT, isbn INT, date VARCHAR(255))")
        # create checkin_approvals table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS checkin_approvals (number INT PRIMARY KEY AUTO_INCREMENT, id INT, isbn INT)")
        # create teacher_approvals table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS teacher_approvals (number INT PRIMARY KEY AUTO_INCREMENT, id INT)")
        # create settings table and insert default values
        self.cursor.execute("CREATE TABLE IF NOT EXISTS settings (number INT PRIMARY KEY AUTO_INCREMENT, student_book_limit INT, student_book_time INT)")
        sql = "INSERT IGNORE INTO settings VALUES (1, 2, 7)".format(id)
        self.cursor.execute(sql)
        self.mydb.commit()

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
                return False, 0
        else:
            sql = "SELECT * FROM users WHERE email = '{}'".format(input)
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            if len(user) == 0:
                return False, 0

        # check password
        actual_password = user[0][3]
        verify_password = self.hash_password(password)
        if actual_password == verify_password:
            return True, user[0][0]
        return False, 0

    def search_book(self, isbn=None, title=None, author=None, category=None, show_only_available=True):
        if isbn is not None:
            sql = "SELECT * FROM books WHERE isbn LIKE '%{}%'".format(isbn)
        elif title is not None and author is not None and category is not None:
            sql = "SELECT * FROM books WHERE title LIKE '%{}%' AND author LIKE '%{}%' AND category LIKE '%{}%'".format(title, author, category)
        elif title is not None and author is not None:
            sql = "SELECT * FROM books WHERE title LIKE '%{}%' AND author LIKE '%{}%'".format(title, author)
        elif title is not None and category is not None:
            sql = "SELECT * FROM books WHERE title LIKE '%{}%' AND category LIKE '%{}%'".format(title, category)
        elif author is not None and category is not None:
            sql = "SELECT * FROM books WHERE author LIKE '%{}%' AND category LIKE '%{}%'".format(author, category)
        elif title is not None:
            sql = "SELECT * FROM books WHERE title LIKE '%{}%'".format(title)
        elif author is not None:
            sql = "SELECT * FROM books WHERE author LIKE '%{}%'".format(author)
        elif category is not None:
            sql = "SELECT * FROM books WHERE category LIKE '%{}%'".format(category)
        self.cursor.execute(sql)
        books = self.cursor.fetchall()

        if show_only_available is False:
            for book in books[:]:
                if book[7] == 0:
                    books.remove(book)
        return books

    def get_student_book_limit(self):
        self.cursor.execute("SELECT * FROM settings")
        return self.cursor.fetchall()[0][1]

    def get_student_book_time(self):
        self.cursor.execute("SELECT * FROM settings")
        return self.cursor.fetchall()[0][2]

    def set_student_book_limit(self, student_book_limit):
        self.cursor.execute("UPDATE settings SET student_book_limit = {} WHERE number = 1".format(student_book_limit))
        self.mydb.commit()

    def set_student_book_time(self, student_book_time):
        self.cursor.execute("UPDATE settings SET student_book_time = {} WHERE number = 1".format(student_book_time))
        self.mydb.commit()

    def set_student_book_time(self, student_book_time):
        self.cursor.execute("UPDATE settings SET student_book_time = {} WHERE number = 1".format(student_book_time))
        self.mydb.commit()

    def show_my_books(self, id):
        sql = "SELECT * FROM checkouts WHERE id = '{}'".format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def check_if_student(self, id):
        # check if user is student or teacher
        sql = "SELECT * FROM users WHERE id = '{}'".format(id)
        self.cursor.execute(sql)
        user_level = self.cursor.fetchall()[0][4]

        # check if student has a limit
        if user_level == 1:
            return True
        return False

    def check_if_admin(self, id):
        # check if user is admin
        sql = "SELECT * FROM users WHERE id = '{}'".format(id)
        self.cursor.execute(sql)
        user_level = self.cursor.fetchall()[0][4]

        # check if student has a limit
        if user_level == 3:
            return True
        return False

    def book_available_number(self, isbn):
        # return number of available number if book is available
        sql = "SELECT * FROM books WHERE isbn = '{}'".format(isbn)
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][7]

    def checkout_book(self, id, isbn):
        available_number = self.book_available_number(isbn)
        if available_number == 0:
            return False

        if self.check_if_student(id) is True:
            if self.get_student_book_limit() <= len(self.show_my_books(id)):
                return False

        # Checkout book
        self.cursor.execute("UPDATE books SET available_number = {} WHERE isbn = {}".format(available_number - 1, isbn))
        self.mydb.commit()

        date = str(time.time())
        sql = "INSERT INTO checkouts VALUES (DEFAULT, {}, {}, {})".format(id, isbn, date)
        self.cursor.execute(sql)
        self.mydb.commit()
        return True

    def book_time_notification(self, id):
        # check if user is student or teacher
        if self.check_if_student(id) is False:
            return []

        sql = "SELECT * FROM checkouts WHERE id = '{}'".format(id)
        self.cursor.execute(sql)
        checkouts = self.cursor.fetchall()

        notify_books = []
        student_book_time_seconds = self.get_student_book_time() * 60
        for checkout in checkouts:
            time_difference_seconds = time.time() - float(checkout[3])
            if time_difference_seconds > student_book_time_seconds:
                notify_books.append(self.get_title_from_isbn(checkout[2]))
        return notify_books

    def get_title_from_isbn(self, isbn):
        self.cursor.execute("SELECT * FROM books WHERE isbn = {}".format(isbn))
        return self.cursor.fetchall()[0][1]

    def get_all_checkouts(self):
        # show all checkouts from database (only used by admin)
        self.cursor.execute("SELECT * FROM checkouts")
        return self.cursor.fetchall()

    def add_teacher_approval(self, id):
        try:
            sql = "INSERT INTO teacher_approvals (number, id) VALUES (DEFAULT, {})".format(id)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

    def get_teacher_approvals(self):
        # (only used by admin)
        self.cursor.execute("SELECT * FROM teacher_approvals")
        return self.cursor.fetchall()

    def approve_teacher_approval(self, id):
        # (only used by admin)
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
        # (only used by admin)
        try:
            sql = "DELETE FROM teacher_approvals WHERE id = {}".format(id)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

    def add_checkin_book_approval(self, id, isbn):
        # request for a Checkin book
        try:
            sql = "INSERT INTO checkin_approvals (number, id, isbn) VALUES (DEFAULT, {}, {})".format(id, isbn)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

    def get_checkin_book_approvals(self):
        # (only used by admin)
        self.cursor.execute("SELECT * FROM checkin_approvals")
        return self.cursor.fetchall()

    def approve_checkin_approval(self, id, isbn):
        # (only used by admin)
        try:
            # increase available number
            available_number = self.book_available_number(isbn)
            self.cursor.execute("UPDATE books SET available_number = {} WHERE isbn = {}".format(available_number + 1, isbn))
            self.mydb.commit()
            # delete book+id from checkouts
            sql = "DELETE FROM checkouts WHERE id = {} AND isbn = {}".format(id, isbn)
            self.cursor.execute(sql)
            self.mydb.commit()
            # delete book+id from checkin approvals
            sql = "DELETE FROM checkin_approvals WHERE id = {} AND isbn = {}".format(id, isbn)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

    def reject_checkin_book_approval(self, id, isbn):
        # (only used by admin)
        try:
            sql = "DELETE FROM checkin_approvals WHERE id = {} AND isbn = {}".format(id, isbn)
            self.cursor.execute(sql)
            self.mydb.commit()
        except:
            return False
        return True

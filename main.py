from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets

import sys
from datetime import date

from Library import Library

from LoginPage import Ui_LoginWindow
from RegistrationPage import Ui_RegistrationWindow
from BookSearch import Ui_SearchBookWindow
from StudentPage import Ui_StudentWindow
from AdminPage import Ui_AdminWindow
from TeacherAprovalPAge import Ui_TeacherAprovalWindow
from CheckedoutBookPage import Ui_CheckeoutWindow
from BookAdditionPage import Ui_BookAdditionWindow
from CheckinApprovalPage import Ui_CheckinApprovalWindow
from NotificationPage import Ui_NotificationWindow
from MyBooksPage import Ui_MyBooksWindow
from SettingsPage import Ui_SettingsWindow


def open_checkout_page():
    ui_checkedout_book.setupUi(MainWindow)
    ui_checkedout_book.button_back.clicked.connect(open_main_menu)
    # Get and fill in the book approvals into table
    ui_checkedout_book.tableWidget.clear()
    checkouts = lib.get_all_checkouts()

    if not checkouts:
        ui_checkedout_book.tableWidget.clear()
    else:
        num_rows = len(checkouts)
        num_cols = len(checkouts[0])-1

        # Set colums and rows in QTableWidget
        ui_checkedout_book.tableWidget.setRowCount(num_rows)
        ui_checkedout_book.tableWidget.setColumnCount(num_cols)
        ui_checkedout_book.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        ui_checkedout_book.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("ISBN"))
        ui_checkedout_book.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Date"))

        # Loops to add values into QTableWidget
        for row in range(num_rows):
            for column in range(num_cols):
                if column == 2:
                    item = str(date.fromtimestamp(float(checkouts[row][column+1])).__str__())
                else:
                    item = str(checkouts[row][column+1])
                ui_checkedout_book.tableWidget.setItem(row, column, QTableWidgetItem(item))
    MainWindow.show()


def open_main_menu():
    global global_id
    if lib.check_if_admin(global_id) is True:
        ui_admin.setupUi(MainWindow)
        ui_admin.button_searchbook.clicked.connect(open_search_page)
        ui_admin.button_addbook.clicked.connect(open_addbook_page)
        ui_admin.button_bookapproval.clicked.connect(open_bookapproval_page)
        ui_admin.button_teacherapproval.clicked.connect(open_teacherapproval_page)
        ui_admin.button_checkedout.clicked.connect(open_checkout_page)
        ui_admin.button_settings.clicked.connect(open_settings_page)
    else:
        ui_student.setupUi(MainWindow)
        ui_student.button_searchbook.clicked.connect(open_search_page)
        ui_student.button_notifications.clicked.connect(open_notification_page)
        ui_student.button_mybooks.clicked.connect(open_mybooks_page)
    MainWindow.show()


def login_func():
    global global_id
    login_check, id = lib.login(ui_login.text_input.text(), ui_login.text_password_login.text())
    if login_check is True:
        global_id = id
        open_main_menu()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Try again...")
        msg.setWindowTitle("Login Failed!")
        msg.exec()


def open_signup_page():
    ui_registration.setupUi(MainWindow)
    ui_registration.button_submit.clicked.connect(signup_submit_func)
    MainWindow.show()


def signup_submit_func():
    id = ui_registration.text_id.text()
    name = ui_registration.text_name.text() + ' ' + ui_registration.text_surname.text()
    email = ui_registration.text_email.text()
    password = ui_registration.text_password.text()
    password_confirm = ui_registration.text_password_confirm.text()
    if password != password_confirm:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Passwords does not match!")
        msg.setWindowTitle("Check password confirm")
        msg.exec()

    # add user to database
    if lib.add_user(id, name, email, password, 1) is True:
        if ui_registration.checkbox_teacher.isChecked() is True:
            lib.add_teacher_approval(id)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Redirecting to login page...")
        msg.setWindowTitle("Registration Succecss!")
        msg.exec()
        # reopen login page
        ui_login.setupUi(MainWindow)
        ui_login.button_login.clicked.connect(login_func)
        ui_login.button_signup.clicked.connect(open_signup_page)
        ui_login.text_input.setText(id)
        ui_login.text_password_login.setText(password)
        MainWindow.show()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Check inputs again...")
        msg.setWindowTitle("Registration failed!")
        msg.exec()


def open_search_page():
    ui_search_book.setupUi(MainWindow)
    ui_search_book.button_search.clicked.connect(search_func)
    ui_search_book.button_checkout.clicked.connect(checkout_func)
    ui_search_book.button_back.clicked.connect(open_main_menu)


def search_func():
    isbn = ui_search_book.text_isbn.text()
    if isbn == '':
        isbn = None
    title = ui_search_book.text_title.text()
    if title == '':
        title = None
    author = ui_search_book.text_author.text()
    if author == '':
        author = None
    category = ui_search_book.text_category.text()
    if category == '':
        category = None
    show_only_available = not ui_search_book.checkbox_available.isChecked()

    books = lib.search_book(isbn, title, author, category, show_only_available)
    if not books:
        ui_search_book.tableWidget.clear()
    else:
        num_rows = len(books)
        num_cols = len(books[0])

        # Set colums and rows in QTableWidget
        ui_search_book.tableWidget.setRowCount(num_rows)
        ui_search_book.tableWidget.setColumnCount(num_cols)

        # Loops to add values into QTableWidget
        for row in range(num_rows):
            for column in range(num_cols):
                item = str(books[row][column])
                ui_search_book.tableWidget.setItem(row, column, QTableWidgetItem(item))


def checkout_func():
    global global_id
    index = ui_search_book.tableWidget.currentRow()
    isbn = ui_search_book.tableWidget.item(index, 0).text()
    if lib.checkout_book(global_id, isbn) is True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Good reading...")
        msg.setWindowTitle("Checkout Success!")
        msg.exec()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Either book is not available OR you have reached your limit...")
        msg.setWindowTitle("Checkout failed!")
        msg.exec()


def open_addbook_page():
    ui_book_addition.setupUi(MainWindow)
    ui_book_addition.button_submit.clicked.connect(add_book_func)
    ui_book_addition.button_back.clicked.connect(open_main_menu)
    MainWindow.show()


def add_book_func():
    isbn = int(ui_book_addition.text_isbn.text())
    title = ui_book_addition.text_title.text()
    author = ui_book_addition.text_author.text()
    publish_year = int(ui_book_addition.text_publishyear.text())
    category = ui_book_addition.text_category.text()
    page_number = int(ui_book_addition.text_pagenumber.text())
    if lib.add_book(isbn, title, author, publish_year, category, page_number) is True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Book added to library...")
        msg.setWindowTitle("Book Addition Succecss!")
        msg.exec()
        # empty the fields login page
        ui_book_addition.text_isbn.setText('')
        ui_book_addition.text_title.setText('')
        ui_book_addition.text_author.setText('')
        ui_book_addition.text_publishyear.setText('')
        ui_book_addition.text_category.setText('')
        ui_book_addition.text_pagenumber.setText('')
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Check inputs again...")
        msg.setWindowTitle("Book addition failed!")
        msg.exec()


def open_bookapproval_page():
    ui_checkin_approval.setupUi(MainWindow)
    ui_checkin_approval.button_accept.clicked.connect(book_approval_accept_func)
    ui_checkin_approval.button_reject.clicked.connect(book_approval_reject_func)
    ui_checkin_approval.button_back.clicked.connect(open_main_menu)
    # Get and fill in the book approvals into table
    refresh_book_approval_table()
    MainWindow.show()

def refresh_book_approval_table():
    ui_checkin_approval.tableWidget.clear()
    bookapprovals = lib.get_checkin_book_approvals()
    if not bookapprovals:
        ui_checkin_approval.tableWidget.clear()
    else:
        num_rows = len(bookapprovals)
        num_cols = len(bookapprovals[0])-1

        # Set colums and rows in QTableWidget
        ui_checkin_approval.tableWidget.setRowCount(num_rows)
        ui_checkin_approval.tableWidget.setColumnCount(num_cols)
        ui_checkin_approval.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        ui_checkin_approval.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("ISBN"))
        ui_checkin_approval.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Date"))

        # Loops to add values into QTableWidget
        for row in range(num_rows):
            for column in range(num_cols):
                if column == 2:
                    item = str(date.fromtimestamp(float(bookapprovals[row][column+1])).__str__())
                else:
                    item = str(bookapprovals[row][column+1])
                ui_checkin_approval.tableWidget.setItem(row, column, QTableWidgetItem(item))

def book_approval_accept_func():
    index = ui_checkin_approval.tableWidget.currentRow()
    id = ui_checkin_approval.tableWidget.item(index, 0).text()
    isbn = ui_checkin_approval.tableWidget.item(index, 1).text()
    if lib.approve_checkin_approval(id, isbn) is True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Checkin book approved...")
        msg.setWindowTitle("Success!")
        msg.exec()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Failed to approve...")
        msg.setWindowTitle("Failure!")
        msg.exec()
    refresh_book_approval_table()

def book_approval_reject_func():
    index = ui_checkin_approval.tableWidget.currentRow()
    id = ui_checkin_approval.tableWidget.item(index, 0).text()
    isbn = ui_checkin_approval.tableWidget.item(index, 1).text()
    if lib.reject_checkin_book_approval(id, isbn) is True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Checkin book rejected...")
        msg.setWindowTitle("Success!")
        msg.exec()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Failed to reject...")
        msg.setWindowTitle("Failure!")
        msg.exec()
    refresh_book_approval_table()


def open_teacherapproval_page():
    ui_teacher_approval.setupUi(MainWindow)
    ui_teacher_approval.button_accept.clicked.connect(teacher_approval_accept_func)
    ui_teacher_approval.button_reject.clicked.connect(teacher_approval_reject_func)
    ui_teacher_approval.button_back.clicked.connect(open_main_menu)
    # Get and fill in the book approvals into table
    refresh_teacher_approval_table()
    MainWindow.show()


def refresh_teacher_approval_table():
    ui_teacher_approval.tableWidget.clear()
    teacherapprovals = lib.get_teacher_approvals()
    if not teacherapprovals:
        ui_teacher_approval.tableWidget.clear()
    else:
        num_rows = len(teacherapprovals)
        num_cols = len(teacherapprovals[0])-1

        # Set colums and rows in QTableWidget
        ui_teacher_approval.tableWidget.setRowCount(num_rows)
        ui_teacher_approval.tableWidget.setColumnCount(num_cols)
        ui_teacher_approval.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))

        # Loops to add values into QTable.Widget
        for row in range(num_rows):
            for column in range(num_cols):
                item = str(teacherapprovals[row][column+1])
                ui_teacher_approval.tableWidget.setItem(row, column, QTableWidgetItem(item))


def teacher_approval_accept_func():
    index = ui_teacher_approval.tableWidget.currentRow()
    id = ui_teacher_approval.tableWidget.item(index, 0).text()
    if lib.approve_teacher_approval(id) is True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Teacher approved...")
        msg.setWindowTitle("Success!")
        msg.exec()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Failed to approve...")
        msg.setWindowTitle("Failure!")
        msg.exec()
    refresh_teacher_approval_table()


def teacher_approval_reject_func():
    index = ui_teacher_approval.tableWidget.currentRow()
    id = ui_teacher_approval.tableWidget.item(index, 0).text()
    if lib.reject_teacher_approval(id) is True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Teacher rejected...")
        msg.setWindowTitle("Success!")
        msg.exec()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Failed to reject...")
        msg.setWindowTitle("Failure!")
        msg.exec()
    refresh_teacher_approval_table()


def open_notification_page():
    global global_id
    ui_notification.setupUi(MainWindow)
    ui_notification.button_back.clicked.connect(open_main_menu)

    notifications = lib.book_time_notification(global_id)
    if len(notifications) == 0:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Have a good day...")
        msg.setWindowTitle("No notifications!")
        msg.exec()
    else:
        for notification in notifications:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please return book {} ".format(notification))
            msg.setWindowTitle("Notification Found!")
            msg.exec()
    MainWindow.show()

def open_mybooks_page():
    global global_id
    ui_my_book.setupUi(MainWindow)
    ui_my_book.button_back.clicked.connect(open_main_menu)
    ui_my_book.button_checkin.clicked.connect(checkin_func)
    # Get and fill in the book approvals into table
    refresh_mybook_table()
    MainWindow.show()

def refresh_mybook_table():
    ui_my_book.tableWidget.clear()
    mybooks = lib.show_my_books(global_id)

    if not mybooks:
        ui_my_book.tableWidget.clear()
    else:
        num_rows = len(mybooks)
        num_cols = len(mybooks[0])-2

        # Set colums and rows in QTableWidget
        ui_my_book.tableWidget.setRowCount(num_rows)
        ui_my_book.tableWidget.setColumnCount(num_cols)
        ui_my_book.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ISBN"))
        ui_my_book.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Date"))

        # Loops to add values into QTableWidget
        for row in range(num_rows):
            for column in range(num_cols):
                if column == 1:
                    item = str(date.fromtimestamp(float(mybooks[row][column+2])).__str__())
                else:
                    item = str(mybooks[row][column+2])
                ui_my_book.tableWidget.setItem(row, column, QTableWidgetItem(item))

def checkin_func():
    global global_id
    index = ui_my_book.tableWidget.currentRow()
    isbn = ui_my_book.tableWidget.item(index, 0).text()

    if lib.add_checkin_book_approval(global_id, int(isbn)) is True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Read more...")
        msg.setWindowTitle("Checkin Success!")
        msg.exec()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Checkin process failed ")
        msg.setWindowTitle("Checkin Failed!")
        msg.exec()
    refresh_mybook_table()

def open_settings_page():
    ui_settings.setupUi(MainWindow)


    ui_settings.text_book_limit.setText(lib.get_student_book_limit())
    ui_settings.text_book_time.setText(lib.get_student_book_time())

    ui_settings.button_book_limit.clicked.connect(book_limit_func)
    ui_settings.button_book_time.clicked.connect(book_time_func)
    ui_settings.button_back.clicked.connect(open_main_menu)
    MainWindow.show()

def book_limit_func():
    book_limit = ui_settings.text_book_limit.text()
    lib.set_student_book_limit(book_limit)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("New Book Limit set...")
    msg.setWindowTitle("Success!")
    msg.exec()

def book_time_func():
    book_time = ui_settings.text_book_time.text()
    lib.set_student_book_time(book_time)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("New Book Time set...")
    msg.setWindowTitle("Success!")
    msg.exec()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Setup Login Window
ui_login = Ui_LoginWindow()
ui_login.setupUi(MainWindow)
ui_login.button_login.clicked.connect(login_func)
ui_login.button_signup.clicked.connect(open_signup_page)
global_id = 0

# Setup Registration Window
ui_registration = Ui_RegistrationWindow()

# Setup Search Window
ui_search_book = Ui_SearchBookWindow()

ui_student = Ui_StudentWindow()
ui_admin = Ui_AdminWindow()
ui_teacher_approval = Ui_TeacherAprovalWindow()
ui_checkedout_book = Ui_CheckeoutWindow()
ui_book_addition = Ui_BookAdditionWindow()
ui_checkin_approval = Ui_CheckinApprovalWindow()
ui_notification = Ui_NotificationWindow()
ui_my_book = Ui_MyBooksWindow()
ui_settings = Ui_SettingsWindow()


# Setup Library Database
lib = Library()

MainWindow.show()
sys.exit(app.exec_())


# if __name__ == "__main__":
    # lib.add_book(1576, 'lalala', 'bey ', 1950, 'horror', 50)
    # lib.add_book(1578, 'safsdf', 'sdf ', 1950, 'horror', 50)
    # lib.add_user(195050001, 'simay seyrek', 'simayseyrek@gmail.com', 'ss123', 3)
    # lib.add_user(195050001, 'simay seyrek', 'simayseyrek@gmail.com', 'ss123', 3)
    # print(lib.get_teacher_approval())
    # print(lib.add_user(19505000, 'simay seyrek', 'simayseyrek@gmail.com', 'ss123', 1))
    # print(lib.add_teacher_approval(19505000))
    # print(lib.get_teacher_approval())
    # print(lib.reject_teacher_approval(19505000))
    # print(lib.get_teacher_approval())
    # print(lib.add_teacher_approval(19505000))
    # print(lib.approve_teacher_approval(19505000))
    # lib.add_user(195050001, 'simay seyrek', 'simayseyrek@gmail.com', 'ss123', 3)
    # print(lib.login('195050000', 'sad'))
    # print(lib.login('195050001', 'sad'))
    # print(lib.login('simayseyredk@gmail.com', 'ss123'))
    # print(lib.login('simayseyrek@gmail.com', 'sad'))
    # print(lib.login('simayseyrek@gmail.com', 'ss123'))
    # print(lib.login('195050001', 'ss123'))
    # print(lib.search_book(isbn='1047210'))
    # print(lib.search_book(isbn='1047213'))
    # print(lib.search_book(category='Contemporar', title='Brav', author='Aldo'))
    # print(lib.search_book(author='Eli', category='Roman'))
    # print(lib.search_book(category='Dystopian', title='First Among'))
    # print(lib.search_book(author='Eli', title='Daug'))
    # print(lib.search_book(author='sdasd'))
    # print(lib.search_book(title='The Fighting Man'))
    # print(lib.search_book(category='asdasd'))
    # print(lib.search_book(title='The Fighting Man', show_only_available=True))
    # print(lib.search_book(title='The Fighting Man', show_only_available=False))

    # print(lib.get_student_book_limit())
    # print(lib.get_student_book_time())
    # print(lib.set_student_book_limit(2)
    # print(lib.set_student_book_time(7))

    # print(lib.add_user(195050002, 'simay seyrek', 'simayseyrek@gmail.com', 'ss123', 1))
    # print(lib.show_my_book(195050002))
    # print(lib.checkout_book(195050002, 1052039))
    # print(lib.show_my_book(195050002))
    # print(lib.checkout_book(195050002, 1010565))
    # print(lib.show_my_book(195050002))
    # print(lib.checkout_book(195050002, 1360469))
    # print(lib.show_my_book(195050002))
    # print(lib.checkout_book(195050002, 1048082))
    # print(lib.book_time_notification(195050002))

    # print(lib.show_my_books(195050001))
    # print(lib.show_my_books(195050002))
    # print(lib.add_checkin_book_approval(195050001, 7154615))
    # print(lib.add_checkin_book_approval(195050002, 7154615))
    # print(lib.add_checkin_book_approval(195050001, 1049879))
    # print(lib.show_my_books(195050001))
    # print(lib.show_my_books(195050002))
    # print(lib.search_book(isbn='7154615'))
    #
    # print(lib.get_checkin_book_approvals())
    # print(lib.reject_checkin_book_approval(195050001, 1049879))
    # print(lib.get_checkin_book_approvals())
    #
    # print(lib.approve_checkin_approval(195050001, 7154615))
    # print(lib.approve_checkin_approval(195050002, 7154615))
    # print(lib.get_checkin_book_approvals())
    # print(lib.show_my_books(195050001))
    # print(lib.show_my_books(195050002))
    # print(lib.search_book(isbn='7154615'))
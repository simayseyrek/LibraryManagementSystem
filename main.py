from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from Library import Library
import sys
from LoginPage import Ui_LoginWindow
from RegistrationPage import Ui_RegistrationWindow
from BookSearch import Ui_SearchBookWindow
from PyQt5 import QtWidgets


def login_func():
    global global_id
    login_check, id = lib.login(ui_login.text_input.text(), ui_login.text_password_login.text())
    if login_check is True:
        global_id = id
        if lib.check_if_admin(id) is True:
            ui_search_book.setupUi(MainWindow)  # TODO ui_admin_main
            ui_search_book.button_search.clicked.connect(search)
            ui_search_book.button_checkout.clicked.connect(checkout)
        else:
            ui_search_book.setupUi(MainWindow)  # TODO ui_student_main
            ui_search_book.button_search.clicked.connect(search)
            ui_search_book.button_checkout.clicked.connect(checkout)
        MainWindow.show()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Try again...")
        msg.setWindowTitle("Login Failed!")
        msg.exec()


def signup_func():
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
        ui_login.button_signup.clicked.connect(signup_func)
        ui_login.text_input.setText(id)
        ui_login.text_password_login.setText(password)
        MainWindow.show()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Check inputs again...")
        msg.setWindowTitle("Registration failed!")
        msg.exec()


def search():
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
        num_rows = len(books)  # 6 rows in your example
        num_cols = len(books[0])  # 3 columns in your example

        # Set colums and rows in QTableWidget
        ui_search_book.tableWidget.setRowCount(num_rows)
        ui_search_book.tableWidget.setColumnCount(num_cols)

        # Loops to add values into QTableWidget
        for row in range(num_rows):
            for column in range(num_cols):
                item = str(books[row][column])
                ui_search_book.tableWidget.setItem(row, column, QTableWidgetItem(item))


def checkout():
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





app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Setup Login Window
ui_login = Ui_LoginWindow()
ui_login.setupUi(MainWindow)
ui_login.button_login.clicked.connect(login_func)
ui_login.button_signup.clicked.connect(signup_func)
global_id = 0

# Setup Registration Window
ui_registration = Ui_RegistrationWindow()

# Setup Search Window
ui_search_book = Ui_SearchBookWindow()

ui_admin_main = Ui_SearchBookWindow()
ui_student_main = Ui_SearchBookWindow()

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
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(20)
        LoginWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 186, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(440, 290, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.button_signup = QtWidgets.QPushButton(self.centralwidget)
        self.button_signup.setGeometry(QtCore.QRect(440, 380, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_signup.setFont(font)
        self.button_signup.setObjectName("button_signup")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 380, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input.setGeometry(QtCore.QRect(250, 110, 370, 40))
        self.text_input.setObjectName("text_input")
        self.text_password_login = QtWidgets.QLineEdit(self.centralwidget)
        self.text_password_login.setGeometry(QtCore.QRect(250, 180, 370, 40))
        self.text_password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_password_login.setObjectName("text_password_login")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "Welcome to E-Library"))
        self.label_2.setText(_translate("LoginWindow", "Enter e-mail / ID :"))
        self.label_3.setText(_translate("LoginWindow", "Password : "))
        self.button_login.setText(_translate("LoginWindow", "Login"))
        self.button_signup.setText(_translate("LoginWindow", "Sign up"))
        self.label_4.setText(_translate("LoginWindow", "Don\'t have an account yet? "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_book_limit = QtWidgets.QPushButton(self.centralwidget)
        self.button_book_limit.setGeometry(QtCore.QRect(420, 100, 121, 31))
        self.button_book_limit.setObjectName("button_book_limit")
        self.text_book_limit = QtWidgets.QLineEdit(self.centralwidget)
        self.text_book_limit.setGeometry(QtCore.QRect(180, 100, 181, 31))
        self.text_book_limit.setObjectName("text_book_limit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.text_book_time = QtWidgets.QLineEdit(self.centralwidget)
        self.text_book_time.setGeometry(QtCore.QRect(170, 320, 181, 31))
        self.text_book_time.setObjectName("text_book_time")
        self.button_book_time = QtWidgets.QPushButton(self.centralwidget)
        self.button_book_time.setGeometry(QtCore.QRect(410, 320, 121, 31))
        self.button_book_time.setObjectName("button_book_time")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(680, 500, 89, 25))
        self.button_back.setObjectName("button_back")
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.button_book_limit.setText(_translate("SettingsWindow", "SET"))
        self.label.setText(_translate("SettingsWindow", "Book Limit"))
        self.button_book_time.setText(_translate("SettingsWindow", "SET"))
        self.label_3.setText(_translate("SettingsWindow", "Book Time"))
        self.button_back.setText(_translate("SettingsWindow", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())


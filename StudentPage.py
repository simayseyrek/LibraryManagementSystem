# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentWindow(object):
    def setupUi(self, StudentWindow):
        StudentWindow.setObjectName("StudentWindow")
        StudentWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(StudentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_mybooks = QtWidgets.QPushButton(self.centralwidget)
        self.button_mybooks.setGeometry(QtCore.QRect(70, 90, 641, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_mybooks.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/131-1310865_school-supply-list-school-book-icon-png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_mybooks.setIcon(icon)
        self.button_mybooks.setIconSize(QtCore.QSize(75, 75))
        self.button_mybooks.setObjectName("button_mybooks")
        self.button_notifications = QtWidgets.QPushButton(self.centralwidget)
        self.button_notifications.setGeometry(QtCore.QRect(70, 360, 641, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_notifications.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../tmp/mozilla_sim0/icons8-notification-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_notifications.setIcon(icon1)
        self.button_notifications.setIconSize(QtCore.QSize(100, 100))
        self.button_notifications.setObjectName("button_notifications")
        self.button_searchbook = QtWidgets.QPushButton(self.centralwidget)
        self.button_searchbook.setGeometry(QtCore.QRect(70, 230, 641, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_searchbook.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/book_searchj.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_searchbook.setIcon(icon2)
        self.button_searchbook.setIconSize(QtCore.QSize(75, 75))
        self.button_searchbook.setObjectName("button_searchbook")
        StudentWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StudentWindow)
        self.statusbar.setObjectName("statusbar")
        StudentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StudentWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentWindow)

    def retranslateUi(self, StudentWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentWindow.setWindowTitle(_translate("StudentWindow", "MainWindow"))
        self.button_mybooks.setText(_translate("StudentWindow", " My Books"))
        self.button_notifications.setText(_translate("StudentWindow", " Notifications"))
        self.button_searchbook.setText(_translate("StudentWindow", " Search Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentWindow()
    ui.setupUi(StudentWindow)
    StudentWindow.show()
    sys.exit(app.exec_())


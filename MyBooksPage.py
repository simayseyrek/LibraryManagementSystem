# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyBooksPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyBooksWindow(object):
    def setupUi(self, MyBooksWindow):
        MyBooksWindow.setObjectName("MyBooksWindow")
        MyBooksWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MyBooksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(680, 520, 89, 25))
        self.button_back.setObjectName("button_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 751, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(245)
        self.button_checkin = QtWidgets.QPushButton(self.centralwidget)
        self.button_checkin.setGeometry(QtCore.QRect(480, 470, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_checkin.setFont(font)
        self.button_checkin.setObjectName("button_checkin")
        MyBooksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MyBooksWindow)
        self.statusbar.setObjectName("statusbar")
        MyBooksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyBooksWindow)
        QtCore.QMetaObject.connectSlotsByName(MyBooksWindow)

    def retranslateUi(self, MyBooksWindow):
        _translate = QtCore.QCoreApplication.translate
        MyBooksWindow.setWindowTitle(_translate("MyBooksWindow", "MainWindow"))
        self.button_back.setText(_translate("MyBooksWindow", "back"))
        self.label.setText(_translate("MyBooksWindow", "My Books"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MyBooksWindow", "isbn"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MyBooksWindow", "isbn"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MyBooksWindow", "Date"))
        self.button_checkin.setText(_translate("MyBooksWindow", "Check-in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyBooksWindow = QtWidgets.QMainWindow()
    ui = Ui_MyBooksWindow()
    ui.setupUi(MyBooksWindow)
    MyBooksWindow.show()
    sys.exit(app.exec_())


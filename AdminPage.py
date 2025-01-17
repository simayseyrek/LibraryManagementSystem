# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_addbook = QtWidgets.QPushButton(self.centralwidget)
        self.button_addbook.setGeometry(QtCore.QRect(70, 110, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_addbook.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/661579_book_512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_addbook.setIcon(icon)
        self.button_addbook.setIconSize(QtCore.QSize(75, 75))
        self.button_addbook.setObjectName("button_addbook")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.button_checkedout = QtWidgets.QPushButton(self.centralwidget)
        self.button_checkedout.setGeometry(QtCore.QRect(70, 370, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_checkedout.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/reading_list-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_checkedout.setIcon(icon1)
        self.button_checkedout.setIconSize(QtCore.QSize(75, 75))
        self.button_checkedout.setObjectName("button_checkedout")
        self.button_searchbook = QtWidgets.QPushButton(self.centralwidget)
        self.button_searchbook.setGeometry(QtCore.QRect(70, 240, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_searchbook.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/131-1310865_school-supply-list-school-book-icon-png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_searchbook.setIcon(icon2)
        self.button_searchbook.setIconSize(QtCore.QSize(75, 75))
        self.button_searchbook.setObjectName("button_searchbook")
        self.button_teacherapproval = QtWidgets.QPushButton(self.centralwidget)
        self.button_teacherapproval.setGeometry(QtCore.QRect(440, 240, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_teacherapproval.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/teacher_approval.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_teacherapproval.setIcon(icon3)
        self.button_teacherapproval.setIconSize(QtCore.QSize(75, 75))
        self.button_teacherapproval.setObjectName("button_teacherapproval")
        self.button_bookapproval = QtWidgets.QPushButton(self.centralwidget)
        self.button_bookapproval.setGeometry(QtCore.QRect(440, 110, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_bookapproval.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/book_approve (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_bookapproval.setIcon(icon4)
        self.button_bookapproval.setIconSize(QtCore.QSize(75, 75))
        self.button_bookapproval.setObjectName("button_bookapproval")
        self.button_settings = QtWidgets.QPushButton(self.centralwidget)
        self.button_settings.setGeometry(QtCore.QRect(440, 370, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_settings.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_settings.setIcon(icon5)
        self.button_settings.setIconSize(QtCore.QSize(75, 75))
        self.button_settings.setObjectName("button_settings")
        AdminWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "MainWindow"))
        self.button_addbook.setText(_translate("AdminWindow", "Add Book"))
        self.label.setText(_translate("AdminWindow", "Welcome to Admin Page"))
        self.button_checkedout.setText(_translate("AdminWindow", "Checked Out Books"))
        self.button_searchbook.setText(_translate("AdminWindow", "Search Book"))
        self.button_teacherapproval.setText(_translate("AdminWindow", "Teacher Approvals"))
        self.button_bookapproval.setText(_translate("AdminWindow", " Check-in Approvals"))
        self.button_settings.setText(_translate("AdminWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NotificationPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotificationWindow(object):
    def setupUi(self, NotificationWindow):
        NotificationWindow.setObjectName("NotificationWindow")
        NotificationWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NotificationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(660, 520, 89, 25))
        self.button_back.setObjectName("button_back")
        NotificationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NotificationWindow)
        self.statusbar.setObjectName("statusbar")
        NotificationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NotificationWindow)
        QtCore.QMetaObject.connectSlotsByName(NotificationWindow)

    def retranslateUi(self, NotificationWindow):
        _translate = QtCore.QCoreApplication.translate
        NotificationWindow.setWindowTitle(_translate("NotificationWindow", "MainWindow"))
        self.label.setText(_translate("NotificationWindow", "Notifications"))
        self.button_back.setText(_translate("NotificationWindow", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NotificationWindow = QtWidgets.QMainWindow()
    ui = Ui_NotificationWindow()
    ui.setupUi(NotificationWindow)
    NotificationWindow.show()
    sys.exit(app.exec_())


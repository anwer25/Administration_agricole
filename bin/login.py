# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 225)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 100, 101, 20))
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(20, 30, 171, 20))
        self.username.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(20, 100, 171, 20))
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(250, 170, 111, 31))
        self.login.setObjectName("login")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(30, 170, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.exit.setFont(font)
        self.exit.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "إسم المستخدم :"))
        self.label_2.setText(_translate("MainWindow", "كلمة السر :"))
        self.login.setText(_translate("MainWindow", "تسجيل دخول"))
        self.exit.setText(_translate("MainWindow", "خروج"))

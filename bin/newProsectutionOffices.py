# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProsectutionOffices.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(389, 416)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(18)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(300, 380, 75, 23))
        self.save.setObjectName("save")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(210, 380, 75, 23))
        self.cancel.setObjectName("cancel")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 307, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 226, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 145, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 64, 111, 16))
        self.label_4.setObjectName("label_4")
        self.addres = QtWidgets.QLineEdit(Form)
        self.addres.setGeometry(QtCore.QRect(46, 226, 181, 20))
        self.addres.setObjectName("addres")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(46, 307, 181, 20))
        self.phone.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.phone.setObjectName("phone")
        self.lastName = QtWidgets.QLineEdit(Form)
        self.lastName.setGeometry(QtCore.QRect(46, 145, 181, 20))
        self.lastName.setObjectName("lastName")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(46, 64, 181, 20))
        self.name.setObjectName("name")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save.setText(_translate("Form", "حفظ"))
        self.cancel.setText(_translate("Form", "إلغاء"))
        self.label.setText(_translate("Form", "الهاتف:"))
        self.label_2.setText(_translate("Form", "عنوان:"))
        self.label_3.setText(_translate("Form", "لقب صاحب نيابة:"))
        self.label_4.setText(_translate("Form", "اسم صاحب نيابة:"))

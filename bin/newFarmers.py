# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newFarmers.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newFarmers(object):
    def setupUi(self, newFarmers):
        newFarmers.setObjectName("newFarmers")
        newFarmers.setWindowModality(QtCore.Qt.WindowModal)
        newFarmers.resize(442, 316)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(11)
        newFarmers.setFont(font)
        newFarmers.setLayoutDirection(QtCore.Qt.RightToLeft)
        newFarmers.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.gridLayout = QtWidgets.QGridLayout(newFarmers)
        self.gridLayout.setObjectName("gridLayout")
        self.lastName = QtWidgets.QLineEdit(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.lastName.setFont(font)
        self.lastName.setObjectName("lastName")
        self.gridLayout.addWidget(self.lastName, 2, 4, 1, 1)
        self.idNumber = QtWidgets.QLineEdit(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.idNumber.setFont(font)
        self.idNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.idNumber.setObjectName("idNumber")
        self.gridLayout.addWidget(self.idNumber, 0, 4, 1, 1)
        self.name = QtWidgets.QLineEdit(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 4, 1, 1)
        self.headsNumber = QtWidgets.QLineEdit(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.headsNumber.setFont(font)
        self.headsNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.headsNumber.setObjectName("headsNumber")
        self.gridLayout.addWidget(self.headsNumber, 5, 4, 1, 1)
        self.phoneNumber = QtWidgets.QLineEdit(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.phoneNumber.setFont(font)
        self.phoneNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.phoneNumber.setObjectName("phoneNumber")
        self.gridLayout.addWidget(self.phoneNumber, 3, 4, 1, 1)
        self.Deanship = QtWidgets.QComboBox(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.Deanship.setFont(font)
        self.Deanship.setObjectName("Deanship")
        self.gridLayout.addWidget(self.Deanship, 4, 4, 1, 1)
        self.cancel = QtWidgets.QPushButton(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 7, 3, 1, 1)
        self.save = QtWidgets.QPushButton(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 7, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(newFarmers)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.retranslateUi(newFarmers)
        QtCore.QMetaObject.connectSlotsByName(newFarmers)

    def retranslateUi(self, newFarmers):
        _translate = QtCore.QCoreApplication.translate
        newFarmers.setWindowTitle(_translate("newFarmers", "جديد"))
        self.cancel.setText(_translate("newFarmers", "إلغاء"))
        self.save.setText(_translate("newFarmers", "حفظ"))
        self.label_2.setText(_translate("newFarmers", "رقم بطاقة التعريف وطنية :"))
        self.label_3.setText(_translate("newFarmers", "الاسم :"))
        self.label_4.setText(_translate("newFarmers", "اللقب :"))
        self.label_8.setText(_translate("newFarmers", "الهاتف :"))
        self.label_6.setText(_translate("newFarmers", "العمادة :"))
        self.label_7.setText(_translate("newFarmers", "عدد الرؤوس :"))

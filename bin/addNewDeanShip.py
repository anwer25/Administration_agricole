# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNewDeanShip.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addNewDeanShip(object):
    def setupUi(self, addNewDeanShip):
        addNewDeanShip.setObjectName("addNewDeanShip")
        addNewDeanShip.resize(340, 124)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        addNewDeanShip.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addNewDeanShip.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(addNewDeanShip)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.save = QtWidgets.QPushButton(addNewDeanShip)
        self.save.setIconSize(QtCore.QSize(31, 25))
        self.save.setObjectName("save")
        self.gridLayout_2.addWidget(self.save, 2, 2, 1, 1)
        self.cancel = QtWidgets.QPushButton(addNewDeanShip)
        self.cancel.setObjectName("cancel")
        self.gridLayout_2.addWidget(self.cancel, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(addNewDeanShip)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(addNewDeanShip)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.deanshipName = QtWidgets.QLineEdit(addNewDeanShip)
        self.deanshipName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deanshipName.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.deanshipName.setObjectName("deanshipName")
        self.gridLayout_2.addWidget(self.deanshipName, 0, 0, 1, 2)
        self.population = QtWidgets.QLineEdit(addNewDeanShip)
        self.population.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.population.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.population.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.population.setMaxLength(8)
        self.population.setObjectName("population")
        self.gridLayout_2.addWidget(self.population, 1, 0, 1, 2)

        self.retranslateUi(addNewDeanShip)
        QtCore.QMetaObject.connectSlotsByName(addNewDeanShip)

    def retranslateUi(self, addNewDeanShip):
        _translate = QtCore.QCoreApplication.translate
        addNewDeanShip.setWindowTitle(_translate("addNewDeanShip", "D.P.A إضافة عمادة جديدة "))
        self.save.setText(_translate("addNewDeanShip", "حفظ"))
        self.cancel.setText(_translate("addNewDeanShip", "إلغاء"))
        self.label.setText(_translate("addNewDeanShip", "اسم عمادة :"))
        self.label_2.setText(_translate("addNewDeanShip", "عدد السكان:"))
from qrc_source import source

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchMethod.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_searchMethod(object):
    def setupUi(self, searchMethod):
        searchMethod.setObjectName("searchMethod")
        searchMethod.setWindowModality(QtCore.Qt.WindowModal)
        searchMethod.resize(558, 134)
        searchMethod.setMinimumSize(QtCore.QSize(558, 134))
        searchMethod.setMaximumSize(QtCore.QSize(558, 134))
        searchMethod.setBaseSize(QtCore.QSize(558, 134))
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(19)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        searchMethod.setFont(font)
        searchMethod.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        searchMethod.setWindowIcon(icon)
        searchMethod.setLayoutDirection(QtCore.Qt.RightToLeft)
        searchMethod.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.gridLayout = QtWidgets.QGridLayout(searchMethod)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(searchMethod)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 7, 1, 1)
        self.dateTO = QtWidgets.QDateEdit(searchMethod)
        self.dateTO.setFrame(True)
        self.dateTO.setMinimumDate(QtCore.QDate(2000, 9, 14))
        self.dateTO.setCalendarPopup(True)
        self.dateTO.setObjectName("dateTO")
        self.gridLayout.addWidget(self.dateTO, 0, 8, 1, 1)
        self.label = QtWidgets.QLabel(searchMethod)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)
        self.dateSearchOnOff = QtWidgets.QRadioButton(searchMethod)
        self.dateSearchOnOff.setChecked(True)
        self.dateSearchOnOff.setObjectName("dateSearchOnOff")
        self.gridLayout.addWidget(self.dateSearchOnOff, 0, 4, 1, 1)
        self.dateFrom = QtWidgets.QDateEdit(searchMethod)
        self.dateFrom.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateFrom.setCalendarPopup(True)
        self.dateFrom.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateFrom.setObjectName("dateFrom")
        self.gridLayout.addWidget(self.dateFrom, 0, 6, 1, 1)
        self.cinSearch = QtWidgets.QRadioButton(searchMethod)
        self.cinSearch.setObjectName("cinSearch")
        self.gridLayout.addWidget(self.cinSearch, 1, 4, 1, 1)
        self.CIN = QtWidgets.QLineEdit(searchMethod)
        self.CIN.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.CIN.setMaxLength(8)
        self.CIN.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.CIN.setObjectName("CIN")
        self.gridLayout.addWidget(self.CIN, 1, 8, 1, 1)
        self.searchButton = QtWidgets.QDialogButtonBox(searchMethod)
        self.searchButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 2, 4, 1, 1)

        self.retranslateUi(searchMethod)
        QtCore.QMetaObject.connectSlotsByName(searchMethod)

    def retranslateUi(self, searchMethod):
        _translate = QtCore.QCoreApplication.translate
        searchMethod.setWindowTitle(_translate("searchMethod", "D.P.A-ارشيف-طريقة-بحث"))
        self.label_2.setText(_translate("searchMethod", "    الى"))
        self.dateTO.setDisplayFormat(_translate("searchMethod", "d/M/yyyy"))
        self.label.setText(_translate("searchMethod", ":   من"))
        self.dateSearchOnOff.setText(_translate("searchMethod", "البحث باستخدام التاريخ"))
        self.dateFrom.setDisplayFormat(_translate("searchMethod", "d/M/yyyy"))
        self.cinSearch.setText(_translate("searchMethod", "البحث باستخدام ب.ت.و "))
from qrc_source import source

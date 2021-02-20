# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_history(object):
    def setupUi(self, history):
        history.setObjectName("history")
        history.setWindowModality(QtCore.Qt.ApplicationModal)
        history.resize(1366, 705)
        history.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        history.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        history.setWindowIcon(icon)
        history.setLayoutDirection(QtCore.Qt.RightToLeft)
        history.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.gridLayout = QtWidgets.QGridLayout(history)
        self.gridLayout.setObjectName("gridLayout")
        self.data = QtWidgets.QTableWidget(history)
        self.data.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.data.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.data.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.data.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.data.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.data.setTabKeyNavigation(False)
        self.data.setProperty("showDropIndicator", False)
        self.data.setDragDropOverwriteMode(False)
        self.data.setAlternatingRowColors(True)
        self.data.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.data.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.data.setCornerButtonEnabled(False)
        self.data.setObjectName("data")
        self.data.setColumnCount(7)
        self.data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(6, item)
        self.data.horizontalHeader().setDefaultSectionSize(192)
        self.data.horizontalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.data, 2, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(history)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.searsh = QtWidgets.QPushButton(self.splitter)
        self.searsh.setObjectName("searsh")
        self.remove = QtWidgets.QPushButton(self.splitter)
        self.remove.setObjectName("remove")
        self.print = QtWidgets.QPushButton(self.splitter)
        self.print.setObjectName("print")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.retranslateUi(history)
        QtCore.QMetaObject.connectSlotsByName(history)

    def retranslateUi(self, history):
        _translate = QtCore.QCoreApplication.translate
        history.setWindowTitle(_translate("history", "أرشيف"))
        self.data.setSortingEnabled(True)
        item = self.data.horizontalHeaderItem(0)
        item.setText(_translate("history", "رقم ب.ت.و"))
        item = self.data.horizontalHeaderItem(1)
        item.setText(_translate("history", "الاسم"))
        item = self.data.horizontalHeaderItem(2)
        item.setText(_translate("history", "اللقب"))
        item = self.data.horizontalHeaderItem(3)
        item.setText(_translate("history", "النيابة"))
        item = self.data.horizontalHeaderItem(4)
        item.setText(_translate("history", "عدد اكيس"))
        item = self.data.horizontalHeaderItem(5)
        item.setText(_translate("history", "التاريخ"))
        item = self.data.horizontalHeaderItem(6)
        item.setText(_translate("history", "رقم التذكرة"))
        self.searsh.setText(_translate("history", "بحث"))
        self.remove.setText(_translate("history", "مسح"))
        self.print.setText(_translate("history", "طباعة"))
from qrc_source import source

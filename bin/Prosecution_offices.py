# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prosecution_offices.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProsecutionOffices(object):
    def setupUi(self, ProsecutionOffices):
        ProsecutionOffices.setObjectName("ProsecutionOffices")
        ProsecutionOffices.resize(1366, 705)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        ProsecutionOffices.setFont(font)
        ProsecutionOffices.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gridLayout = QtWidgets.QGridLayout(ProsecutionOffices)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newProsecutionOffices = QtWidgets.QPushButton(ProsecutionOffices)
        self.newProsecutionOffices.setObjectName("newProsecutionOffices")
        self.horizontalLayout.addWidget(self.newProsecutionOffices)
        self.change = QtWidgets.QPushButton(ProsecutionOffices)
        self.change.setObjectName("change")
        self.horizontalLayout.addWidget(self.change)
        self.remove = QtWidgets.QPushButton(ProsecutionOffices)
        self.remove.setObjectName("remove")
        self.horizontalLayout.addWidget(self.remove)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.data = QtWidgets.QTableWidget(ProsecutionOffices)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        font.setKerning(True)
        self.data.setFont(font)
        self.data.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.data.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.data.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.data.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.data.setMidLineWidth(11)
        self.data.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.data.setTabKeyNavigation(False)
        self.data.setProperty("showDropIndicator", False)
        self.data.setDragDropOverwriteMode(False)
        self.data.setAlternatingRowColors(True)
        self.data.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.data.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.data.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.data.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.data.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.data.setShowGrid(True)
        self.data.setGridStyle(QtCore.Qt.SolidLine)
        self.data.setCornerButtonEnabled(True)
        self.data.setObjectName("data")
        self.data.setColumnCount(4)
        self.data.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(1)
        item.setFont(font)
        self.data.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data.setItem(0, 3, item)
        self.data.horizontalHeader().setDefaultSectionSize(333)
        self.gridLayout.addWidget(self.data, 1, 0, 1, 1)

        self.retranslateUi(ProsecutionOffices)
        QtCore.QMetaObject.connectSlotsByName(ProsecutionOffices)

    def retranslateUi(self, ProsecutionOffices):
        _translate = QtCore.QCoreApplication.translate
        ProsecutionOffices.setWindowTitle(_translate("ProsecutionOffices", "النيابات"))
        self.newProsecutionOffices.setText(_translate("ProsecutionOffices", "نيابة جديدة"))
        self.change.setText(_translate("ProsecutionOffices", "تغير"))
        self.remove.setText(_translate("ProsecutionOffices", "حذف"))
        self.data.setSortingEnabled(True)
        item = self.data.verticalHeaderItem(0)
        item.setText(_translate("ProsecutionOffices", "1"))
        item = self.data.horizontalHeaderItem(0)
        item.setText(_translate("ProsecutionOffices", "اسم صاحب نيابة"))
        item = self.data.horizontalHeaderItem(1)
        item.setText(_translate("ProsecutionOffices", "لقب صاحب نيابة"))
        item = self.data.horizontalHeaderItem(2)
        item.setText(_translate("ProsecutionOffices", "عنوان"))
        item = self.data.horizontalHeaderItem(3)
        item.setText(_translate("ProsecutionOffices", "الهاتف"))
        __sortingEnabled = self.data.isSortingEnabled()
        self.data.setSortingEnabled(False)
        self.data.setSortingEnabled(__sortingEnabled)

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distribution.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_distribution(object):
    def setupUi(self, distribution):
        distribution.setObjectName("distribution")
        distribution.resize(1366, 705)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        distribution.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        distribution.setWindowIcon(icon)
        distribution.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.horizontalLayout = QtWidgets.QHBoxLayout(distribution)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(distribution)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(19)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(0, 13, 9, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.displayByDeanships = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.displayByDeanships.setFont(font)
        self.displayByDeanships.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.displayByDeanships.setAutoRepeat(True)
        self.displayByDeanships.setObjectName("displayByDeanships")
        self.gridLayout_2.addWidget(self.displayByDeanships, 0, 1, 1, 1)
        self.displayByCIN = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.displayByCIN.setFont(font)
        self.displayByCIN.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.displayByCIN.setChecked(True)
        self.displayByCIN.setAutoRepeat(True)
        self.displayByCIN.setAutoRepeatDelay(300)
        self.displayByCIN.setObjectName("displayByCIN")
        self.gridLayout_2.addWidget(self.displayByCIN, 0, 3, 1, 1)
        self.searsh = QtWidgets.QLineEdit(self.groupBox_2)
        self.searsh.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.searsh.setFont(font)
        self.searsh.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.searsh.setObjectName("searsh")
        self.gridLayout_2.addWidget(self.searsh, 1, 5, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.deanships = QtWidgets.QComboBox(self.groupBox_2)
        self.deanships.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.deanships.setFont(font)
        self.deanships.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.deanships.setObjectName("deanships")
        self.gridLayout_2.addWidget(self.deanships, 1, 1, 1, 1)
        self.searshButton = QtWidgets.QPushButton(self.groupBox_2)
        self.searshButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.searshButton.setFont(font)
        self.searshButton.setObjectName("searshButton")
        self.gridLayout_2.addWidget(self.searshButton, 1, 7, 1, 1)
        self.farmersListTable = QtWidgets.QTableWidget(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.farmersListTable.setFont(font)
        self.farmersListTable.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.farmersListTable.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.farmersListTable.setLineWidth(12)
        self.farmersListTable.setMidLineWidth(6)
        self.farmersListTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.farmersListTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.farmersListTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.farmersListTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.farmersListTable.setTabKeyNavigation(False)
        self.farmersListTable.setProperty("showDropIndicator", True)
        self.farmersListTable.setDragEnabled(True)
        self.farmersListTable.setDragDropOverwriteMode(False)
        self.farmersListTable.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.farmersListTable.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.farmersListTable.setAlternatingRowColors(True)
        self.farmersListTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.farmersListTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.farmersListTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.farmersListTable.setCornerButtonEnabled(True)
        self.farmersListTable.setColumnCount(4)
        self.farmersListTable.setObjectName("farmersListTable")
        self.farmersListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.farmersListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmersListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmersListTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmersListTable.setHorizontalHeaderItem(3, item)
        self.farmersListTable.horizontalHeader().setVisible(True)
        self.farmersListTable.horizontalHeader().setCascadingSectionResizes(False)
        self.farmersListTable.horizontalHeader().setDefaultSectionSize(163)
        self.farmersListTable.horizontalHeader().setHighlightSections(False)
        self.gridLayout_2.addWidget(self.farmersListTable, 2, 0, 1, 8)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(distribution)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(19)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.printingList = QtWidgets.QTableWidget(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.printingList.setFont(font)
        self.printingList.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.printingList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.printingList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.printingList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.printingList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.printingList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.printingList.setTabKeyNavigation(False)
        self.printingList.setProperty("showDropIndicator", True)
        self.printingList.setDragEnabled(True)
        self.printingList.setDragDropOverwriteMode(False)
        self.printingList.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.printingList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.printingList.setAlternatingRowColors(True)
        self.printingList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.printingList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.printingList.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.printingList.setCornerButtonEnabled(False)
        self.printingList.setObjectName("printingList")
        self.printingList.setColumnCount(6)
        self.printingList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.printingList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.printingList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.printingList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.printingList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.printingList.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.printingList.setHorizontalHeaderItem(5, item)
        self.printingList.horizontalHeader().setDefaultSectionSize(107)
        self.printingList.horizontalHeader().setHighlightSections(False)
        self.printingList.horizontalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.printingList, 4, 0, 1, 4)
        self.print = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        self.print.setFont(font)
        self.print.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Tunisia))
        self.print.setObjectName("print")
        self.gridLayout.addWidget(self.print, 1, 0, 1, 1)
        self.remove = QtWidgets.QPushButton(self.groupBox)
        self.remove.setObjectName("remove")
        self.gridLayout.addWidget(self.remove, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(distribution)
        QtCore.QMetaObject.connectSlotsByName(distribution)

    def retranslateUi(self, distribution):
        _translate = QtCore.QCoreApplication.translate
        distribution.setWindowTitle(_translate("distribution", "D.P.A التوزيع"))
        self.groupBox_2.setTitle(_translate("distribution", "قائمة الفلاحة"))
        self.displayByDeanships.setText(_translate("distribution", "العمادة"))
        self.displayByCIN.setText(_translate("distribution", "ب.ت.و"))
        self.label.setText(_translate("distribution", "العرض حسب :"))
        self.label_2.setText(_translate("distribution", "اكتب ب.ت.و :"))
        self.label_3.setText(_translate("distribution", "اختار العمادة :"))
        self.searshButton.setText(_translate("distribution", "بحث"))
        self.farmersListTable.setSortingEnabled(True)
        item = self.farmersListTable.horizontalHeaderItem(0)
        item.setText(_translate("distribution", "ب.ت.و"))
        item = self.farmersListTable.horizontalHeaderItem(1)
        item.setText(_translate("distribution", "اسم"))
        item = self.farmersListTable.horizontalHeaderItem(2)
        item.setText(_translate("distribution", "اللقب"))
        item = self.farmersListTable.horizontalHeaderItem(3)
        item.setText(_translate("distribution", "العمادة"))
        self.groupBox.setTitle(_translate("distribution", "اختيار النيابة"))
        self.printingList.setSortingEnabled(True)
        item = self.printingList.horizontalHeaderItem(0)
        item.setText(_translate("distribution", "ب.ت.و"))
        item = self.printingList.horizontalHeaderItem(1)
        item.setText(_translate("distribution", "اسم"))
        item = self.printingList.horizontalHeaderItem(2)
        item.setText(_translate("distribution", "اللقب"))
        item = self.printingList.horizontalHeaderItem(3)
        item.setText(_translate("distribution", "العمادة"))
        item = self.printingList.horizontalHeaderItem(4)
        item.setText(_translate("distribution", "النيابة"))
        item = self.printingList.horizontalHeaderItem(5)
        item.setText(_translate("distribution", "عدد اكيس"))
        self.print.setText(_translate("distribution", "طباعة الوصلات"))
        self.remove.setText(_translate("distribution", "حذف"))
from qrc_source import source

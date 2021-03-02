# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python-project\Administration_agricole\UI\subDistribution.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qrc_source import source
from bin.sync import dataBaseSyncer


class Ui_subDistribution(object):
    def setupUi(self, subDistribution):
        subDistribution.setObjectName("subDistribution")
        subDistribution.setWindowModality(QtCore.Qt.WindowModal)
        subDistribution.resize(277, 122)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        subDistribution.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        subDistribution.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(subDistribution)
        self.gridLayout.setObjectName("gridLayout")
        self.deanship = QtWidgets.QComboBox(subDistribution)
        self.deanship.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deanship.setObjectName("deanship")
        self.gridLayout.addWidget(self.deanship, 0, 0, 1, 1)
        self.number = QtWidgets.QSpinBox(subDistribution)
        self.number.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.number.setAlignment(QtCore.Qt.AlignCenter)
        self.number.setMinimum(1)
        self.number.setMaximum(20)
        self.number.setObjectName("number")
        self.gridLayout.addWidget(self.number, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(subDistribution)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(subDistribution)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.saveCancelButton = QtWidgets.QDialogButtonBox(subDistribution)
        self.saveCancelButton.setOrientation(QtCore.Qt.Horizontal)
        self.saveCancelButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.saveCancelButton.setObjectName("saveCancelButton")
        self.gridLayout.addWidget(self.saveCancelButton, 2, 0, 1, 2)

        self.retranslateUi(subDistribution)
        self.saveCancelButton.accepted.connect(subDistribution.accept)
        self.saveCancelButton.rejected.connect(subDistribution.reject)
        QtCore.QMetaObject.connectSlotsByName(subDistribution)

    def retranslateUi(self, subDistribution):
        _translate = QtCore.QCoreApplication.translate
        subDistribution.setWindowTitle(_translate("subDistribution", "D.P.A التوزيع"))
        self.label_2.setText(_translate("subDistribution", "النيابة :"))
        self.label.setText(_translate("subDistribution", "عدد اكيس :"))


class subDistributionMenu(QtWidgets.QDialog, Ui_subDistribution):
    dataSender = QtCore.pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(subDistributionMenu, self).__init__(parent)
        self.cancelButton = None
        self.saveButton = None
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
        """

        :return:
        """
        self.show()
        self.readDataToProsecutionOfficesComboBox()
        self.cancelButton = self.saveCancelButton.button(QtWidgets.QDialogButtonBox.Cancel)
        self.saveButton = self.saveCancelButton.button(QtWidgets.QDialogButtonBox.Save)
        self.cancelButton.setText('إلغاء')
        self.saveButton.setText('حفظ')

    def Buttons(self):
        """

        :return:
        """
        self.saveButton.clicked.connect(self.save)
        self.cancelButton.clicked.connect(self.close)

    def readDataToProsecutionOfficesComboBox(self) -> None:
        """

        :return:
        """
        self.dataEngine = dataBaseSyncer(f'SELECT NAME_ FROM prosecutionoffices')
        self.dataEngine.start()
        self.dataEngine.Deanshipresult.connect(self.insertDataToProsecutionOfficesComboBox)

    def insertDataToProsecutionOfficesComboBox(self, data: str):
        """

        :param data:  prosecutionOffices Name
        :return:
        """
        self.deanship.addItem(data[2:-3])

    def save(self):
        prosecutionOfficesName = self.deanship.currentText()
        numberOfBags = self.number.value()
        self.dataSender.emit(prosecutionOfficesName, str(numberOfBags))

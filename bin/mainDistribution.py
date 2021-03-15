from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap, QIntValidator
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QRadioButton, QTableWidget, QMessageBox

from bin.worker import TableWorker
from bin.sync import dataBaseSyncer
from bin.distribution import Ui_distribution
from bin.subDistributionM import subDistributionMenu
from bin.printEngine import printingData


class distributionWind(QWidget, Ui_distribution):
    switcher = pyqtSignal()
    events = pyqtSignal(bool)

    def __init__(self):
        super(distributionWind, self).__init__()
        self.rea = None
        self.subDistributionWindow = None
        self.___printEngine = None
        self.dataEngine = None
        self.setupUi(self)
        self.message = QMessageBox()
        self.readDataToDeanshipsComboBox()
        self.tableData()
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        """

        :return:
        """

        self.label_2.setEnabled(True)
        self.searsh.setEnabled(True)
        self.searshButton.setEnabled(True)
        Validator = QIntValidator(00000000, 99999999, self)
        self.searsh.setValidator(Validator)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.message.setWindowIcon(icon)
        self.message.setWindowTitle('تأكيد الحذف')
        self.message.setText('هل تريد حذف')
        self.message.setIcon(QMessageBox.Warning)
        self.message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.yesButtonArabicName = self.message.button(QMessageBox.Yes)
        self.NoButtonArabicName = self.message.button(QMessageBox.No)
        self.yesButtonArabicName.setText('حذف')
        self.NoButtonArabicName.setText('إلغاء')
        self.message.setDefaultButton(QMessageBox.No)
        self.show()

    def Buttons(self) -> None:
        """

        :return:
        """
        self.displayByDeanships.toggled.connect(lambda: self.radioButtonState(self.displayByDeanships))
        self.displayByCIN.toggled.connect(lambda: self.radioButtonState(self.displayByCIN))
        self.searshButton.clicked.connect(lambda: self.searchEngine(self.searsh.text()))
        self.deanships.activated.connect(lambda: self.searchEngine(self.deanships.currentText()))
        self.print.clicked.connect(lambda: self.addDataToHistory(self.printingList))
        self.moveToPrint.clicked.connect(self.itemChanged)
        self.removeFromPrint.clicked.connect(self.removeFromPrintList)

    def getSelectedItem(self) -> str:
        try:
            IDvalue: QTableWidgetItem = self.farmersListTable.selectedItems()[::]
            return IDvalue
        except IndexError as e:
            return 0

    def tableData(self) -> None:
        """

        :return:
        """
        self.farmersListTable.setRowCount(0)
        self.rea = TableWorker(f'SELECT * FROM farmers')
        self.rea.start()
        self.rea.data_.connect(self.tableDataDisplay)
        self.rea.data__.connect(self.insertRow)

    def insertRow(self, row: int) -> None:
        """
        :param row: row number
        :return:
        """
        self.farmersListTable.insertRow(row)

    def tableDataDisplay(self, rowNumber: int, colNumber: int, data: str) -> None:
        """

        :param rowNumber: table Row number
        :param colNumber: table col number
        :param data: row and col content
        :return: None
        """
        if colNumber <= self.farmersListTable.columnCount() - 1:  # TO REMOVE PHONE AND HEAD
            self.farmersListTable.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))

    def readDataToDeanshipsComboBox(self) -> None:
        """

        :return:
        """

        self.dataEngine = dataBaseSyncer(f'SELECT NAME_ FROM DEANSHIPS')
        self.dataEngine.start()
        self.dataEngine.Deanshipresult.connect(self.insertDataToDeanshipsComboBox)

    def insertDataToDeanshipsComboBox(self, data: str) -> None:
        """

        :param data: Deanship name
        :return: None
        """
        self.deanships.addItem(data[2:-4])

    def radioButtonState(self, obj: QRadioButton) -> None:
        """

        :param obj: QRadioButton Object
        :return: None
        """
        if obj.text() == "ب.ت.و":
            if obj.isChecked():
                self.label_2.setEnabled(True)
                self.searsh.setEnabled(True)
                self.searshButton.setEnabled(True)
            else:
                self.label_2.setEnabled(False)
                self.searsh.setEnabled(False)
                self.searshButton.setEnabled(False)
        if obj.text() == "العمادة":
            if obj.isChecked():
                self.label_3.setEnabled(True)
                self.deanships.setEnabled(True)
            else:
                self.label_3.setEnabled(False)
                self.deanships.setEnabled(False)

    def searchEngine(self, key: str) -> None:
        """

        :param key: search key from comboBox or lineEdit if key is alpha search by deanship else search by id(CIN)
        :return: None
        """
        self.farmersListTable.setRowCount(0)

        if key.isalpha():
            self.rea = TableWorker(f"SELECT * FROM farmers WHERE DEANSHIP= '{key}'")
        else:
            self.rea = TableWorker(f'SELECT * FROM farmers WHERE ID= {key}')
        self.rea.start()
        self.rea.data_.connect(self.tableDataDisplay)
        self.rea.data__.connect(self.insertRow)

    def itemChanged(self):
        ___selectedItem = self.getSelectedItem()
        if not ___selectedItem:
            self.setEnabled(False)
            self.message.setWindowTitle('هناك مشكلة')
            self.message.setText('لم يتم تحديد عنصر')
            self.message.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.message.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.message.exec_()
            self.setEnabled(True)
        else:
            self.subDistributionWindow = subDistributionMenu(___selectedItem)
            self.subDistributionWindow.dataSender.connect(self.addTable)

    def addTable(self, result: list) -> None:

        rowNumber = self.printingList.rowCount()
        self.printingList.insertRow(rowNumber)
        for colNumber, data in enumerate(result):
            self.printingList.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))
        self.farmersListTable.removeRow(self.farmersListTable.currentRow())
        self.subDistributionWindow.close()

    def addDataToHistory(self, table: QTableWidget) -> None:
        if self.printingList.rowCount() != 0:
            self.___printEngine = printingData(table)
            self.___printEngine.start()
            self.___printEngine.resetTable.connect(lambda: self.printingList.setRowCount(0))
        else:
            self.setEnabled(False)
            self.message.setWindowTitle('هناك مشكلة')
            self.message.setText('لا توجد عناصر في جدول')
            self.message.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.message.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.message.exec_()
            self.setEnabled(True)
    def removeFromPrintList(self):
        ___selected = self.printingList.selectedItems()[::]
        if self.printingList.rowCount() != 0:
            if not ___selected:
                self.setEnabled(False)
                self.message.setWindowTitle('هناك مشكلة')
                self.message.setText('لم يتم تحديد عنصر')
                self.message.setStandardButtons(QMessageBox.Ok)
                okArabicMessage = self.message.button(QMessageBox.Ok)
                okArabicMessage.setText('موافق')
                self.message.exec_()
                self.setEnabled(True)
            else:
                self.message.setWindowTitle('تأكيد الحذف')
                self.message.setText('هل تريد حذف')
                self.message.setIcon(QMessageBox.Warning)
                self.message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                self.yesButtonArabicName = self.message.button(QMessageBox.Yes)
                self.NoButtonArabicName = self.message.button(QMessageBox.No)
                self.yesButtonArabicName.setText('حذف')
                self.NoButtonArabicName.setText('إلغاء')
                self.message.setDefaultButton(QMessageBox.No)
                self.setEnabled(False)
                self.message.exec_()
                if self.message.clickedButton() == self.yesButtonArabicName:
                    ___row = self.farmersListTable.rowCount()
                    self.insertRow(___row)
                    for ColNumber, data in enumerate(___selected):
                        self.farmersListTable.setItem(___row, ColNumber, QTableWidgetItem(str(data.text())))
                    self.printingList.removeRow(self.printingList.currentRow())
                self.setEnabled(True)
        else:
            self.setEnabled(False)
            self.message.setWindowTitle('هناك مشكلة')
            self.message.setText('لا توجد عناصر في جدول')
            self.message.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.message.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.message.exec_()
            self.setEnabled(True)

    def closeEvent(self, a0: QCloseEvent) -> None:
        """

        :param a0:
        :return:
        """
        self.switcher.emit()
        self.rea.terminate()
        self.dataEngine.terminate()
        try:
            self.___printEngine.terminate()
        except AttributeError:
            pass

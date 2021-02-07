from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtGui import QCloseEvent, QDropEvent, QDragEnterEvent, QDragLeaveEvent
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QRadioButton, QTableWidget

from bin.worker import TableWorker
from bin.sync import dataBaseSyncer
from bin.distribution import Ui_distribution
from bin.subDistributionM import subDistributionMenu


class distributionWind(QWidget, Ui_distribution):
    switcher = pyqtSignal()
    events = pyqtSignal(bool)

    def __init__(self):
        super(distributionWind, self).__init__()
        self.rea = None
        self.subDistributionWindow = None
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        """

        :return:
        """

        self.label_2.setEnabled(True)
        self.searsh.setEnabled(True)
        self.searshButton.setEnabled(True)
        self.show()
        self.tableData()
        self.readDataToDeanshipsComboBox()
        self.printingList.itemChanged.connect(self.itemChanged)

    def Buttons(self) -> None:
        """

        :return:
        """
        self.displayByDeanships.toggled.connect(lambda: self.radioButtonState(self.displayByDeanships))
        self.displayByCIN.toggled.connect(lambda: self.radioButtonState(self.displayByCIN))
        self.searshButton.clicked.connect(lambda: self.searchEngine(self.searsh.text()))
        self.deanships.activated.connect(lambda: self.searchEngine(self.deanships.currentText()))

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

        dataEngine = dataBaseSyncer(f'SELECT NAME_ FROM DEANSHIPS')
        dataEngine.start()
        dataEngine.Deanshipresult.connect(self.insertDataToDeanshipsComboBox)

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

    def itemChanged(self, result):

        self.subDistributionWindow = subDistributionMenu()
        self.subDistributionWindow.dataSender.connect(lambda p, n: self.addValuesToRow(result, p, n))

        """
        if self.farmersListTable.currentRow() != -1:
            CIN = self.farmersListTable.model().index(self.farmersListTable.currentRow(), 0)
            CINDATA = self.farmersListTable.model().data(CIN)
            if CINDATA in self.___addCIN:
                self.events.emit(False)
            else:
                self.events.emit(True)
                self.___addCIN.add(CINDATA)
                print(self.___addCIN)



            print(f'first{self.farmersListTable.model().data(CIN)}')
            secondCIN = self.printingList.model().index(result.row(), 0)
            resultSecondCIN = self.printingList.model().data(secondCIN)
            print(f'secondCIN{resultSecondCIN}')
            """
    def addValuesToRow(self, index: QTableWidgetItem, prosecutionOfficesName: str, number: str) -> None:
        """

        :param index:
        :param prosecutionOfficesName:
        :param number:
        :return:
        """
        self.printingList.setItem(index.row(), 4, QTableWidgetItem(prosecutionOfficesName))
        self.printingList.setItem(index.row(), 5, QTableWidgetItem(number))
        self.subDistributionWindow.close()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """

        :param a0:
        :return:
        """
        self.switcher.emit()

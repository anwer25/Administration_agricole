from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QRadioButton

from bin.worker import TableWorker
from bin.sync import dataBaseSyncer
from bin.distribution import Ui_distribution


class distributionWind(QWidget, Ui_distribution):
    switcher = pyqtSignal()

    def __init__(self):
        super(distributionWind, self).__init__()
        self.rea = None
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
        self.readDataToProsecutionOfficesComboBox()

    def Buttons(self) -> None:
        """

        :return:
        """
        self.displayByDeanships.toggled.connect(lambda: self.radioButtonState(self.displayByDeanships))
        self.displayByCIN.toggled.connect(lambda: self.radioButtonState(self.displayByCIN))
        self.searshButton.clicked.connect(lambda: self.searchEngine(self.searsh.text()))

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

    def readDataToProsecutionOfficesComboBox(self) -> None:
        """

        :return:
        """
        dataEngine = dataBaseSyncer(f'SELECT NAME_ FROM prosecutionoffices')
        dataEngine.start()
        dataEngine.Deanshipresult.connect(self.insertDataToProsecutionOfficesComboBox)

    def insertDataToProsecutionOfficesComboBox(self, data: str):
        """

        :param data:  prosecutionOffices Name
        :return:
        """
        self.prosecutionOffices.addItem(data[2:-3])

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
        if str.isalpha():
            self.rea = TableWorker(f'SELECT * FROM farmers WHERE DEANSHIP= {key}')
        else:
            self.rea = TableWorker(f'SELECT * FROM farmers WHERE ID= {key}')
        self.rea.start()
        self.rea.data_.connect(self.tableDataDisplay)
        self.rea.data__.connect(self.insertRow)

    def closeEvent(self, a0: QCloseEvent) -> None:
        """

        :param a0:
        :return:
        """
        self.switcher.emit()

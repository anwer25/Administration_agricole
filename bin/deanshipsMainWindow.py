from bin.Deanships import Ui_Deanships
from bin.addNewDeanshipMain import addNewDeanshipWindow
from bin.worker import TableWorker
from bin.sync import dataBaseSyncer

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent


class deanships(QWidget, Ui_Deanships):
    displayMainWindow = pyqtSignal()

    def __init__(self):
        super(deanships, self).__init__()
        self.setupUi(self)
        self.UI()
        self.Buttons()
        self.displayData()
        self.addNewDeanshipW = None
        self.databaseEngine = None
        self.tableData = None

    def UI(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.show()
        self.dataTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.dataTable.setSelectionBehavior(QTableWidget.SelectRows)

    def Buttons(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.addNewDeanship.clicked.connect(self.addNewDeanshipWindow)
        self.removeDeanship.clicked.connect(self.removeDeanshipItem)

    def displayData(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.dataTable.setRowCount(0)
        self.tableData = TableWorker(f"SELECT * FROM DEANSHIPS")
        self.tableData.start()
        self.tableData.data__.connect(self.addRow)
        self.tableData.data_.connect(self.addData)

    def addRow(self, row: int) -> None:
        """
        :rtype: None
        :param row: insert row to table
        :return: None
        """
        self.dataTable.insertRow(row)

    def addData(self, rowNumber: int, colNumber: int, data: str) -> None:
        """
        :rtype: None
        :param rowNumber: insert row to table widget
        :param colNumber: insert col to table widget
        :param data: insert data to table widget
        :return: None
        """
        self.dataTable.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))

    def addNewDeanshipWindow(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.addNewDeanshipW = addNewDeanshipWindow()
        self.addNewDeanshipW.refresh.connect(self.displayData)

    def getSelectedItem(self):
        try:
            IDvalue: QTableWidgetItem = self.dataTable.selectedItems()[0]
            return IDvalue.text()
        except IndexError as e:
            # make message here
            print(f'error at line 79 deanshipsMainWindow')

    def removeDeanshipItem(self) -> None:
        """
        :rtype: None
        :return: None
        """
        ID = self.getSelectedItem()
        self.databaseEngine = dataBaseSyncer(f"DELETE FROM DEANSHIPS WHERE NAME_='{ID}'")
        self.databaseEngine.start()
        self.displayData()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        :rtype: None
        :return: None
        """
        self.displayMainWindow.emit()
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

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
        self.show()
        self.tableData()

    def Buttons(self) -> None:
        """

        :return:
        """
        pass

    def tableData(self) -> None:
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
        self.farmersListTable.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.switcher.emit()

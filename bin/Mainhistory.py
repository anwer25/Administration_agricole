from bin.history import Ui_history
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from bin.worker import TableWorker
from bin.mainSearchMethod import mainSearchMethod


class MainHistory(QWidget, Ui_history):
    displayMainWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(MainHistory, self).__init__(parent)
        self.dataBase = None
        self.searchMethodWindow = None
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Buttons(self) -> None:
        """

        :return:
        """
        self.print.clicked.connect(self.printEngine)
        self.remove.clicked.connect(self.removeButton)
        self.searsh.clicked.connect(self.searchEngine)

    def Ui(self) -> None:
        """

        :return:
        """
        self.show()
        self.readData()

    def readData(self, Query: str = f"SELECT * FROM history") -> None:
        """

        :return:
        """

        self.dataBase = TableWorker(Query)
        self.dataBase.start()
        self.dataBase.data__.connect(self.addRow)
        self.dataBase.data_.connect(self.addData)

    def addRow(self, row: int) -> None:
        """

        :param row:
        :return:
        """
        self.data.insertRow(row)

    def addData(self, rowNumber: int, colNumber: int, data: str) -> None:
        """
        :rtype: None
        :param rowNumber: insert row to table widget
        :param colNumber: insert col to table widget
        :param data: insert data to table widget
        :return: None
        """
        self.data.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))

    def printEngine(self) -> None:
        """

        :return:
        """
        pass

    def removeButton(self) -> None:
        """

        :return:
        """
        pass

    def searchEngine(self) -> None:
        """

        :return:
        """
        def result(key):
            print(key)

        self.searchMethodWindow = mainSearchMethod()
        self.searchMethodWindow.result.connect(lambda key: result(key))
        self.setDisabled(True)
        self.searchMethodWindow.Disable.connect(lambda: self.setDisabled(False))

    def closeEvent(self, a0: QCloseEvent) -> None:
        """

        :param a0:
        :return:
        """
        self.displayMainWindow.emit()
        try:
            self.searchMethodWindow.close()
        except AttributeError:
            pass


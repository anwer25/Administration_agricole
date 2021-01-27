from bin.Prosecution_offices import Ui_ProsecutionOffices
from bin.newProsectutionOffices import Ui_Form
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from bin.worker import TableWorker
from bin.sync import dataBaseSyncer


class newProsecution(QWidget, Ui_Form):
    refresh = pyqtSignal()

    def __init__(self):
        super(newProsecution, self).__init__()
        self.setupUi(self)
        self.UI()
        self.Buttons()

    def UI(self):
        self.show()

    def Buttons(self):
        pass


class ProsecutionMain(QWidget, Ui_ProsecutionOffices):
    display = pyqtSignal()

    def __init__(self):
        super(ProsecutionMain, self).__init__()
        self.setupUi(self)
        self.read = None
        self.newProsecutionWindow = None
        self.Ui()
        self.Buttons()
        self.tableRefresh()

    def Ui(self) -> None:
        """

        :return:
        """
        self.show()

    def Buttons(self) -> None:
        """

        :return:
        """
        self.newProsecutionOffices.clicked.connect(self.openNewProsecution)
        self.change.clicked.connect(self.changeWindow)
        self.remove.clicked.connect(self.removeButton)

    def tableRefresh(self):
        self.data.setRowCount(0)
        self.read = TableWorker(f'SELECT * FROM prosecutionoffices')
        self.read.start()
        self.read.data_.connect(self.tableDataDisplay)
        self.read.data__.connect(self.insertRow)

    def insertRow(self, row: int) -> None:
        """

        :param row:
        :return:
        """
        self.data.insertRow(row)

    def tableDataDisplay(self, rowNumber: int, colNumber: int, data: str) -> None:
        """

        :param rowNumber:
        :param colNumber:
        :param data:
        :return:
        """
        self.data.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))

    def getSelectedItem(self) -> str:

        try:
            IDvalue: QTableWidgetItem = self.data.selectedItems()[0]
            return IDvalue.text()
        except IndexError as e:
            print(f'error at line 60 from prosecutionOfficesMain: {e}')

    def openNewProsecution(self) -> None:
        """

        :return:
        """
        self.newProsecutionWindow = newProsecution()

    def changeWindow(self) -> None:
        """

        :return:
        """
        pass

    def removeButton(self) -> None:
        """

        :return:
        """
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

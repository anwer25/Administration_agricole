from bin.Prosecution_offices import Ui_ProsecutionOffices
from bin.newProsectutionOffices import Ui_Form
from bin.changeProsectutionOffices import Ui_changeProsectution

from bin.worker import TableWorker
from bin.sync import dataBaseSyncer

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent


class newProsecution(QWidget, Ui_Form):
    refresh = pyqtSignal()

    def __init__(self):
        super(newProsecution, self).__init__()
        self.setupUi(self)
        self.dataEngine = None
        self.UI()
        self.Buttons()

    def UI(self):
        self.show()

    def Buttons(self):
        self.save.clicked.connect(self.saveEngine)
        self.cancel.clicked.connect(self.close)

    def saveEngine(self):
        self.dataEngine = dataBaseSyncer(f"INSERT INTO prosecutionoffices VALUES ('{self.name.text()}',"
                                         f"'{self.lastName.text()}', '{self.addres.text()}', '{self.phone.text()}')")
        self.dataEngine.start()
        self.dataEngine.refresher.connect(self.refresh.emit)


class changeProsecutionOffice(QWidget, Ui_changeProsectution):
    refresh = pyqtSignal()

    def __init__(self, ID: str):
        super(changeProsecutionOffice, self).__init__()
        self.setupUi(self)
        self.ID = ID
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        """

        :return:
        """
        dataEngine = dataBaseSyncer(f" SELECT * FROM prosecutionoffices where NAME_= '{self.ID}' ")
        dataEngine.start()
        dataEngine.result.connect(self.getData)
        self.show()

    def Buttons(self) -> None:
        """

        :return:
        """
        self.save.clicked.connect(self.saveEngine)
        self.cancel.clicked.connect(self.close)

    def getData(self, data: list) -> None:
        """

        :param data: data from dataBaseSyncer class
        :return:
        """
        self.name.setText(data[0][0])
        self.lastName.setText(data[0][1])
        self.address.setText(data[0][2])
        self.phoneNumber.setText(data[0][3])

    def saveEngine(self):
        """

        :return:
        """
        dataEngine = dataBaseSyncer(f"UPDATE prosecutionoffices SET ADDRESS = '{self.address.text()}',"
                                    f"PHONENUMBER= '{self.phoneNumber.text()}' WHERE NAME_ = '{self.ID}'")
        dataEngine.start()
        dataEngine.refresher.connect(self.refresh.emit)
        self.close()


class ProsecutionMain(QWidget, Ui_ProsecutionOffices):
    display = pyqtSignal()

    def __init__(self):
        super(ProsecutionMain, self).__init__()
        self.setupUi(self)
        self.read = None
        self.newProsecutionWindow = None
        self.changeWindow_ = None
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
        self.remove.clicked.connect(self.removeButton)
        self.change.clicked.connect(self.changeWindow)
        # self.refresh.clicked.connect()

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
        """

        :return: phoneNumber of item selected type str
        """
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
        self.newProsecutionWindow.refresh.connect(self.tableRefresh)

    def changeWindow(self) -> None:
        """

        :return:
        """
        ID = self.getSelectedItem()
        self.changeWindow_ = changeProsecutionOffice(ID)
        self.changeWindow_.refresh.connect(self.tableRefresh)

    def removeButton(self) -> None:
        """

        :return:
        """
        ID = self.getSelectedItem()
        self.read = dataBaseSyncer(f"DELETE FROM prosecutionoffices WHERE NAME_='{ID}'")
        self.read.start()
        self.read.refresher.connect(self.tableRefresh)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()
        self.read.terminate()

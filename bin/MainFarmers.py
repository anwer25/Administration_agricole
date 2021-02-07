from bin.farmers import Ui_farmers
from bin.newFarmersMain import newFMain
from bin.changeMain import changeMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from bin.sync import dataBaseSyncer
from bin.worker import TableWorker


class farmers(QWidget, Ui_farmers):
    display = pyqtSignal()

    def __init__(self):
        super(farmers, self).__init__()
        self.newFarmerWindow = None
        self.dataEngine = None
        self.setupUi(self)
        self.tableRefresh()
        self.conformMessage = QMessageBox()
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        self.show()
        self.data.setEditTriggers(QTableWidget.NoEditTriggers)
        self.data.setSelectionBehavior(QTableWidget.SelectRows)

        self.conformMessage.setWindowTitle('تأكيد الحذف')
        self.conformMessage.setText('هل تريد حذف')
        self.conformMessage.setIcon(QMessageBox.Warning)
        self.conformMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.yesButtonArabicName = self.conformMessage.button(QMessageBox.Yes)
        self.NoButtonArabicName = self.conformMessage.button(QMessageBox.No)
        self.yesButtonArabicName.setText('حذف')
        self.NoButtonArabicName.setText('إلغاء')
        self.conformMessage.setDefaultButton(QMessageBox.No)

    def Buttons(self) -> None:
        self.new_.clicked.connect(self.addNewFarmer)
        self.change.clicked.connect(self.changeFarmer)
        self.remove.clicked.connect(self.deleteFarmer)
        self.print.clicked.connect(self.printTicket)

    def tableRefresh(self):
        """
        self.data_ = dataBaseSyncer('SELECT * FROM FARMERS')
        self.data_.start()
        self.data_.result.connect(self.tableDataDisplay)
        """
        self.data.setRowCount(0)
        self.read = TableWorker('SELECT * FROM FARMERS')
        self.read.start()
        self.read.data_.connect(self.tableDataDisplay)
        self.read.data__.connect(self.insertrow)

    def insertrow(self, row: int):
        self.data.insertRow(row)

    def tableDataDisplay(self, rowNumber: int, colNumber: int, data: str) -> None:
        """
        self.data.setRowCount(0)
        for rowNumber, rowData in enumerate(data):
            self.data.insertRow(rowNumber)
            for colNumber, data in enumerate(rowData):
                self.data.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))
        """

        self.data.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))

    def getSelectedItem(self) -> str:
        try:
            IDvalue: QTableWidgetItem = self.data.selectedItems()[0]
            return IDvalue.text()
        except IndexError as e:
            # make message here
            print(f'error at line 45 mainFarmers {e}')

    def addNewFarmer(self) -> None:
        self.newFarmerWindow = newFMain()
        self.newFarmerWindow.refresh.connect(self.tableRefresh)

    def changeFarmer(self) -> None:
        id = self.getSelectedItem()
        self.changeWindow = changeMainWindow(id)
        self.changeWindow.refrech.connect(self.tableRefresh)

    def deleteFarmer(self) -> None:
        id = self.getSelectedItem()
        self.conformMessage.exec_()
        if self.conformMessage.clickedButton() == self.yesButtonArabicName:
            self.dataEngine = dataBaseSyncer(f'DELETE FROM FARMERS WHERE ID= {id}')
            self.dataEngine.start()
            self.dataEngine.refresher.connect(self.tableRefresh)
        else:
            pass

    def printTicket(self) -> None:
        id = self.getSelectedItem()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

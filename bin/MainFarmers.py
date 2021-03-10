from bin.farmers import Ui_farmers
from bin.newFarmersMain import newFMain
from bin.changeMain import changeMainWindow
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap
from bin.worker import TableWorker, dataBaseS
from bin.printEngine import printFarmersAndHistoryData
import sys
from qrc_source import source


class farmers(QWidget, Ui_farmers):
    display = pyqtSignal()

    def __init__(self):
        super(farmers, self).__init__()
        self.newFarmerWindow = None
        self.dataEngine = None
        self.yesButtonArabicName = None
        self.NoButtonArabicName = None
        self.changeWindow = None
        self.read = None
        self.newFarmerWindowStateV = False
        self.changeWindowStateV = False
        self.printEngine = None
        self.setupUi(self)
        self.tableRefresh()
        self.conformMessage = QMessageBox()
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        self.show()
        self.data.setEditTriggers(QTableWidget.NoEditTriggers)
        self.data.setSelectionBehavior(QTableWidget.SelectRows)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.conformMessage.setWindowIcon(icon)
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

    def tableRefresh(self) -> None:
        self.data.setRowCount(0)
        self.read = TableWorker('SELECT * FROM FARMERS')
        self.read.start()
        self.read.data_.connect(self.tableDataDisplay)
        self.read.data__.connect(self.insertrow)

    def insertrow(self, row: int) -> None:
        self.data.insertRow(row)

    def tableDataDisplay(self, rowNumber: int, colNumber: int, data: str) -> None:
        self.data.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))

    def getSelectedItem(self) -> str:
        try:
            IDvalue: QTableWidgetItem = self.data.selectedItems()[0]
            return IDvalue.text()
        except IndexError as e:
            self.conformMessage.setWindowTitle('هناك مشكلة')
            self.conformMessage.setText('لم يتم تحديد عنصر')
            self.conformMessage.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.conformMessage.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.conformMessage.exec_()
            return 0

    def addNewFarmer(self) -> None:
        self.setEnabled(False)
        self.newFarmerWindowStateV = True
        self.newFarmerWindow = newFMain()
        self.newFarmerWindow.refresh.connect(self.tableRefresh)
        self.newFarmerWindow.enableMain.connect(lambda: self.setEnabled(True))
        self.newFarmerWindow.newFarmerWindowState.connect(lambda i: self.___newFarmerWindowState(i))

    def changeFarmer(self) -> None:
        id = self.getSelectedItem()
        if id:
            self.setEnabled(False)
            self.changeWindowStateV = True
            self.changeWindow = changeMainWindow(id)
            self.changeWindow.refrech.connect(self.tableRefresh)
            self.changeWindow.enableMain.connect(lambda: self.setEnabled(True))
            self.changeWindow.changeWindowState.connect(lambda i: self.___changeWindowState(i))

    def deleteFarmer(self) -> None:
        self.setEnabled(False)
        id = self.getSelectedItem()
        if id:
            self.conformMessage.exec_()
            if self.conformMessage.clickedButton() == self.yesButtonArabicName:
                self.dataEngine = dataBaseS(f'DELETE FROM FARMERS WHERE ID= {id}')
                self.dataEngine.connector()
                self.tableRefresh()
        self.setEnabled(True)

    def printTicket(self) -> None:
        if self.data.rowCount():
            ___printData = printFarmersAndHistoryData('SELECT * FROM farmers')
        else:
            self.setEnabled(False)
            self.conformMessage.setWindowTitle('هناك مشكلة')
            self.conformMessage.setText('لا توجد عناصر في جدول')
            self.conformMessage.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.conformMessage.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.conformMessage.exec_()
            self.setEnabled(True)

    def ___newFarmerWindowState(self, state: bool) -> None:
        self.___newFarmerWindowStateV = state

    def ___changeWindowState(self, state: bool) -> None:
        self.___changeWindowStateV = state

    def closeEvent(self, a0: QCloseEvent) -> None:
        if self.newFarmerWindowStateV:
            self.newFarmerWindow.close()
        if self.changeWindowStateV:
            self.changeWindow.close()
        self.read.terminate()
        self.display.emit()

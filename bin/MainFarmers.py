from bin.farmers import Ui_farmers
from bin.newFarmersMain import newFMain
from bin.changeMain import changeMainWindow
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap
from bin.worker import TableWorker, dataBaseS
from qrc_source import source


class farmers(QWidget, Ui_farmers):
    display = pyqtSignal()

    def __init__(self):
        super(farmers, self).__init__()
        self.newFarmerWindow = None
        self.dataEngine = None
        self.setupUi(self)
        self.tableRefresh()
        self.conformMessage = QMessageBox()
        self.yesButtonArabicName = None
        self.NoButtonArabicName = None
        self.changeWindow = None
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
        read = TableWorker('SELECT * FROM FARMERS')
        read.start()
        read.data_.connect(self.tableDataDisplay)
        read.data__.connect(self.insertrow)

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
        self.newFarmerWindow = newFMain()
        self.newFarmerWindow.refresh.connect(self.tableRefresh)
        self.newFarmerWindow.enableMain.connect(lambda: self.setEnabled(True))

    def changeFarmer(self) -> None:
        self.setEnabled(False)
        id = self.getSelectedItem()
        if id:
            self.changeWindow = changeMainWindow(id)
            self.changeWindow.refrech.connect(self.tableRefresh)
        self.setEnabled(True)

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
        self.setEnabled(False)
        if self.data.rowCount():
            pass
        else:
            self.conformMessage.setWindowTitle('هناك مشكلة')
            self.conformMessage.setText('لا توجد عناصر في جدول')
            self.conformMessage.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.conformMessage.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.conformMessage.exec_()
        self.setEnabled(False)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

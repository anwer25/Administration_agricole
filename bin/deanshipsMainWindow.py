from bin.Deanships import Ui_Deanships
from bin.addNewDeanshipMain import addNewDeanshipWindow
from bin.worker import TableWorker, dataBaseS

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap
from qrc_source import source


class deanships(QWidget, Ui_Deanships):
    displayMainWindow = pyqtSignal()

    def __init__(self):
        super(deanships, self).__init__()
        self.setupUi(self)
        self.addNewDeanshipW = None
        self.databaseEngine = None
        self.tableData = None
        self.conformMessage = QMessageBox()
        self.UI()
        self.Buttons()
        self.displayData()

    def UI(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.show()
        self.dataTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.dataTable.setSelectionBehavior(QTableWidget.SelectRows)
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
        self.setEnabled(False)
        self.addNewDeanshipW = addNewDeanshipWindow()
        self.addNewDeanshipW.refresh.connect(self.displayData)
        self.addNewDeanshipW.enableWindow.connect(lambda: self.setEnabled(True))

    def getSelectedItem(self):
        try:
            IDvalue: QTableWidgetItem = self.dataTable.selectedItems()[0]
            return IDvalue.text()
        except IndexError as e:
            self.conformMessage.setWindowTitle('هناك مشكلة')
            self.conformMessage.setText('لم يتم تحديد عنصر')
            self.conformMessage.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.conformMessage.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.conformMessage.exec_()

    def removeDeanshipItem(self) -> None:
        """
        :rtype: None
        :return: None
        """
        ID = self.getSelectedItem()
        self.setEnabled(False)
        if ID:
            self.conformMessage.exec_()
            if self.conformMessage.clickedButton() == self.yesButtonArabicName:
                self.databaseEngine = dataBaseS(f"DELETE FROM DEANSHIPS WHERE NAME_='{ID}'")
                self.databaseEngine.connector()
                self.displayData()
        self.setEnabled(True)

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        :rtype: None
        :return: None
        """
        try:
            self.addNewDeanshipW.close()
        except AttributeError:
            pass
        finally:
            self.tableData.terminate()
            self.displayMainWindow.emit()
            self.tableData.terminate()

from bin.history import Ui_history
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap
from bin.printEngine import printFarmersAndHistoryData
from bin.worker import TableWorker
from bin.mainSearchMethod import mainSearchMethod


class MainHistory(QWidget, Ui_history):
    displayMainWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(MainHistory, self).__init__(parent)
        self.dataBase = None
        self.searchMethodWindow = None
        self.___printData = None
        self.conformMessage = QMessageBox()
        self.errorMessage = QMessageBox()
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Buttons(self) -> None:
        """

        :return:
        """
        self.print.clicked.connect(self.handlePreview)
        self.remove.clicked.connect(self.removeButton)
        self.searsh.clicked.connect(self.searchEngine)

    def Ui(self) -> None:
        """

        :return:
        """
        self.show()
        self.readData()
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.errorMessage.setWindowIcon(icon)
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

    def readData(self, Query: str = f"SELECT * FROM history") -> None:
        """

        :return:
        """

        self.data.setRowCount(0)
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

    def handlePreview(self) -> None:
        """

        :return:
        """
        if self.data.rowCount():
            self.___printData = printFarmersAndHistoryData('SELECT * FROM history', f=1)
        else:
            self.setEnabled(False)
            self.errorMessage.setWindowTitle('هناك مشكلة')
            self.errorMessage.setText('لا توجد عناصر في جدول')
            self.errorMessage.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.errorMessage.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.errorMessage.exec_()
            self.setEnabled(True)

    def removeButton(self) -> None:
        """

        :return:
        """
        # TODO: Make conform Message here
        self.setEnabled(False)
        self.conformMessage.exec_()
        if self.conformMessage.clickedButton() == self.yesButtonArabicName:
            self.readData(f"DELETE FROM history")
        self.setEnabled(True)

    def searchEngine(self) -> None:
        """

        :return:
        """

        def result(key: list):
            self.searchMethodWindow.close()
            _start: list = key[0].split('/')
            ___monthesHaveThertyOneDays: list = ['01', '03', '05', '07', '08', '10', '12']
            ___monthesHaveThertyDays: list = ['04', '06', '09', '11']
            day = _start[0]
            month = _start[1]
            year = _start[2]
            if day == '01':
                if month == '01':
                    year = int(year)-1
                    month = '12'
                    day = '31'
                else:
                    month = int(month)-1
                    if len(str(month)) == 1:
                        month = '0'+str(month)
                    day = '31' if month in ___monthesHaveThertyOneDays else '30' \
                        if month in ___monthesHaveThertyDays else '29'
            else:
                day = int(day) - 1
                if len(str(day)) == 1:
                    day = '0'+str(day)


            date = [day, month, year]
            ___result = '/'.join(map(str, date))
            Query = f"SELECT * FROM history WHERE CIN='{key[0]}'" if len(key) == 1 else \
                f"SELECT * FROM history WHERE DATE_ BETWEEN '{___result}' AND '{key[1]}'" if len(key) == 2 else \
                    f"SELECT * FROM history"
            self.readData(Query)

        self.setEnabled(False)
        self.searchMethodWindow = mainSearchMethod()
        self.searchMethodWindow.result.connect(result)
        self.searchMethodWindow.Disable.connect(lambda: self.setEnabled(True))

    def closeEvent(self, a0: QCloseEvent) -> None:
        """

        :param a0:
        :return:
        """

        try:
            self.searchMethodWindow.close()
        except AttributeError:
            pass
        finally:
            self.dataBase.terminate()
            self.displayMainWindow.emit()

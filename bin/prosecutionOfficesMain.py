from bin.Prosecution_offices import Ui_ProsecutionOffices
from bin.newProsectutionOffices import Ui_Form
from bin.changeProsectutionOffices import Ui_changeProsectution

from bin.worker import TableWorker, dataBaseS

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap, QIntValidator


class newProsecution(QWidget, Ui_Form):
    refresh = pyqtSignal()
    enable = pyqtSignal()

    def __init__(self):
        super(newProsecution, self).__init__()
        self.dataEngine = None
        self.message = QMessageBox()
        self.setupUi(self)
        self.UI()
        self.Buttons()

    def UI(self):
        Validator = QIntValidator(00000000, 99999999, self)
        self.phone.setValidator(Validator)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.message.setWindowIcon(icon)
        self.message.setWindowTitle('خطأ عند الحفظ')
        self.message.setText('يوجد صندوق فارغ')
        self.message.setIcon(QMessageBox.Warning)
        self.message.setStandardButtons(QMessageBox.Ok)
        self.OkButtonArabicName = self.message.button(QMessageBox.Ok)
        self.OkButtonArabicName.setText('موافق')
        self.message.setDefaultButton(QMessageBox.Ok)
        self.show()

    def Buttons(self):
        self.save.clicked.connect(self.saveEngine)
        self.cancel.clicked.connect(self.close)

    def saveEngine(self):
        if self.name.text() and self.lastName.text() and self.addres.text() and self.phone.text() != '':
            self.dataEngine = dataBaseS(f"INSERT INTO prosecutionoffices VALUES ('{self.name.text()}',"
                                        f"'{self.lastName.text()}', '{self.addres.text()}', '{self.phone.text()}')")
            self.dataEngine.connector()
            self.refresh.emit()
            self.lastName.clear()
            self.addres.clear()
            self.phone.clear()
            self.name.clear()
        else:
            self.message.exec_()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.enable.emit()


class changeProsecutionOffice(QWidget, Ui_changeProsectution):
    refresh = pyqtSignal()
    enable = pyqtSignal()

    def __init__(self, ID: str):
        super(changeProsecutionOffice, self).__init__()
        self.message = QMessageBox()
        self.setupUi(self)
        self.ID = ID
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        """

        :return:
        """
        Validator = QIntValidator(00000000, 99999999, self)
        self.phoneNumber.setValidator(Validator)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.message.setWindowIcon(icon)
        self.message.setWindowTitle('خطأ عند الحفظ')
        self.message.setText('يوجد صندوق فارغ')
        self.message.setIcon(QMessageBox.Warning)
        self.message.setStandardButtons(QMessageBox.Ok)
        self.OkButtonArabicName = self.message.button(QMessageBox.Ok)
        self.OkButtonArabicName.setText('موافق')
        self.message.setDefaultButton(QMessageBox.Ok)
        dataEngine = dataBaseS(f" SELECT * FROM prosecutionoffices where NAME_= '{self.ID}' ")
        self.getData(dataEngine.connector())
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
        if self.address.text() and self.phoneNumber.text() != '':
            dataEngine = dataBaseS(f"UPDATE prosecutionoffices SET ADDRESS = '{self.address.text()}',"
                                   f"PHONENUMBER= '{self.phoneNumber.text()}' WHERE NAME_ = '{self.ID}'")
            dataEngine.connector()
            self.refresh.emit()
            self.close()
        else:
            self.message.exec_()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.enable.emit()


class ProsecutionMain(QWidget, Ui_ProsecutionOffices):
    display = pyqtSignal()

    def __init__(self):
        super(ProsecutionMain, self).__init__()
        self.setupUi(self)
        self.read = None
        self.newProsecutionWindow = None
        self.changeWindow_ = None
        self.conformMessage = QMessageBox()
        self.Ui()
        self.Buttons()
        self.tableRefresh()

    def Ui(self) -> None:
        """

        :return:
        """
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
            self.conformMessage.setWindowTitle('هناك مشكلة')
            self.conformMessage.setText('لم يتم تحديد عنصر')
            self.conformMessage.setStandardButtons(QMessageBox.Ok)
            okArabicMessage = self.conformMessage.button(QMessageBox.Ok)
            okArabicMessage.setText('موافق')
            self.conformMessage.exec_()
            return 0

    def openNewProsecution(self) -> None:
        """

        :return:
        """
        self.setEnabled(False)
        self.newProsecutionWindow = newProsecution()
        self.newProsecutionWindow.refresh.connect(self.tableRefresh)
        self.newProsecutionWindow.enable.connect(lambda: self.setEnabled(True))

    def changeWindow(self) -> None:
        """

        :return:
        """
        ID = self.getSelectedItem()
        if ID:
            self.setEnabled(False)
            self.changeWindow_ = changeProsecutionOffice(ID)
            self.changeWindow_.refresh.connect(self.tableRefresh)
            self.changeWindow_.enable.connect(lambda: self.setEnabled(True))

    def removeButton(self) -> None:
        """

        :return:
        """
        self.setEnabled(False)
        ID = self.getSelectedItem()
        if ID:
            self.conformMessage.exec_()
            if self.conformMessage.clickedButton() == self.yesButtonArabicName:
                self.read = dataBaseS(f"DELETE FROM prosecutionoffices WHERE NAME_='{ID}'")
                self.read.connector()
                self.tableRefresh()
        self.setEnabled(True)

    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            self.newProsecutionWindow.close()
        except AttributeError:
            try:
                self.changeWindow_.close()
            except AttributeError:
                pass
        finally:
            self.display.emit()
            self.read.terminate()

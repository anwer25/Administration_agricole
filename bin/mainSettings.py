from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSignal, QSettings
from PyQt5.QtGui import QCloseEvent, QPixmap, QIcon
import mysql.connector
from bin.mysqlError import mysqlError
from bin.settings import Ui_settings
from bin.worker import TableWorker, dataBaseS
from bin.mainAddNewUser import mainAddNewUser
from bin.mainChangeUserData import mainChangeUserData
from qrc_source import source


class mainSettings(QWidget, Ui_settings):
    displayMainWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(mainSettings, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.conformMessage = QMessageBox()
        self.normalMessage = QMessageBox()
        self.NewUserWindow = None
        self.fileLocation = None
        self.userModifier = None
        self.tableRefresher()
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        """

        :return:
        """
        self.dbUserName.setText(self.settings.value('DATABASE_USER_NAME', 'root', str))
        self.dbPassword.setText(self.settings.value('DATABASE_PASSWORD', 'admin', str))
        self.dbHost.setText(self.settings.value('DATABASE_HOST', 'localhost', str))
        self.tableName.setText(self.settings.value('DATABASE_NAME', 'administration-agricole'))
        self.show()
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.normalMessage.setWindowIcon(icon)
        self.conformMessage.setWindowIcon(icon)
        self.normalMessage.setStandardButtons(QMessageBox.Ok)
        self.normalMessage.setIcon(QMessageBox.Information)
        okArabicMessage = self.normalMessage.button(QMessageBox.Ok)
        okArabicMessage.setText('موافق')
        self.conformMessage.setWindowTitle('تأكيد الحذف')
        self.conformMessage.setText('هل تريد حذف')
        self.conformMessage.setIcon(QMessageBox.Warning)
        self.conformMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.yesButtonArabicName = self.conformMessage.button(QMessageBox.Yes)
        self.NoButtonArabicName = self.conformMessage.button(QMessageBox.No)
        self.yesButtonArabicName.setText('حذف')
        self.NoButtonArabicName.setText('إلغاء')
        self.conformMessage.setDefaultButton(QMessageBox.No)

    def Buttons(self):
        self.testConnection.clicked.connect(self._testConnection)
        self.delete_2.clicked.connect(self.deleteUser)
        self.addNewUser.clicked.connect(self.addNewUserWindow)
        self.modifieUser.clicked.connect(self._Usermodifier)
        self.saveData.clicked.connect(self._saveData)

    def _testConnection(self) -> None:
        """

        :return:
        """
        config = {
            'user': self.dbUserName.text(),
            'password': self.dbPassword.text(),
            'host': self.dbHost.text(),
            'database': self.tableName.text(),
            'raise_on_warnings': True
        }
        try:
            connection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            mysqlerror = mysqlError(err)
            self.normalMessage.setWindowTitle('تحقق من نتيجة الاختبار')
            self.normalMessage.setText(mysqlerror.__str__())
            self.normalMessage.exec_()
        else:
            self.normalMessage.setWindowTitle('تحقق من نتيجة الاختبار')
            self.normalMessage.setText('نجح الاتصال ، يمكنك حفظ الإعدادات')
            self.normalMessage.exec_()

    def tableRefresher(self):
        self.usersTable.setRowCount(0)
        self.read = TableWorker(f'SELECT * FROM users')
        self.read.start()
        self.read.data_.connect(lambda row, col, data: self.tableDataDisplay(row, col, data))
        self.read.data__.connect(lambda i: self.insertRow(i))

    def insertRow(self, row: int):
        self.usersTable.insertRow(row)

    def tableDataDisplay(self, row: int, col: int, data: str):
        result = 'نعم' if data == '1' else 'لا' if data == '0' else data
        self.usersTable.setItem(row, col, QTableWidgetItem(result))

    def _saveData(self):
        try:
            config = {
                'user': self.dbUserName.text(),
                'password': self.dbPassword.text(),
                'host': self.dbHost.text(),
                'database': self.tableName.text(),
                'raise_on_warnings': True
            }
            connection = mysql.connector.connect(**config)
        except mysql.connector.errors as err:
            mysqlerror = mysqlError(err)
            self.normalMessage.setWindowTitle('تحقق من نتيجة الاختبار')
            self.normalMessage.setText(mysqlerror.__str__())
            self.normalMessage.exec_()
        else:
            self.settings.setValue('DATABASE_USER_NAME', self.dbUserName.text())
            self.settings.setValue('DATABASE_PASSWORD', self.dbPassword.text())
            self.settings.setValue('DATABASE_HOST', self.dbHost.text())
            self.settings.setValue('DATABASE_NAME', self.tableName.text())
            self.settings.sync()
            self.normalMessage.setWindowTitle('حفظ الإعدادات')
            self.normalMessage.setText('تم حفظ الإعدادات بنجاح')
            self.normalMessage.exec_()

    def getSelectedItem(self) -> tuple:
        try:
            IDvalue: QTableWidgetItem = self.usersTable.selectedItems()[0]
            _IDvalue: QTableWidgetItem = self.usersTable.selectedItems()[3]
            return IDvalue.text(), _IDvalue.text()
        except IndexError as e:
            self.normalMessage.setWindowTitle('هناك مشكلة')
            self.normalMessage.setText('لم يتم تحديد عنصر')
            self.normalMessage.exec_()
            return 0

    def addNewUserWindow(self):
        self.NewUserWindow: mainAddNewUser = mainAddNewUser()
        self.setEnabled(False)
        self.NewUserWindow.display.connect(lambda: self.setEnabled(True))
        self.NewUserWindow.refresher.connect(self.tableRefresher)

    def _Usermodifier(self):
        selectedItem = self.getSelectedItem()
        if selectedItem:
            self.userModifier: mainChangeUserData = mainChangeUserData(selectedItem)
            self.setEnabled(False)
            self.userModifier.display.connect(lambda: self.setEnabled(True))
            self.userModifier.refresher.connect(self.tableRefresher)

    def deleteUser(self):
        selectedItem = self.getSelectedItem()
        self.setEnabled(False)
        if selectedItem:
            if selectedItem[1] != 'نعم':
                self.conformMessage.exec_()
                if self.conformMessage.clickedButton() == self.yesButtonArabicName:
                    engine = dataBaseS(f"DELETE FROM users WHERE USER_='{selectedItem[0]}'")
                    engine.connector()
                    self.tableRefresher()
            else:
                self.normalMessage.setWindowTitle('هناك مشكلة')
                self.normalMessage.setText('لا يمكنك حذف حساب المسؤول')
                self.normalMessage.exec_()
        self.setEnabled(True)

    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            self.NewUserWindow.close()
        except AttributeError:
            try:
                self.userModifier.close()
            except AttributeError:
                pass
        finally:
            self.displayMainWindow.emit()
            self.read.terminate()

from PyQt5.QtWidgets import QWidget, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal, QSettings
from PyQt5.QtGui import QCloseEvent
import mysql.connector
from bin.mysqlError import mysqlError
from bin.settings import Ui_settings
from bin.worker import TableWorker, dataBaseS
from bin.mainAddNewUser import mainAddNewUser
from bin.mainChangeUserData import mainChangeUserData


class mainSettings(QWidget, Ui_settings):
    displayMainWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(mainSettings, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
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
            mysqlerror.errorType.connect(lambda i: print(f'{i} main settings file'))
        else:
            pass

    def tableRefresher(self):
        # TODO: fix thread big
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
            mysqlerror.errorType.connect(lambda i: print(f'{i} main settings file'))
        else:
            if connection.is_connected():
                self.settings.setValue('DATABASE_USER_NAME', self.dbUserName.text())
                self.settings.setValue('DATABASE_PASSWORD', self.dbPassword.text())
                self.settings.setValue('DATABASE_HOST', self.dbHost.text())
                self.settings.setValue('DATABASE_NAME', self.tableName.text())
                self.settings.sync()

    def getSelectedItem(self) -> str:
        try:
            IDvalue: QTableWidgetItem = self.usersTable.selectedItems()[0]
            return IDvalue.text()
        except IndexError as e:
            # make message here
            print(f'error at line 96 mainSettings {e}')

    def addNewUserWindow(self):
        self.NewUserWindow: mainAddNewUser = mainAddNewUser()
        self.setEnabled(False)
        self.NewUserWindow.display.connect(lambda: self.setEnabled(True))
        self.NewUserWindow.refresher.connect(self.tableRefresher)

    def _Usermodifier(self):
        self.userModifier: mainAddNewUser = mainChangeUserData(self.getSelectedItem())
        self.setEnabled(False)
        self.userModifier.display.connect(lambda: self.setEnabled(True))
        self.userModifier.refresher.connect(self.tableRefresher)

    def deleteUser(self):
        selectedItem = self.getSelectedItem()
        # TODO: make conform message here
        engine = dataBaseS(f"DELETE FROM users WHERE USER_='{selectedItem}'")
        engine.connector()
        self.tableRefresher()
        # TODO: check if the are more than one user to delete if there are les than 2 this function doesn't work and
        #  display message

    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            self.NewUserWindow.close()
        except AttributeError:
            pass
        finally:
            self.displayMainWindow.emit()
            self.read.terminate()

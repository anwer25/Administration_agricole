from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal, QSettings
import mysql.connector
from bin.conf import Ui_config
from bin.mysqlError import mysqlError


class mainConfig(QMainWindow, Ui_config):
    changeWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(mainConfig, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()

    def Buttons(self):
        self.cancel.clicked.connect(self.close)

    def saveData(self):
        try:
            config = {
                'user': self.dbUserName.text(),
                'password': self.dbPassword.text(),
                'host': self.dbHost.text(),
                'raise_on_warnings': True
            }
            connection = mysql.connector.connect(**config)
        except mysql.connector.errors as err:
            ___mysqlError = mysqlError(err)
            ___mysqlError.errorType.connect(lambda i: print(f'{i} configWindow'))
        else:
            if connection.is_connected():
                self.settings.setValue('DATABASE_USER_NAME', self.dbUserName.text())
                self.settings.setValue('DATABASE_PASSWORD', self.dbPassword.text())
                self.settings.setValue('DATABASE_HOST', self.dbHost.text())
                self.settings.sync()
                self.changeWindow.emit()
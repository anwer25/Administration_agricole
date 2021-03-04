from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSettings
import mysql.connector
from bin.conf import Ui_config
from bin.mysqlError import mysqlError


class mainConfig(QMainWindow, Ui_config):

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
        self.save.clicked.connect(self.saveData)

    def saveData(self):
        try:
            config = {
                'user': self.dbUserName.text(),
                'password': self.dbPassword.text(),
                'host': self.dbHost.text(),
                'raise_on_warnings': True
            }
            connection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            ___mysqlError = mysqlError(err)
            print(___mysqlError.__str__())
        else:
            def ___dataBaseBuilder(con: mysql.connector.connect):
                pass
            if connection.is_connected():
                self.settings.setValue('DATABASE_USER_NAME', self.dbUserName.text())
                self.settings.setValue('DATABASE_PASSWORD', self.dbPassword.text())
                self.settings.setValue('DATABASE_HOST', self.dbHost.text())
                self.settings.setValue('DATABASE_NAME', self.dataBaseName.text())
                self.settings.sync()
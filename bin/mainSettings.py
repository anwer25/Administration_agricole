from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import pyqtSignal, QSettings
from PyQt5.QtGui import QCloseEvent
import mysql.connector
from bin.mysqlError import mysqlError
from bin.settings import Ui_settings


class mainSettings(QWidget, Ui_settings):
    displayMainWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(mainSettings, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.fileLocation = None
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
        self.dataBaseBackUpFileLoction.clicked.connect(self.openSaveFileLocation)

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

    def openSaveFileLocation(self):
        self.fileLocation = QFileDialog.getSaveFileName(self, 'موقع حفظ الملف')
        print(self.fileLocation)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.displayMainWindow.emit()

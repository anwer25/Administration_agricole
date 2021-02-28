from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QSettings
from PyQt5.QtGui import QCloseEvent
from bin.settings import Ui_settings


class mainSettings(QWidget, Ui_settings):
    displayMainWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(mainSettings, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
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
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.displayMainWindow.emit()

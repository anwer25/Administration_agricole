from bin.addNewDeanShip import Ui_addNewDeanShip
from bin.sync import dataBaseSyncer

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent


class addNewDeanshipWindow(QWidget, Ui_addNewDeanShip):
    refresh = pyqtSignal()

    def __init__(self):
        super(addNewDeanshipWindow, self).__init__()
        self.setupUi(self)
        self.Ui()
        self.Buttons()
        self.databaseEngine = None

    def Ui(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.show()

    def Buttons(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.save.clicked.connect(self.saveData)

    def saveData(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.databaseEngine = dataBaseSyncer(f"INSERT INTO DEANSHIPS VALUES('{self.deanshipName.text()}',"
                                             f"{self.population.text()})")
        self.databaseEngine.start()
        self.databaseEngine.refresher.connect(self.refresh.emit)
        self.deanshipName.clear()
        self.population.clear()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        :rtype: None
        :return: None
        """
        self.refresh.emit()

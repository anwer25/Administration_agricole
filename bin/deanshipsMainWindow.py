from bin.Deanships import Ui_Deanships
from bin.worker import dataBaseS
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent


class deanships(QWidget, Ui_Deanships):
    displayMainWindow = pyqtSignal()

    def __init__(self):
        super(deanships, self).__init__()
        self.setupUi(self)
        self.UI()
        self.Buttons()
        self.displayData()

    def UI(self) -> None:
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
        self.addNewDeanship.clicked.connect(self.addNewDeanshipWindow)
        self.removeDeanship.clicked.connect(self.removeDeanshipItem)

    def displayData(self) -> None:
        """
        :rtype: None
        :return: None
        """
        pass

    def addNewDeanshipWindow(self) -> None:
        """
        :rtype: None
        :return: None
        """
        pass

    def removeDeanshipItem(self) -> None:
        """
        :rtype: None
        :return: None
        """
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        :rtype: None
        :return: None
        """
        self.displayMainWindow.emit()
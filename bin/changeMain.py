from bin.change import Ui_change
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from bin.sync import dataBaseSyncer


class changeMainWindow(QWidget, Ui_change):
    refrech = pyqtSignal()

    def __init__(self, id: str = None):
        super(changeMainWindow, self).__init__()
        self.id = id
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
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
        self.cancel.clicked.connect(self.close)

    def saveData(self) -> None:
        """
        :rtype: None
        :return: None
        """
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:

        self.refrech.emit()
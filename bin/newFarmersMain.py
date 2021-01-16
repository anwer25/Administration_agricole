from bin.newFarmers import Ui_newFarmers
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent


class newFMain(QWidget, Ui_newFarmers):
    refresh = pyqtSignal()

    def __init__(self):
        super(newFMain, self).__init__()
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        self.show()

    def Buttons(self):
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.refresh.emit()

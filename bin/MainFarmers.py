from bin.farmers import Ui_farmers
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class farmers(QWidget, Ui_farmers):
    display = pyqtSignal()

    def __init__(self):
        super(farmers, self).__init__()
        self.setupUi(self)
        # self.username = username
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()

    def Buttons(self):
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

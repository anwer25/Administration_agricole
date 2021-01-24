from bin.Prosecution_offices import Ui_ProsecutionOffices
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent


class ProsecutionMain(QWidget, Ui_ProsecutionOffices):
    display = pyqtSignal()

    def __init__(self):
        super(ProsecutionMain, self).__init__()
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        """

        :return:
        """
        self.show()

    def Buttons(self) -> None:
        """

        :return:
        """
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

from bin.history import Ui_history
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent


class MainHistory(QWidget, Ui_history):
    displayMainWindow = pyqtSignal()
    def __init__(self, parent=None):
        super(MainHistory, self).__init__(parent)
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Buttons(self) -> None:
        """

        :return:
        """
        pass

    def Ui(self) -> None:
        """

        :return:
        """
        self.show()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """

        :param a0:
        :return:
        """
        self.displayMainWindow.emit()
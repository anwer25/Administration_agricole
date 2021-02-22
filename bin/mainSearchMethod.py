from bin.searchMethod import Ui_searchMethod
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QShowEvent, QCloseEvent


class mainsearchMethod(QDialog, Ui_searchMethod):
    result = pyqtSignal()
    Disable = pyqtSignal()

    def __init__(self, parent=None):
        super(mainsearchMethod, self).__init__(parent)
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        """

        :return:
        """
        self.show()

    def Buttons(self):
        """

        :return:
        """
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.Disable.emit()
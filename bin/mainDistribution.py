from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QWidget

from bin.worker import TableWorker
from bin.sync import dataBaseSyncer
from bin.distribution import Ui_distribution


class distributionWind(QWidget, Ui_distribution):
    switcher = pyqtSignal()

    def __init__(self):
        super(distributionWind, self).__init__()
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()

    def Buttons(self):
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.switcher.emit()

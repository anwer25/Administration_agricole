from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from bin.mainWindow import Ui_mainwindow
from bin.MainFarmers import farmers
import os


class mainW(QMainWindow, Ui_mainwindow):

    def __init__(self, parent=None):

        super(mainW, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI()
        self.username = None
        self.settings = QSettings('AlphaSoft', 'Admin')
        self.show()

    def UI(self):
        """
        if not result['farmers']:
            self.farmers.isEnabled()
        if not result['ProsectionOffices']:
            self.ProsecutionOffices.isEnabled(False)
        if not result['distribution']:
            self.distribution.isEnabled(False)
        if not result['history']:
            self.histroy.isEnabled(False)
        if not result['settings']:
            pass
        if not result['DeanShip']:
            self.DeanShips.isEnabled(False)
        # self.username = result[]
        """
    def Buttons(self):
        self.farmers.clicked.connect(self.openFarmers)
        self.DeanShips.clicked.connect(self.openDeanShips)
        self.ProsecutionOffices.clicked.connect(self.openProsecutionOffices)
        self.distribution.clicked.connect(self.openDistribution)
        self.histroy.clicked.connect(self.openHistory)

    def openFarmers(self):
        farmersWindow = farmers()

    def openDeanShips(self):
        pass

    def openProsecutionOffices(self):
        pass

    def openDistribution(self):
        pass

    def openHistory(self):
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            os.remove('.\\bin\\data\\temp\\temp.dll')
        except FileNotFoundError as e:
            print(e)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    apps = mainW()
    sys.exit(app.exec_())

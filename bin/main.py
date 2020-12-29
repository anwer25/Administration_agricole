from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from bin.mainWindow import Ui_mainwindow


class mainW(Ui_mainwindow):

    def __init__(self):
        Ui_mainwindow.__init__(self)
        self.setupUi(self)
        self.show()

    def UI(self):
        pass

    def Buttons(self):
        self.farmers.clicked.connect(self.openFarmers)
        self.DeanShips.clicked.connect(self.openDeanShips)
        self.ProsecutionOffices.clicked.connect(self.openProsecutionOffices)
        self.distribution.clicked.connect(self.openDistribution)
        self.histroy.clicked.connect(self.openHistory)

    def openFarmers(self):
        pass

    def openDeanShips(self):
        pass

    def openProsecutionOffices(self):
        pass

    def openDistribution(self):
        pass

    def openHistory(self):
        pass


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    apps = mainW()
    sys.exit(app.exec_())


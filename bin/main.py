from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from bin.perwriter import readr
from bin.mainWindow import Ui_mainwindow
from bin.MainFarmers import farmers
from bin.deanshipsMainWindow import deanships
from bin.prosecutionOfficesMain import ProsecutionMain
from bin.mainDistribution import distributionWind
from bin.Mainhistory import MainHistory
from bin.mainSettings import mainSettings
import os


class mainW(QMainWindow, Ui_mainwindow):

    def __init__(self, parent=None):

        super(mainW, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.data = readr()
        self.data.start()
        self.data.result.connect(self.UI)
        self.username = None
        self.distributionWindow = None
        self.farmersWindow = None
        self.deanships = None
        self.prosecutionWindow = None
        self.historyWindow = None
        self.settingsWindow = None

        self.Buttons()
        self.show()

    def UI(self, result: dict = None):

        if not result['distribution']:
            self.distribution.setEnabled(False)
        if not result['history']:
            self.histroy.setEnabled(False)
        if not result['settings']:
            self.settings.setEnabled(False)

    def Buttons(self):
        self.farmers.clicked.connect(self.openFarmers)
        self.DeanShips.clicked.connect(self.openDeanShips)
        self.ProsecutionOffices.clicked.connect(self.openProsecutionOffices)
        self.distribution.clicked.connect(self.openDistribution)
        self.histroy.clicked.connect(self.openHistory)
        self.settings.clicked.connect(self.openSettings)

    def openFarmers(self) -> None:

        self.farmersWindow = farmers()
        self.hide()
        self.farmersWindow.display.connect(self.show)

    def openDeanShips(self):
        self.deanships = deanships()
        self.hide()
        self.deanships.displayMainWindow.connect(self.show)

    def openProsecutionOffices(self):
        self.prosecutionWindow = ProsecutionMain()
        self.hide()
        self.prosecutionWindow.display.connect(self.show)

    def openDistribution(self):
        self.distributionWindow = distributionWind()
        self.hide()
        self.distributionWindow.switcher.connect(self.show)

    def openHistory(self):
        self.historyWindow = MainHistory()
        self.hide()
        self.historyWindow.displayMainWindow.connect(self.show)

    def openSettings(self):
        self.settingsWindow = mainSettings()
        self.hide()
        self.settingsWindow.displayMainWindow.connect(self.show)

    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            os.remove('.\\bin\\data\\temp\\temp.dll')

        except FileNotFoundError as e:
            print('Error from line 66 main class mainWindow')

from bin.newFarmers import Ui_newFarmers
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from bin.sync import dataBaseSyncer


class newFMain(QWidget, Ui_newFarmers):
    refresh = pyqtSignal()

    def __init__(self):
        super(newFMain, self).__init__()
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        self.readDeanShipsData()
        self.show()

    def Buttons(self):
        self.save.clicked.connect(self.saveData)
        self.cancel.clicked.connect(self.close)

    def readDeanShipsData(self):
        self.dataBaseEngine = dataBaseSyncer(f'SELECT NAME_ FROM DEANSHIPS')
        self.dataBaseEngine.start()
        self.dataBaseEngine.Deanshipresult.connect(self.addDataToComboBox)

    def addDataToComboBox(self, data):
        self.Deanship.addItem(data[2:-4])

    def saveData(self):
        self.dataBaseEngine = dataBaseSyncer(
            f"INSERT INTO FARMERS VALUES('{self.idNumber.text()}','{self.name.text()}',"
            f"'{self.lastName.text()}', '{self.Deanship.currentText()}', "
            f"'{self.phoneNumber.text()}', '{self.headsNumber.text()}')")
        self.dataBaseEngine.start()
        self.dataBaseEngine.refresher.connect(self.refresh.emit)
        self.idNumber.clear()
        self.name.clear()
        self.lastName.clear()
        self.phoneNumber.clear()
        self.headsNumber.clear()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.refresh.emit()

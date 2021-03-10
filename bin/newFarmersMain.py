from bin.newFarmers import Ui_newFarmers
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIntValidator
from bin.sync import dataBaseSyncer
from bin.worker import dataBaseS


class newFMain(QWidget, Ui_newFarmers):
    refresh = pyqtSignal()
    enableMain = pyqtSignal()
    newFarmerWindowState = pyqtSignal(bool)

    def __init__(self):
        super(newFMain, self).__init__()
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        self.readDeanShipsData()
        self.show()
        validator = QIntValidator(00000000, 99999999, self)
        self.idNumber.setValidator(validator)
        self.headsNumber.setValidator(validator)
        self.phoneNumber.setValidator(validator)

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
        self.dataBaseEngine = dataBaseS(
            f"INSERT INTO FARMERS VALUES('{self.idNumber.text()}','{self.name.text()}',"
            f"'{self.lastName.text()}', '{self.Deanship.currentText()}', "
            f"'{self.phoneNumber.text()}', '{self.headsNumber.text()}')")
        self.dataBaseEngine.connector()
        self.refresh.emit()
        self.idNumber.clear()
        self.name.clear()
        self.lastName.clear()
        self.phoneNumber.clear()
        self.headsNumber.clear()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.enableMain.emit()
        self.newFarmerWindowState.emit(False)

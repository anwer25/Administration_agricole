from bin.change import Ui_change
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from bin.sync import dataBaseSyncer


class changeMainWindow(QWidget, Ui_change):
    refrech = pyqtSignal()

    def __init__(self, CIN: str = None):
        super(changeMainWindow, self).__init__()
        self.CIN = CIN
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
        """
        :rtype: None
        :return: None
        """
        self.show()
        self.readDeanShipsData()
        print(self.CIN)
        self.database = dataBaseSyncer(f'SELECT * FROM FARMERS WHERE ID={self.CIN}')
        self.database.start()
        self.database.result.connect(self.getData)

    def getData(self, data: list):
        self.idNumber.setText(data[0])
        self.name.setText(data[1])
        self.lastName.setText(data[2])
        self.phoneNumber.setText(data[3])
        self.Deanship.setCurrentText([data[4]])
        self.headsNumber.setText(data[5])

    def readDeanShipsData(self):
        self.dataBaseEngine = dataBaseSyncer(f'SELECT * FROM DEANSHIPS')
        self.dataBaseEngine.start()
        self.dataBaseEngine.Deanshipresult.connect(self.addDataToComboBox)

    def addDataToComboBox(self, data):
        self.Deanship.addItem(data[2:-4])

    def Buttons(self) -> None:
        """
        :rtype: None
        :return: None
        """
        self.save.clicked.connect(self.saveData)
        self.cancel.clicked.connect(self.close)

    def saveData(self) -> None:
        """
        :rtype: None
        :return: None
        """
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.refrech.emit()

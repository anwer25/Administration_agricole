from bin.change import Ui_change
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIntValidator
from bin.worker import dataBaseS
from bin.sync import dataBaseSyncer


class changeMainWindow(QWidget, Ui_change):
    refrech = pyqtSignal()
    enableMain = pyqtSignal()
    changeWindowState = pyqtSignal(bool)

    def __init__(self, CIN: str = None):
        super(changeMainWindow, self).__init__()
        self.CIN = CIN
        self.database = None
        self.dataBaseSaveEngine = None
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
        self.database = dataBaseS(f'SELECT * FROM FARMERS WHERE ID={self.CIN}')
        self.getData(self.database.connector())
        validator = QIntValidator(00000000, 99999999, self)
        self.phoneNumber.setValidator(validator)
        self.headsNumber.setValidator(validator)

    def getData(self, data: list):
        self.idNumber.setText(str(data[0][0]))
        self.name.setText(data[0][1])
        self.lastName.setText(data[0][2])
        self.phoneNumber.setText(str(data[0][3]))
        self.Deanship.setCurrentText(data[0][4])
        self.headsNumber.setText(str(data[0][5]))

    def readDeanShipsData(self):
        """
        About : read Deanship data from data base 
        :return: None
        """
        self.___dataBaseEngine = dataBaseSyncer(f'SELECT NAME_ FROM DEANSHIPS')
        self.___dataBaseEngine.start()
        self.___dataBaseEngine.Deanshipresult.connect(self.addDataToComboBox)

    def addDataToComboBox(self, data):
        """

        :param data: Deanship name from database
        :return: None
        """
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
        self.dataBaseSaveEngine = dataBaseS(f"UPDATE FARMERS SET PHONENUMBER = '{self.phoneNumber.text()}',"
                                            f"DEANSHIP= '{self.Deanship.currentText()}',"
                                            f"HEADNUMBERS= {self.headsNumber.text()} WHERE ID={self.CIN}")
        self.dataBaseSaveEngine.connector()
        self.refrech.emit()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.___dataBaseEngine.terminate()
        self.enableMain.emit()
        self.changeWindowState.emit(False)

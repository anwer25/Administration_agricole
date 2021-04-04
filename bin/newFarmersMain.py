from bin.newFarmers import Ui_newFarmers
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIntValidator, QIcon, QPixmap
from bin.sync import dataBaseSyncer
from bin.worker import dataBaseS


class newFMain(QWidget, Ui_newFarmers):
    refresh = pyqtSignal()
    enableMain = pyqtSignal()
    newFarmerWindowState = pyqtSignal(bool)

    def __init__(self):
        super(newFMain, self).__init__()
        self.message = QMessageBox()
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.message.setWindowIcon(icon)
        self.message.setWindowTitle('خطأ عند الحفظ')
        self.message.setText('يوجد صندوق فارغ')
        self.message.setIcon(QMessageBox.Warning)
        self.message.setStandardButtons(QMessageBox.Ok)
        self.OkButtonArabicName = self.message.button(QMessageBox.Ok)
        self.OkButtonArabicName.setText('موافق')
        self.message.setDefaultButton(QMessageBox.Ok)
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
        if self.idNumber.text() and self.name.text() and self.lastName.text() and self.phoneNumber.text() and \
                self.headsNumber.text() != '':
            self.dataBaseEngine = dataBaseS(
                f"INSERT INTO FARMERS VALUES('{self.idNumber.text()}','{self.name.text()}',"
                f"'{self.lastName.text()}', '{self.Deanship.currentText()}', "
                f"'{self.phoneNumber.text()}', '{self.headsNumber.text()}')")
            self.dataBaseEngine.connector()
            self.refresh.emit()
            self.close()
        else:
            self.message.exec_()

    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            self.dataBaseEngine.terminate()
        except AttributeError:
            pass
        finally:
            self.enableMain.emit()
            self.newFarmerWindowState.emit(False)

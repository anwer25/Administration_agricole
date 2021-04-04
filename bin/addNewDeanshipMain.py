from bin.addNewDeanShip import Ui_addNewDeanShip
from bin.worker import dataBaseS

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIntValidator, QIcon, QPixmap


class addNewDeanshipWindow(QWidget, Ui_addNewDeanShip):
    refresh = pyqtSignal()
    enableWindow = pyqtSignal()

    def __init__(self):
        super(addNewDeanshipWindow, self).__init__()
        self.message = QMessageBox()
        self.setupUi(self)
        self.Ui()
        self.Buttons()
        self.databaseEngine = None

    def Ui(self) -> None:
        """
        :rtype: None
        :return: None
        """
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
        validator = QIntValidator(00000000, 99999999)
        self.population.setValidator(validator)
        self.show()

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
        if self.deanshipName.text() and self.population.text() != '':
            self.databaseEngine = dataBaseS(f"INSERT INTO DEANSHIPS VALUES('{self.deanshipName.text()}',"
                                            f"{self.population.text()})")
            self.databaseEngine.connector()
            self.refresh.emit()
            self.close()
        else:
            self.message.exec_()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        :rtype: None
        :return: None
        """
        self.enableWindow.emit()

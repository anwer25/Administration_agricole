from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from bin.addNewUser import Ui_Dialog
from bin.psd import Crypt
from bin.worker import dataBaseS


class mainAddNewUser(QDialog, Ui_Dialog):
    display = pyqtSignal()
    refresher = pyqtSignal()

    def __init__(self, parent=None):
        super(mainAddNewUser, self).__init__(parent)
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()

    def Buttons(self):
        def password():
            if self.displayPassword.isChecked():
                self.password_2.setEchoMode(QLineEdit.Normal)
            else:
                self.password_2.setEchoMode(QLineEdit.Password)

        self.save.clicked.connect(self.__saveData)
        self.cancel.clicked.connect(self.close)
        self.displayPassword.clicked.connect(password)

    def __saveData(self):
        password: str = self.password_2.text()
        userName: str = self.userName_2.text()
        distribution: int = 1 if self.distribution.isChecked() else 0
        history: int = 1 if self.history.isChecked() else 0
        encrypting: Crypt = Crypt(password)
        self.___saver: dataBaseS = dataBaseS(
            f"INSERT INTO users Values('{userName}', '{history}', '{distribution}', 0,"
            f"'{encrypting.encryptUserNameAndPassword()}')")
        self.___saver.connector()
        self.___saver.refresher.connect(self.refresher.emit)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

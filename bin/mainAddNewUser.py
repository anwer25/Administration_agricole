from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap
from bin.addNewUser import Ui_Dialog
from bin.psd import Crypt
from bin.worker import dataBaseS
from qrc_source import source


class mainAddNewUser(QDialog, Ui_Dialog):
    display = pyqtSignal()
    refresher = pyqtSignal()

    def __init__(self, parent=None):
        super(mainAddNewUser, self).__init__(parent)
        self.setupUi(self)
        self.errorMessage = QMessageBox()
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.errorMessage.setWindowTitle('هناك مشكلة')
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.errorMessage.setWindowIcon(icon)
        self.errorMessage.setText('هناك حقل إدخال فارغ')
        self.errorMessage.setIcon(QMessageBox.Warning)
        self.errorMessage.setDefaultButton(QMessageBox.Ok)
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
        # TODO: check if there are another user with some name
        password: str = self.password_2.text()
        userName: str = self.userName_2.text()
        if password != '' and userName != '':
            distribution: int = 1 if self.distribution.isChecked() else 0
            history: int = 1 if self.history.isChecked() else 0
            encrypting: Crypt = Crypt(password)
            ___saver: dataBaseS = dataBaseS(
                f"INSERT INTO users Values('{userName}', '{history}', '{distribution}', 0,"
                f"'{encrypting.encryptUserNameAndPassword()}')")
            ___saver.connector()
            self.refresher.emit()
            self.close()
        else:
            self.errorMessage.exec_()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

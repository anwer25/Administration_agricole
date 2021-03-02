from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from bin.addNewUser import Ui_Dialog
from bin.psd import Crypt


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

        self.save.clicked.connect(self.saveData)
        self.cancel.clicked.connect(self.close)
        self.displayPassword.clicked.connect(password)

    def saveData(self):
        pass

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

from bin.login import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow, QMessageBox



class loginMain(QMainWindow, Ui_MainWindow):
    windowSwitcher = pyqtSignal()

    def __init__(self):
        super(loginMain, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        self.show()

    def Buttons(self):
        self.login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        username = self.username.text()
        passowrd = self.password.text()


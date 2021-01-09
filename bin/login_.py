from bin.login import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from bin.sync import dataBaseSyncer
from bin.psd import Dcrypt


class loginMain(QMainWindow, Ui_MainWindow):
    windowSwitcher = pyqtSignal(str)

    def __init__(self):
        super(loginMain, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        self.show()
        self.noUserMessage = QMessageBox()
        self.noUserMessage.setWindowTitle('مشكلة في تسجيل الدخول')
        self.noUserMessage.setText('لا يوجد مستخدم بهذا الاسم')
        self.noUserMessage.setIcon(QMessageBox.Warning)
        self.noUserMessage.setStandardButtons(QMessageBox.Ok)
        self.passwordProblem = QMessageBox()
        self.passwordProblem.setWindowTitle('مشكلة في تسجيل الدخول')
        self.passwordProblem.setText('كلمة مرور خاطئة')
        self.passwordProblem.setIcon(QMessageBox.Warning)
        self.passwordProblem.setStandardButtons(QMessageBox.Ok)
        self.password.setEchoMode(QLineEdit.Password)

    def Buttons(self):
        self.login.clicked.connect(self.checkLogin)
        self.exit.clicked.connect(self.close)

    def checkLogin(self):
        username = f'\'{self.username.text()}\''

        database = dataBaseSyncer(f"SELECT password FROM users WHERE USER_={username}")
        database.start()
        database.result.connect(self.result)

    def result(self, r):
        if len(r) == 0:
            self.noUserMessage.exec_()
        else:
            password = self.password.text()
            passwordVerify = Dcrypt(password, r)
            passwordVerify.start()
            passwordVerify.state.connect(self.windowSwitcherEngine)

    def checkPermission(self):
        pass

    def windowSwitcherEngine(self, r):
        if r:
            self.windowSwitcher.emit()
        else:
            self.passwordProblem.exec_()

from bin.reg import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from bin.psd import Crypt
from bin.sync import dataBaseSyncer


class registerWindow(QMainWindow, Ui_MainWindow):
    windowSwitcher = pyqtSignal()

    def __init__(self):
        super(registerWindow, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.passwordProblem = QMessageBox()
        self.ok = QMessageBox()
        self.Ui()
        self.Buttons()


    def Ui(self):
        self.show()
        self.passwordProblem.setWindowTitle('خطأ في كلمة المرور')
        self.passwordProblem.setText('خطأ في إعادة كلمة المرور')
        self.passwordProblem.setInformativeText('يجب أن يكون طول كلمة المرور أكبر من أربعة')
        self.passwordProblem.setIcon(QMessageBox.Warning)
        self.passwordProblem.setStandardButtons(QMessageBox.Ok)
        self.ok.setWindowTitle('التسجيل')
        self.ok.setText('اكتمل التسجيل بشكل صحيح')
        self.ok.setIcon(QMessageBox.Information)
        self.ok.setStandardButtons(QMessageBox.Ok)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_2.setEchoMode(QLineEdit.Password)

    def Buttons(self):
        self.login.clicked.connect(self.createAccount)

    def createAccount(self):
        print(f'username:{self.username.text()}, password: {self.password.text()} password2: {self.password_2.text()}')
        if self.password.text() == self.password_2.text() and len(self.password.text()) > 4:
            CryptEngine = Crypt(self.username.text(), self.password.text())
            CryptEngine.start()
            CryptEngine.passwordAndUserName.connect(self.saver)
        else:
            self.passwordProblem.exec_()
            self.password.clear()
            self.password_2.clear()

    def saver(self, username, password):
        print(username)
        print(password)
        saverEngine = dataBaseSyncer(f"INSERT INTO users values('4','{username}','{password}', 'True')")
        saverEngine.start()


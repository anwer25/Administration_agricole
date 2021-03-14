from bin.login import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from bin.worker import dataBaseS
from bin.psd import Dcrypt
from bin.perwriter import writer
import shutil
import os.path
from qrc_source import source


class loginMain(QMainWindow, Ui_MainWindow):
    """

    """
    windowSwitcher = pyqtSignal()

    def __init__(self):
        super(loginMain, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Buttons()
        self.Problem = QMessageBox()
        self.Ui()

    def Ui(self) -> None:
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.Problem.setWindowIcon(icon)
        self.Problem.setWindowTitle('مشكلة في تسجيل الدخول')
        self.Problem.setIcon(QMessageBox.Warning)
        self.Problem.setStandardButtons(QMessageBox.Ok)
        self.password.setEchoMode(QLineEdit.Password)
        self.show()

    def Buttons(self) -> None:
        self.login.clicked.connect(self.checkLogin)
        self.exit.clicked.connect(self.close)

    def checkLogin(self) -> None:
        # noinspection PyGlobalUndefined
        global username
        username = f'\'{self.username.text()}\''

        database = dataBaseS(f"SELECT password FROM users WHERE USER_={username}")
        self.result(database.connector())

    def result(self, r: list) -> None:

        if len(r) == 0:
            self.Problem.setText('لا يوجد مستخدم بهذا الاسم')
            self.Problem.exec_()
        else:
            password = self.password.text()
            passwordVerify = Dcrypt(password, r)

            self.windowSwitcherEngine(passwordVerify.passwordShaker())

    def windowSwitcherEngine(self, r) -> None:
        def ignore(path, content_list):
            return [
                content
                for content in content_list
                if os.path.isdir(os.path.join(path, content))
            ]
        if r:
            shutil.copytree('template', f'{os.path.expanduser("~")}\\template', ignore=ignore, dirs_exist_ok=True)
            jsonWriter = writer(username)
            self.windowSwitcher.emit()
        else:
            self.Problem.setText('كلمة مرور خاطئة')
            self.Problem.exec_()

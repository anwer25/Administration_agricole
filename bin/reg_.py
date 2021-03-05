from bin.reg import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from bin.psd import Crypt
from bin.worker import dataBaseS
from bin.perwriter import writer
from qrc_source import source


class registerWindow(QMainWindow, Ui_MainWindow):
    windowSwitcher = pyqtSignal()                               # SEND SIGNAL TO CONTROLLER CLASS
    """
        registerWindow is subclass to bin.reg.Ui_MainWindow 
        displayed on first programme launch if no user on database 
        imported models and class
        
    """
    def __init__(self):
        super(registerWindow, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.message = QMessageBox()
        self.Ui()
        self.Buttons()

    def Ui(self) -> None:
        self.show()
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.message.setWindowIcon(icon)
        self.message.setStandardButtons(QMessageBox.Ok)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_2.setEchoMode(QLineEdit.Password)

    def Buttons(self) -> None:
        self.login.clicked.connect(self.createAccount)
        self.exit.clicked.connect(self.close)

    def createAccount(self) -> None:
        if self.password.text() == self.password_2.text() and len(self.password.text()) > 4:        # check if len
            # passowrd is greater than 4 and password one and tow is the some
            CryptEngine = Crypt(self.password.text())                   # password encrypting
            self.saver(CryptEngine.encryptUserNameAndPassword())        # pass password to save method
        else:
            self.message.setWindowTitle('خطأ في كلمة المرور')
            self.message.setText('خطأ في إعادة كلمة المرور')
            self.message.setInformativeText('يجب أن يكون طول كلمة المرور أكبر من أربعة')
            self.message.setIcon(QMessageBox.Warning)
            self.message.exec_()                                # display message if there are
            self.password.clear()                                       # problem on password
            self.password_2.clear()

    def saver(self, password) -> None:
        saverEngine = dataBaseS(f"INSERT INTO users values('{self.username.text()}',1, 1"
                                f", 1, '{password}')")              # save password on data base using databaseS class
        saverEngine.connector()
        jsonWriter = writer(f"'{self.username.text()}'")            # write user privilege on json file to use it later
        self.message.setWindowTitle('التسجيل')
        self.message.setText('اكتمل التسجيل بشكل صحيح')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_()
        self.windowSwitcher.emit()                                  # send signal to display main Window

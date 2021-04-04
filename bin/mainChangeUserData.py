from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent, QPixmap, QIcon
from bin.changeUserData import Ui_Dialog
from bin.psd import Crypt
from bin.worker import dataBaseS
from qrc_source import source


class mainChangeUserData(QDialog, Ui_Dialog):
    display = pyqtSignal()
    refresher = pyqtSignal()

    def __init__(self, user, parent=None):
        super(mainChangeUserData, self).__init__(parent)
        self.settings = 0
        self.setupUi(self)
        self.user = user
        self.errorMessage = QMessageBox()
        self.message = QMessageBox()
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.userName_2.setText(self.user[0])
        if self.user[1] == 'نعم':
            self.distribution.setChecked(True)
            self.history.setChecked(True)
            self.distribution.setEnabled(False)
            self.history.setEnabled(False)
            self.settings = 1
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.message.setWindowTitle('إشعار تم تحديث بيانات')
        self.message.setWindowIcon(icon)
        self.message.setText('تم تحديث البيانات بنجاح')
        self.message.setDefaultButton(QMessageBox.Ok)
        self.message.setIcon(QMessageBox.Information)
        ##############################################
        self.errorMessage.setWindowTitle('هناك مشكلة')
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

        self.pushButton.clicked.connect(self.__saveData)
        self.pushButton_2.clicked.connect(self.close)
        self.displayPassword.clicked.connect(password)

    def __saveData(self):
        # TODO: check if there are another user with some name
        password: str = self.password_2.text()
        userName: str = self.userName_2.text()
        if password and userName != '':
            distribution: int = 1 if self.distribution.isChecked() else 0
            history: int = 1 if self.history.isChecked() else 0
            encrypting: Crypt = Crypt(password)
            query = f"UPDATE users SET USER_= '{userName}' ,history= '{history}', distribution= '{distribution}'," \
                    f"settings='{self.settings}', password= '{encrypting.encryptUserNameAndPassword()}' " \
                    f"WHERE USER_='{self.user[0]}'"
            ___saver: dataBaseS = dataBaseS(query)
            ___saver.connector()
            self.message.exec_()
            self.refresher.emit()
            self.close()
        else:
            self.errorMessage.exec_()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.display.emit()

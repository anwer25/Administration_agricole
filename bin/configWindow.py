from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon, QPixmap
import mysql.connector
from bin.conf import Ui_config
from bin.mysqlError import mysqlError
from qrc_source import source


class mainConfig(QMainWindow, Ui_config):

    def __init__(self, parent=None):
        super(mainConfig, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.message = QMessageBox()
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.message.setWindowTitle('تم حفظ الإعدادات بنجاح')
        icon = QIcon()
        icon.addPixmap(
        QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
        QIcon.Normal, QIcon.Off)
        self.message.setWindowIcon(icon)
        self.message.setIcon(QMessageBox.Information)
        self.message.setStandardButtons(QMessageBox.Ok)
        self.message.setText('تم حفظ الإعدادات بنجاح.الرجاء إغلاق البرنامج وتشغيله مرة أخرى')
        self.show()

    def Buttons(self):
        self.cancel.clicked.connect(self.close)
        self.save.clicked.connect(self.saveData)

    def saveData(self):
        try:
            config = {
                'user': self.dbUserName.text(),
                'password': self.dbPassword.text(),
                'host': self.dbHost.text(),
                'raise_on_warnings': True
            }
            connection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            ___mysqlError = mysqlError(err)
            self.message.setWindowTitle('هناك خطأ')
            self.message.setText(___mysqlError.__str__())
            self.message.setIcon(QMessageBox.Warning)
            self.message.exec_()
        else:
            if connection.is_connected():
                self.settings.setValue('DATABASE_USER_NAME', self.dbUserName.text())
                self.settings.setValue('DATABASE_PASSWORD', self.dbPassword.text())
                self.settings.setValue('DATABASE_HOST', self.dbHost.text())
                self.settings.setValue('DATABASE_NAME', self.dataBaseName.text())
                self.settings.sync()
                self.message.exec_()
                self.close()
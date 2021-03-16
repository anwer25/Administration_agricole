from PyQt5.QtCore import QThread, pyqtSignal, QSettings, QObject
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
import mysql.connector
from bin.mysqlError import mysqlError

import logging

logging.basicConfig(filename='debug.log', filemode='w', level=logging.DEBUG, format="%(message)s")


class dataBaseS(QObject):
    """

    """

    def __init__(self, com: str, parent=None):
        super(dataBaseS, self).__init__(parent)
        self.com = com
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.connection = None
        self.cursor = None
        self.messages = QMessageBox()
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.messages.setWindowIcon(icon)

    def connector(self) -> list:
        """
        :rtype: list
        :return:dataBase Query result
        """
        config = {
            'user': self.settings.value('DATABASE_USER_NAME', '', str),
            'password': self.settings.value('DATABASE_PASSWORD', '', str),
            'host': self.settings.value('DATABASE_HOST', '', str),
            'database': self.settings.value('DATABASE_NAME', '', str),
            'raise_on_warnings': True
        }
        try:
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.com)
            if 'INSERT' in self.com or 'UPDATE' in self.com or 'DELETE' in self.com:
                self.connection.commit()
            else:
                return self.cursor.fetchall()
        except mysql.connector.Error as err:
            error = mysqlError(err)
            self.messages.setWindowTitle('هناك خطأ')
            self.messages.setIcon(QMessageBox.Warning)
            self.messages.setText(error.__str__())
            self.messages.exec_()
        finally:
            try:
                self.connection.close()
            except:
                pass

class TableWorker(QThread):
    data_ = pyqtSignal(int, int, str)
    data__ = pyqtSignal(int)

    def __init__(self, command: str):
        super(TableWorker, self).__init__()
        self.command = command
        self.data = None

    def run(self) -> None:
        self.dataresult()

    def dataresult(self):
        self.data = dataBaseS(self.command)
        data_ = self.data.connector()
        self.data.connection.close()
        try:
            for rowNumber, rowData in enumerate(data_):
                self.data__.emit(rowNumber)
                for colNumber, data in enumerate(rowData):
                    self.data_.emit(rowNumber, colNumber, str(data))
        except TypeError as e:
            logging.debug(f'worker error line 69 :{e}')
        finally:
            self.quit()

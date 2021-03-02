from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QSettings, QObject
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import mysql.connector
from bin.mysqlError import mysqlError


class dataBaseS(QObject):
    data = pyqtSignal(list)
    refresher = pyqtSignal()

    def __init__(self, com: str, parent=None):
        super(dataBaseS, self).__init__(parent)
        self.com = com
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.connection = None
        self.cursor = None

    def connector(self) -> list:
        """
        :rtype: list
        :return:dataBase Query result
        """
        config = {
            'user': self.settings.value('DATABASE_USER_NAME', 'root', str),
            # password must changed to ''
            'password': self.settings.value('DATABASE_PASSWORD', 'admin', str),
            'host': self.settings.value('DATABASE_HOST', 'localhost', str),
            'database': self.settings.value('DATABASE_NAME', 'administration-agricole', str),
            'raise_on_warnings': True
        }
        try:
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.com)
            if 'INSERT' in self.com or 'UPDATE' in self.com or 'DELETE' in self.com:
                self.connection.commit()
                self.connection.close()
            else:
                return self.cursor.fetchall()
        except mysql.connector.Error as err:
            # TODO: FIX NO ERROR RETURNED FROM MYSQLERROR CLASS
            print(err)
            error = mysqlError(err)
            error.errorType.connect(lambda i: print(f'{i} from worker line 32'))


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
            print(f'worker error line 60 :{e}')
        finally:
            self.quit()

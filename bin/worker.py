from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QSettings
import mysql.connector


class dataBaseS:
    data = pyqtSignal(list)

    def __init__(self, com: str):
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
            'host': self.settings.value('DATABASE HOST', 'localhost', str),
            'database': self.settings.value('DATABASE_NAME', 'administration-agricole', str),
            'raise_on_warnings': True
        }
        try:
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.com)
            if 'INSERT' in self.com:
                self.connection.commit()
            else:
                return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f'Error from line 23 sync file class dataBaseSyncer: {err}')


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
        print(data_)
        self.data.connection.close()
        try:
            for rowNumber, rowData in enumerate(data_):
                self.data__.emit(rowNumber)
                for colNumber, data in enumerate(rowData):
                    self.data_.emit(rowNumber, colNumber, str(data))
        except TypeError as e:
            print(f'worker error line 53 :{e}')
        finally:
            self.quit()

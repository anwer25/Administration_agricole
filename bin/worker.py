from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from pyodbc import Error
import pyodbc


class dataBaseS:
    data = pyqtSignal(list)

    def __init__(self, com: str):
        self.com = com


    def connecter(self) -> list:
        """
        :rtype: list
        :return:dataBase Query result
        """
        ___DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
        ___MDB = '.\\bin\\data\\alphaData.accdb'
        ___PWD = 'An23011997'
        try:
            self.conn = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(___DRV, ___MDB, ___PWD))
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.com)
            return self.cursor.fetchall()
        except Error as e:
            print(f'Error from line 23 sync file class dataBaseSyncer: {e}')


class TableWorker(QThread):
    data_ = pyqtSignal(list)
    datastr = pyqtSignal(str)
    col = pyqtSignal(int)
    row = pyqtSignal(int)

    def __init__(self):
        super(TableWorker, self).__init__()

    def run(self) -> None:
        self.dataresult()

    def dataresult(self):
        self.data = dataBaseS('SELECT * FROM FARMERS')
        data_ = self.data.connecter()
        self.data.conn.close()
        for rowNumber, rowData in enumerate(data_):
            # self.rowNumberS.emit(rowNumber)
            temp = []
            for colNumber, data in enumerate(rowData):
                temp.append(rowNumber)
                temp.append(colNumber)
                temp.append(str(data))
                self.row.emit(rowNumber)
                self.col.emit(colNumber)
                self.datastr.emit(str(data))
                self.data_.emit(temp)
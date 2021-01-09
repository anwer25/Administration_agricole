from pyodbc import Error
import pyodbc
from PyQt5.QtCore import QThread, pyqtSignal


class dataBaseSyncer(QThread):
    result = pyqtSignal(list)

    def __init__(self, com: str):
        super(dataBaseSyncer, self).__init__()
        self.com = com

    def run(self) -> None:
        self._connecter()

    def _connecter(self) -> None:
        """
        :rtype: None
        :return:dataBase Query result 
        """
        ___DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
        ___MDB = '.\\bin\\data\\alphaData.accdb'
        ___PWD = 'An23011997'
        try:
            conn = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(___DRV, ___MDB, ___PWD))
            cursor = conn.cursor()
            cursor.execute(self.com)
            if "INSERT" in self.com:
                conn.commit()
            else:
                self.result.emit(cursor.fetchall())

        except Error as e:
            print(f'Error from line 23 sync file class dataBaseSyncer: {e}')

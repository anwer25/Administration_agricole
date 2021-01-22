from pyodbc import Error
import pyodbc
from PyQt5.QtCore import QThread, pyqtSignal


class dataBaseSyncer(QThread):
    result = pyqtSignal(list)
    Deanshipresult = pyqtSignal(str)

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
            self.conn = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(___DRV, ___MDB, ___PWD))
            cursor = self.conn.cursor()
            if 'INSERT' in self.com or 'UPDATE' in self.com or 'DELETE' in self.com:
                cursor.execute(self.com)
                self.conn.commit()
            else:
                if "DEANSHIPS" in self.com:
                    for Deanship in cursor.execute(self.com):

                        self.Deanshipresult.emit(str(Deanship))
                else:
                    cursor.execute(self.com)
                    self.result.emit(cursor.fetchall())
            self.conn.close()

        except Error as e:
            print(f'Error from line 23 sync file class dataBaseSyncer: {e}')

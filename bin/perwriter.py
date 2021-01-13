from pyodbc import Error
import pyodbc
import json
from PyQt5.QtCore import QThread, pyqtSignal


class writer(QThread):
    def __init__(self, name):
        super(writer, self).__init__()
        self.name = name
        self.database = None

    def run(self) -> None:
        self.writeDataToJson()

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
            self.cursor = conn.cursor()

        except Error as e:
            print(f'Error from line 29 sync file class dataBaseSyncer: perwriter file {e}')

    def writeDataToJson(self):
        self._connecter()
        self.cursor.execute(f"SELECT * FROM users WHERE USER_={self.name}")
        data = self.cursor.fetchall()
        temp = {
            'user': data[0][0],
            'ProsectionOffices': data[0][2],
            'farmers': data[0][3],
            'newFarmers': data[0][4],
            'history': data[0][5],
            'distribution': data[0][6],
            'ProsectutionOffices': data[0][7],
            'changeProsectutionOffices': data[0][8],
            'change': data[0][9],
            'settings': data[0][10],
            'DeanShip': data[0][11],
            'addNewDeanShip': data[0][12]
        }
        with open('.\\bin\\data\\temp\\temp.dll', 'w') as jsonFile:
            json.dump(temp, jsonFile, indent=4)

class readr(QThread):
    result = pyqtSignal(dict)

    def __init__(self):
        super(readr, self).__init__()

    def run(self) -> None:
        self.reader()

    def reader(self):
        with open('.\\bin\\data\\temp\\temp.dll', 'r') as jsonFile:
            data = json.load(jsonFile)
            _ = data.copy()
            self.result.emit(_)

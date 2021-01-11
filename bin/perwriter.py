from sync import dataBaseSyncer
import json
from PyQt5.QtCore import QThread, pyqtSignal


class writer(QThread):
    def __init__(self, name):
        super(writer, self).__init__()
        self.name = name

    def run(self) -> None:
        self.readData()

    def readData(self):
        database = dataBaseSyncer(f"SELECT * FROM users WHERE USER_='{self.name}'")
        database.start()
        database.result.connect(self.writeDataToJson)

    def writeDataToJson(self, data):

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

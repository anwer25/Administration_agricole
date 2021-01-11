from sync import dataBaseSyncer
import json
from PyQt5.QtCore import QThread

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
            'ProsectionOffices': data[0][2],
            'newFarmers': data[0][3],
            'history': data[0][4],
            'distribution': data[0][5],
            'changeProsectutionOffices': data[0][6],
            'change': data[0][7],
            'settings': data[0][8],
            'addNewDeanShip': data[0][9]
        }
        with open('.\\bin\\data\\temp\\temp.dll', 'w') as jsonFile:
            json.dump(temp, jsonFile)


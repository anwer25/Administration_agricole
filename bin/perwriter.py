from typing import Dict, Any, Union
import mysql.connector
import json
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QSettings, QObject
import os


class writer(QObject):
    def __init__(self, name):
        super(writer, self).__init__()
        self.data = None
        self.name = name
        self.database = None
        self.connection = None
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.writeDataToJson()

    def _connecter(self) -> None:
        """
        :rtype: None
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

        except mysql.connector.Error as err:
            print(f'Error from line 29 sync file class dataBaseSyncer: perwriter file {err}')

    def writeDataToJson(self):
        self._connecter()
        self.cursor.execute(f"SELECT * FROM users WHERE USER_={self.name}")
        self.data = self.cursor.fetchall()
        try:
            temp: Dict[Union[str, Any], Any] = {
                'user': self.data[0][0],
                'ProsectionOffices': self.data[0][2],
                'farmers': self.data[0][3],
                'newFarmers': self.data[0][4],
                'history': self.data[0][5],
                'distribution': self.data[0][6],
                'ProsectutionOffices': self.data[0][7],
                'changeProsectutionOffices': self.data[0][8],
                'change': self.data[0][9],
                'settings': self.data[0][10],
                'DeanShip': self.data[0][11],
                'addNewDeanShip': self.data[0][12]
            }
        except IndexError as e:
            self._connecter()
            self.cursor.execute(f"SELECT * FROM users WHERE USER_={self.name}")
            self.data = self.cursor.fetchall()
            temp = {
                'user': self.data[0][0],
                'history': self.data[0][1],
                'distribution': self.data[0][2],
                'settings': self.data[0][3],
            }
        try:
            with open('.\\bin\\data\\temp\\temp.dll', 'w') as jsonFile:
                json.dump(temp, jsonFile, indent=4)
        except FileNotFoundError as e:
            if os.path.exists('.\\bin\\data\\temp'):
                print(e)
            else:
                os.mkdir('.\\bin\\data\\temp')
                with open('.\\bin\\data\\temp\\temp.dll', 'w') as jsonFile:
                    json.dump(temp, jsonFile, indent=4)
        finally:
            self.connection.close()


class readr(QThread):
    result = pyqtSignal(dict)

    def __init__(self):
        super(readr, self).__init__()

    def run(self) -> None:
        self.reader()

    def reader(self):
        try:
            with open('.\\bin\\data\\temp\\temp.dll', 'r') as jsonFile:
                data = json.load(jsonFile)
                _ = data.copy()
                self.result.emit(_)
        except FileNotFoundError as e:
            print(f'Error line 64 from perwriter class read {e}')

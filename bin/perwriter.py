from typing import Dict, Any, Union
from bin.worker import dataBaseS
import json
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QSettings, QObject
import os


class writer(QObject):
    """
    writer class to read user  privileges and write them to json file to use it later by main Window
    """
    def __init__(self, name):
        super(writer, self).__init__()
        self.name = name
        self.writeDataToJson()

    def writeDataToJson(self) -> None:
        """

        :return:
        """
        database = dataBaseS(f"SELECT * FROM users WHERE USER_={self.name}")
        data = database.connector()
        temp: Dict[Union[str, Any], Any] = {
            'user': data[0][0],
            'history': data[0][1],
            'distribution': data[0][2],
            'settings': data[0][3],
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
            pass


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

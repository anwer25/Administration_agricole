from sync import dataBaseSyncer
from PyQt5.QtCore import QThread, pyqtSignal, QSettings


class writer(QThread):
    def __init__(self, data):
        super(writer, self).__init__()
        self.settings = QSettings('AlphaSoft', 'admin')
        self.data = data
        self.start()

    def run(self) -> None:
        self.writeData()

    def writeData(self):
        self.settings.setValue('username', self.data[0][0])
        self.settings.setValue('ProsectionOffices', self.data[0][2])
        self.settings.setValue('farmers', self.data[0][3])
        self.settings.setValue('newFarmers', self.data[0][4])
        self.settings.setValue('history', self.data[0][5])
        self.settings.setValue('distribution', self.data[0][6])
        self.settings.setValue('ProsectutionOffices', self.data[0][7])
        self.settings.setValue('changeProsectutionOffices', self.data[0][8])
        self.settings.setValue('change', self.data[0][9])
        self.settings.setValue('settings', self.data[0][10])
        self.settings.setValue('DeanShip', self.data[0][11])
        self.settings.setValue('addNewDeanShip', self.data[0][12])

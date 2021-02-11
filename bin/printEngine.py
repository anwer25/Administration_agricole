from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QTableWidget
from bin.sync import dataBaseSyncer
from datetime import datetime


class printingData(QThread):
    """
        get tableWidget from mainDistribution file of type QTableWidget
        using QThread class to make this class run on thread
        reading data from QTableWidget using for lop by col and rows
        after that add gathering data to database and printing it
    """
    message = pyqtSignal()
    resetTable = pyqtSignal()
    def __init__(self, tableWidget: QTableWidget):
        super(printingData, self).__init__()
        self.tableWidget = tableWidget
        self.dataBaseEngine = None
        self.___CIN = None
        self.___NAME = None
        self.___LASTNAME = None
        self.___DEANSHIP = None
        self.___ProsectutionOffices = None
        self.___NUMBEROFBAGS = None

    def run(self) -> None:
        """

        :return:
        """
        self.readingData()

    def readingData(self) -> None:

        rowCount = self.tableWidget.rowCount()
        for row in range(rowCount):
            self.___CIN = self.tableWidget.item(row, 0).text()
            self.___NAME = self.tableWidget.item(row, 1).text()
            self.___LASTNAME = self.tableWidget.item(row, 2).text()
            self.___DEANSHIP = self.tableWidget.item(row, 3).text()
            self.___ProsectutionOffices = self.tableWidget.item(row, 4).text()
            self.___NUMBEROFBAGS = self.tableWidget.item(row, 5).text()
            self.dataBaseEngine = dataBaseSyncer(f'SELECT DATE_ FROM history where CIN={self.___CIN}')
            self.dataBaseEngine.start()
            self.dataBaseEngine.result.connect(self.dateS)
            print(self.___CIN)

    def dateS(self, datestr: list) -> None:
        todayDate = datetime.today()
        dateStr = todayDate.strftime("%d-%m-%Y")
        print(len(datestr), datestr)
        if len(datestr):
            print(datestr)
            dif = datetime.strptime(dateStr, "%d-%m-%Y")-datetime.strptime(str(datestr[0])[2:-3], "%d-%m-%Y")
            if dif.days >= 30:
                print('pk', self.___CIN)
                self.dataBaseEngine = dataBaseSyncer(
                    f"INSERT INTO history values('{self.___CIN}','{self.___NAME}','{self.___LASTNAME}',"
                    f"'{self.___DEANSHIP}','{self.___ProsectutionOffices}','{self.___NUMBEROFBAGS}',"
                    f"'{dateStr}', null )")
                self.dataBaseEngine.start()
            else:
                print('sss')

        else:
            print("qq", self.___CIN)
            self.dataBaseEngine = dataBaseSyncer(
                f"INSERT INTO history values ('{self.___CIN}','{self.___NAME}','{self.___LASTNAME}',"
                f"'{self.___DEANSHIP}','{self.___ProsectutionOffices}','{self.___NUMBEROFBAGS}',"
                f"'{dateStr}', null)")
            self.dataBaseEngine.start()
        # self.resetTable.emit()


from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QTableWidget
from bin.worker import dataBaseS
from datetime import datetime


class printingData(QThread):
    """
        get tableWidget from mainDistribution file of type QTableWidget
        using QThread class to make this class run on thread
        reading data from QTableWidget using for lop by col and rows
        after that add gathering data to database and printing it
    """
    message = pyqtSignal(list)
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
        self.messageList = []

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
            self.dataBaseEngine = dataBaseS(f'SELECT DATE_ FROM history where CIN={self.___CIN}')
            data = self.dataBaseEngine.connector()
            self.dataBaseEngine.connection.close()
            self.dateS(data)

    def dateS(self, datestr: list) -> None:
        todayDate = datetime.today()  # get today time
        dateStr = todayDate.strftime("%d-%m-%Y")  # convert todayDate to str
        if len(datestr):  # check if datestr is not empty
            dif = datetime.strptime(dateStr, "%d-%m-%Y") - datetime.strptime(str(datestr[-1])[2:-3], "%d-%m-%Y")  # calculate deffrince bettwine time on data base and current time
            if dif.days >= 30:  # check if dif is not less than 30Days

                self.dataBaseEngine = dataBaseS(
                f"INSERT INTO history values ('{self.___CIN}','{self.___NAME}','{self.___LASTNAME}',"
                f"'{self.___DEANSHIP}','{self.___ProsectutionOffices}','{self.___NUMBEROFBAGS}',"
                f"'{dateStr}', null)")
                data = self.dataBaseEngine.connector()
                self.dataBaseEngine.connection.close()
            else:
                self.messageList.append(self.___CIN)

        else:

            self.dataBaseEngine = dataBaseS(
                f"INSERT INTO history values ('{self.___CIN}','{self.___NAME}','{self.___LASTNAME}',"
                f"'{self.___DEANSHIP}','{self.___ProsectutionOffices}','{self.___NUMBEROFBAGS}',"
                f"'{dateStr}', null)")
            data = self.dataBaseEngine.connector()
            self.dataBaseEngine.connection.close()
        self.message.emit(self.messageList)

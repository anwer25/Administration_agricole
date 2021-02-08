from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QTableWidget
from bin.sync import dataBaseSyncer


class printingData(QThread):
    """
        get tableWidget from mainDistribution file of type QTableWidget
        using QThread class to make this class run on thread
        reading data from QTableWidget using for lop by col and rows
        after that add gathering data to database and printing it
    """

    def __init__(self, tableWidget: QTableWidget):
        super(printingData, self).__init__()
        self.tableWidget = tableWidget
        self.dataBaseEngine = None

    def run(self) -> None:
        """

        :return:
        """
        self.readingData()

    def readingData(self) -> None:

        rowCount = self.tableWidget.rowCount()
        colCount = self.tableWidget.columnCount()

        for row in range(rowCount):
            print(self.tableWidget.item(row, 0).text())
            ___CIN = self.tableWidget.item(row, 0).text()
            ___NAME = self.tableWidget.item(row, 1).text()
            ___LASTNAME = self.tableWidget.item(row, 2).text()
            ___DEANSHIP = self.tableWidget.item(row, 3).text()
            ___ProsectutionOffices = self.tableWidget.item(row, 4).text()
            ___NUMBEROFBAGS = self.tableWidget.item(row, 5).text()
            print(___CIN, ___NAME, ___LASTNAME, ___DEANSHIP, ___ProsectutionOffices, ___NUMBEROFBAGS)

            self.dataBaseEngine = dataBaseSyncer(f"INSERT INTO histroy values(CIN='{___CIN}',"
                                                 f"NAME_='{___NAME}',"
                                                 f"LASTNAME='{___LASTNAME}',"
                                                 f"DEANSHIP='{___DEANSHIP}',"
                                                 f"ProsectutionOffices='{___ProsectutionOffices}',"
                                                 f"NUMBEROFBAGS='{___NUMBEROFBAGS}')")
            self.dataBaseEngine.start()



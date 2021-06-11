from PyQt5.QtCore import QThread, pyqtSignal, QSettings, QObject
from PyQt5.QtWidgets import QTableWidget
from bin.worker import dataBaseS
from datetime import datetime
from docxtpl import DocxTemplate
from docx.opc import exceptions
import uuid
from win32com import client
import time
import pythoncom
import os
import logging

logging.basicConfig(filename='debug.log', filemode='w', level=logging.DEBUG, format="%(message)s")


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
        self.printList = []
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
            self.___data = self.dataBaseEngine.connector()
            UUID = self.dateS(self.___data)
            logging.debug(UUID)
            if UUID != '0':
                self.printList.append(UUID)
            else:
                pass
        template = templateEngine(self.printList)

    @staticmethod
    def com(cin: str, name: str, lastName: str, deanship: str, ProsectutionOffices: str,
            NUMBEROFBAGS: str, date: str, printID: str):
        dataBaseEngine = dataBaseS(
            f"INSERT INTO history values ('{cin}','{name}','{lastName}',"
            f"'{deanship}','{ProsectutionOffices}','{NUMBEROFBAGS}',"
            f"'{date}', null, '{printID}')")
        dataBaseEngine.connector()

    def dateS(self, datestr: list) -> str:

        todayDate = datetime.today()  # get today time
        dateStr = todayDate.strftime("%d-%m-%Y")  # convert todayDate to str
        printID = uuid.uuid4()

        if datestr:  # check if datestr is not empty
            dif = datetime.strptime(dateStr, "%d-%m-%Y") - datetime.strptime(str(datestr[-1])[2:-3],
                                                                             "%d-%m-%Y")  # calculate deffrince bettwine time on data base and current time
            if dif.days >= 30:  # check if dif is not less than 30Days

                self.com(self.___CIN, self.___NAME, self.___LASTNAME, self.___DEANSHIP,
                         self.___ProsectutionOffices, self.___NUMBEROFBAGS, dateStr, str(printID))
                return str(printID)
            self.messageList.append(self.___CIN)
            return str(0)
        self.com(self.___CIN, self.___NAME, self.___LASTNAME, self.___DEANSHIP,
                 self.___ProsectutionOffices, self.___NUMBEROFBAGS, dateStr, str(printID))
        return str(printID)
        # self.message.emit(self.messageList)
        # self.quit()


class templateEngine(QObject):
    TemplateNotFound = pyqtSignal()

    def __init__(self, printID: list):
        super(templateEngine, self).__init__()
        self.printID = printID
        self.dataBaseEngine = None
        self.___settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.templateWriter()

    @staticmethod
    def printingfile(file: str):
        """

        :param file:
        :return:
        """
        pythoncom.CoInitialize()
        word = client.Dispatch("Word.Application")
        pythoncom.CoInitialize()
        word.Documents.Open(file)
        word.ActiveDocument.PrintOut()
        time.sleep(2)
        word.ActiveDocument.Close()
        word.Quit()

    def templateWriter(self) -> None:
        """

        :return:
        """
        con = []
        i = 1
        ___COUNT = int(len(self.printID))
        for UUID in self.printID:
            self.dataBaseEngine = dataBaseS(f"SELECT * FROM history where PRINTID='{UUID}'")
            data = self.dataBaseEngine.connector()
            self.dataBaseEngine.connection.close()
            con.append([
                data[0][7],
                data[0][6],
                f'{data[0][1]} {data[0][2]}',
                data[0][0],
                data[0][5],
                data[0][4],
            ])

            def ___save(n: int = 6):
                context = {
                    'd': con
                }

                docx = f'{os.getcwd()}\\template\\template6.docx' if n == 6\
                    else f'{os.getcwd()}\\template\\template5.docx' if n == 5 \
                    else f'{os.getcwd()}\\template\\template4.docx' if n == 4\
                    else f'{os.getcwd()}\\template\\template3.docx' if n == 3 \
                    else f'{os.getcwd()}\\template\\template2.docx' if n == 2\
                    else f'{os.getcwd()}\\template\\template1.docx'
                try:
                    doc = DocxTemplate(docx)
                    logging.debug(docx)
                except exceptions.PackageNotFoundError as e:
                    logging.debug(f' line 154 from printEngine{e}')
                    self.TemplateNotFound.emit()
                else:
                    doc.render(context)
                    file = f'{os.getcwd()}\\temp\\{data[0][8]}.docx'
                    doc.save(file)
                    con.clear()
                    logging.debug(file)
                    return file

            if ___COUNT >= 6:
                if i == 6:
                    ___COUNT -= i
                    i = 0
                    self.printingfile(___save())
            elif i == ___COUNT:
                self.printingfile(___save(i))
            i += 1


class printFarmersAndHistoryData(QThread):

    def __init__(self, com: str, parent=None, f=0):
        super(printFarmersAndHistoryData, self).__init__(parent)
        self.fileParent = f
        self.com = com
        self.data = dataBaseS(com)
        self.start()

    def run(self) -> None:
        data = self.data.connector()
        self.printingfile(self.wordWriter(data))

    @staticmethod
    def printingfile(file: str):
        """

        :param file:
        :return:
        """
        pythoncom.CoInitialize()
        word = client.Dispatch("Word.Application")
        pythoncom.CoInitialize()
        word.Documents.Open(file)
        word.ActiveDocument.PrintOut()
        time.sleep(2)
        word.ActiveDocument.Close()
        word.Quit()
        os.remove(file)

    def wordWriter(self, data) -> str:
        todayDate = datetime.today()  # get today time
        dateStr = todayDate.strftime("%d-%m-%Y")  # convert todayDate to str
        context = {
            'l': data,
            'date': dateStr,
        }
        docx = f'{os.getcwd()}\\template\\data.docx' if self.fileParent == 0 else \
            f'{os.getcwd()}\\template\\arch.docx'
        doc = DocxTemplate(docx)

        doc.render(context)
        ___name = f'{os.getcwd()}\\temp\\data.docx'
        doc.save(___name)
        return ___name

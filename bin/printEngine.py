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
            data = self.dataBaseEngine.connector()
            self.dataBaseEngine.connection.close()
            UUID = self.dateS(data)
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
        data = dataBaseEngine.connector()
        dataBaseEngine.connection.close()

    def dateS(self, datestr: list) -> str:

        todayDate = datetime.today()  # get today time
        dateStr = todayDate.strftime("%d-%m-%Y")  # convert todayDate to str
        printID = uuid.uuid4()

        if len(datestr):  # check if datestr is not empty
            dif = datetime.strptime(dateStr, "%d-%m-%Y") - datetime.strptime(str(datestr[-1])[2:-3],
                                                                             "%d-%m-%Y")  # calculate deffrince bettwine time on data base and current time
            if dif.days >= 30:  # check if dif is not less than 30Days

                self.com(self.___CIN, self.___NAME, self.___LASTNAME, self.___DEANSHIP,
                         self.___ProsectutionOffices, self.___NUMBEROFBAGS, dateStr, str(printID))
                return str(printID)
            else:
                self.messageList.append(self.___CIN)
                return str(0)

        else:
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
        os.remove(file)

    def templateWriter(self) -> None:
        """

        :return:
        """
        docx = self.___settings.value('DOC_TEMPLATE', 'template\\template.docx', type=str)
        try:
            doc = DocxTemplate(docx)
        except exceptions.PackageNotFoundError as e:
            print(f' line 30 from printEngine{e}')
            self.TemplateNotFound.emit()
        else:
            con = list()
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

                def ___save():
                    context = {
                        'd': con
                    }
                    doc = DocxTemplate(docx)
                    doc.render(context)
                    file = f'{os.getcwd()}\\bin\\data\\temp\\{data[0][8]}.docx'
                    doc.save(file)
                    con.clear()
                    return file
                if ___COUNT >= 4:
                    if i == 4:
                        ___COUNT -= i
                        i = 0
                        self.printingfile(___save())
                    i += 1
                else:
                    # TODO: fix me : jinja2.exceptions.UndefinedError: list object has no element 1
                    # ___save()
                    pass
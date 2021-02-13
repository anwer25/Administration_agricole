from PyQt5.QtCore import QThread, pyqtSignal, QSettings
from PyQt5.QtWidgets import QTableWidget
from bin.worker import dataBaseS
from datetime import datetime
from docxtpl import DocxTemplate

class templateEngine:

    def __init__(self, clientName: str, phoneNumber: str, companyName: str, deviceType: str, deviceBrand: str,
                 deviceModel: str, ID: str,date: str, prePaid: str, price: any, accessories: str, qrimage: str):
        super(templateEngine, self).__init__()
        self.___settings = QSettings('alpha', 'Repair_box')
        self.clientName = clientName
        self.phoneNumber = phoneNumber
        self.companyName = companyName
        self.deviceType = deviceType
        self.deviceBrand = deviceBrand
        self.deviceModel = deviceModel
        self.id = ID
        self.date = date
        self.prePaid = prePaid
        self.price = price
        self.accessories = accessories
        self.qrImage = qrimage
    """
    def run(self) -> None:
        self.templateWriter()
    """
    def templateWriter(self) -> None:
        docx = self.___settings.value('DOC_TEMPLATE', 'templete/temp0.docx', type=str)
        qrImageWidth = self.___settings.value('QR_IMAGE_WIDTH', 1.38)
        qrImageHeight = self.___settings.value('QR_IMAGE_HEIGHT', 1.23)
        logoImageWidth = self.___settings.value('LOGO_WIDTH', 1.38)
        logoImageHeight = self.___settings.value('LOGO_HEIGHT', 1.23)
        measuringUnitLogoImage = self.___settings.value('LOGO_IMAGE_MEASURING_UNIT', 'Inches', type=str)
        measuringUnitQrImage = self.___settings.value('QR_IMAGE_MEASURING_UNIT', 'Inches', type=str)
        logoCodePlace = self.___settings.value('LOGO_KEY', 'LOGO', type=str)
        logoImage = self.___settings.value('LOGO_IMAGE', '', type=str)
        qrCodePlace = self.___settings.value('QR_KEY', 'QR', type=str)
        companyAddressCodePlace = self.___settings.value('COMPANY_ADDRESS_KEY', 'companyAddress', type=str)
        companyAddress = self.___settings.value('COMPANY_ADDRESS', 'test', type=str)
        companyPhonePlace = self.___settings.value('COMPANY_PHONE_KEY', 'companyPhone', type=str)
        companyPhone = self.___settings.value('COMPANY_PHONE', '54876555', type=str)
        companyFaxPlace = self.___settings.value('COMPANY_FAX_KEY', 'companyFax', type=str)
        companyFax = self.___settings.value('COMPANY_FAX', '54578754', type=str)
        companyEmailPlace = self.___settings.value('COMPANY_EMAIL_KEY', 'companyEmail', type=str)
        companyEmail = self.___settings.value('COMPANY_EMAIL', 'aaaaa@test.com', type=str)
        companyWebSitePlace = self.___settings.value('COMPANY_WEB_SITE_KEY', 'companySite', type=str)
        companyWebSite = self.___settings.value('COMPANY_SITE', 'www.test.com', type=str)
        companyNamePlace = self.___settings.value('COMPANY_NAME_KEY', 'Company', type=str)
        companyName = self.___settings.value('COMPANY_NAME__KEY', 'TEST', type=str)
        idPlace = self.___settings.value('ID_KEY', 'ID', type=str)
        datePlace = self.___settings.value('DATE_KEY', 'Date', type=str)
        clientNamePlace = self.___settings.value('CLIENT_NAME_KEY', 'clientName', type=str)
        clientNumberPlace = self.___settings.value('CLIENT_NUMBER_KEY', 'clientNumber', type=str)
        deviceTypePlace = self.___settings.value('DEVICE_TYPE_KEY', 'deviceType', type=str)
        deviceBrandPlace = self.___settings.value('DEVICE_BRAND_KEY', 'deviceBrand', type=str)
        deviceModelPlace = self.___settings.value('DEVICE_MODEL_KEY', 'deviceModel', type=str)
        pricePlace = self.___settings.value('PRICE_KEY', 'price', type=str)
        prePaid = self.___settings.value('PRE_PAID_KEY', 'prePaid', type=str)
        Accessories = self.___settings.value('ACCESSORIES_KEY', 'Accessories', type=str)
        clientCompany = self.___settings.value('CLIENT_COMPANY_PLACE', 'clientcompany', type=str)
        savePlace = self.___settings.value('SAVE_WORD_FILE_PLACE', 'main\\data\\clientsWordFile\\', type=str)

        doc = DocxTemplate(docx)
        try:
            if measuringUnitQrImage == 'Inches':
                qrImageUnit = Inches
            elif measuringUnitQrImage == 'Cm':
                qrImageUnit = Cm
            elif measuringUnitQrImage == 'Mm':
                qrImageUnit = Mm
            else:
                qrImageUnit = Emu
        except NameError:
            qrImageUnit = Inches

        try:
            if measuringUnitLogoImage == 'Inches':
                logoUnit = Inches
            elif measuringUnitLogoImage == 'Cm':
                logoUnit = Cm
            elif measuringUnitLogoImage == 'Mm':
                logoUnit = Mm
            else:
                logoUnit = Emu
        except NameError:
            logoUnit = Inches

        qrImage = InlineImage(doc, self.qrImage, width=qrImageUnit(qrImageWidth),
                              height=qrImageUnit(qrImageHeight))
        if logoImage != '':
            logo = InlineImage(doc, logoImage, width=logoUnit(logoImageWidth), height=logoUnit(logoImageHeight))
        else:
            logo = 'logo'
        context = {
            qrCodePlace: qrImage,
            logoCodePlace: logo,
            companyNamePlace: companyName,
            companyAddressCodePlace: companyAddress,
            companyPhonePlace: companyPhone,
            companyFaxPlace: companyFax,
            companyEmailPlace: companyEmail,
            companyWebSitePlace: companyWebSite,
            idPlace: self.id,
            datePlace: self.date,
            clientNamePlace: self.clientName,
            clientNumberPlace: self.phoneNumber,
            deviceTypePlace: self.deviceType,
            deviceBrandPlace: self.deviceBrand,
            deviceModelPlace: self.deviceModel,
            pricePlace: self.price,
            prePaid: self.prePaid,
            Accessories: self.accessories,
            clientCompany: self.companyName
        }
        doc.render(context)
        doc.save(f'{savePlace}{self.id}.docx')

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

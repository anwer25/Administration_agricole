from bin.searchMethod import Ui_searchMethod
from PyQt5.QtCore import pyqtSignal, QDate
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QPushButton, QRadioButton
from PyQt5.QtGui import QCloseEvent
from datetime import datetime


class mainSearchMethod(QDialog, Ui_searchMethod):
    result = pyqtSignal(list)
    Disable = pyqtSignal()

    def __init__(self, parent=None):
        super(mainSearchMethod, self).__init__(parent)
        self.cancelButtons = None
        self.OkButtons = None
        self.setupUi(self)
        self.Buttons()
        self.Ui()

    def Ui(self):
        """

        :return:
        """
        self.CIN.setEnabled(False)
        self.cancelButtons = self.searchButton.button(QDialogButtonBox.Cancel)
        self.OkButtons = self.searchButton.button(QDialogButtonBox.Ok)
        self.OkButtons.setText('بحث')
        self.cancelButtons.setText('إلغاء')
        todayDate = datetime.today()  # get today time
        dateStr = todayDate.strftime("%Y-%m-%d").split('-')  # convert todayDate to str
        self.dateTO.setMaximumDate(QDate(int(dateStr[0]), int(dateStr[1]), int(dateStr[2])))
        self.dateTO.setDate(QDate(int(dateStr[0]), int(dateStr[1]), int(dateStr[2])))

        def radioButtonSate(obj: QRadioButton):

            if obj.text() == "البحث باستخدام ب.ت.و ":
                self.CIN.setEnabled(True)
                self.dateFrom.setEnabled(False)
                self.dateTO.setEnabled(False)
                self.label.setEnabled(False)
                self.label_2.setEnabled(False)
            else:
                self.CIN.setEnabled(False)
                self.dateFrom.setEnabled(True)
                self.dateTO.setEnabled(True)
                self.label.setEnabled(True)
                self.label_2.setEnabled(True)

        self.dateSearchOnOff.toggled.connect(lambda: radioButtonSate(self.dateSearchOnOff))
        self.cinSearch.toggled.connect(lambda: radioButtonSate(self.cinSearch))
        self.show()

    def Buttons(self):
        """

        :return:
        """

        def searchButtonResult(ButtonName: QPushButton) -> None:
            """

            :param ButtonName:
            :return:
            """
            if ButtonName.text() == 'إلغاء':
                self.close()
            else:
                self.search()

        self.searchButton.clicked.connect(lambda i: searchButtonResult(i))

    def search(self) -> None:
        if self.CIN.isEnabled():
            if self.CIN.text() == "":
                # TODO MAKE MESSAGE HERE IF CIN HAS NO VALUE
                self.result.emit([])
            else:
                self.result.emit([self.CIN.text()])
        else:
            self.result.emit([self.dateFrom.text(), self.dateTO.text()])

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.Disable.emit()

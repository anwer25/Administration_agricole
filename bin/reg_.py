from bin.reg import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class registerWindow(QMainWindow, Ui_MainWindow):
    windowSwitcher = pyqtSignal()

    def __init__(self):
        super(registerWindow, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()

    def Buttons(self):
        pass

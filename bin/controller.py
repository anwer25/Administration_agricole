from bin.main import *
from bin.sync import dataBaseSyncer
from bin.login_ import loginMain
from bin.reg_ import registerWindow
from bin.main import mainW
from bin.loading_ import MainWindow

changer = pyqtSignal()


class windowController:
    def __init__(self):
        self.data = dataBaseSyncer('SELECT * FROM users')
        self.data.start()
        self.data.result.connect(self.windowSwitcher)

    @staticmethod
    def usersShaker(data) -> bool:
        """
        :rtype: bool
        :return: true if there are users else return False
        """
        _ = []
        for row in data:
            _.append(row)
            if len(_) == 1:
                return True
            else:
                return False

    def windowSwitcher(self, data) -> None:
        """
        :rtype: None
        :return: None
        switching between windows
        """
        if self.usersShaker(data):
            self.login = loginMain()
            self.login.windowSwitcher.connect(self.showFromLogin)
        else:
            self.register = registerWindow()
            self.register.windowSwitcher.connect(self.showFromRegister)

    def showFromLogin(self):
        self.loading = MainWindow()
        self.loading.switch_window.connect(self.showMainWindow)
        self.login.close()

    def showFromRegister(self):
        self.loading = MainWindow()
        self.loading.switch_window.connect(self.showMainWindow)
        self.register.close()

    def showMainWindow(self):
        self.mainWindow = mainW()
        self.loading.close()

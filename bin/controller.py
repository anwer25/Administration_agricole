from PyQt5.QtCore import QSettings
import mysql.connector
from bin.sync import dataBaseSyncer
from bin.login_ import loginMain
from bin.reg_ import registerWindow
from bin.main import mainW
from bin.loading_ import MainWindow
from bin.configWindow import mainConfig


class windowController:
    """
    check if there ar users or not and if password and username is correct and from here main window run
    on ___ init___ bin.sync.dataBaseSyncer (sub Qthread Class ) pass Query to it to check there are users and send result
    to windowSwitcher method

    windowSwitcher: get result from dataBase Syncer and pass it to usersShaker Method Base on return from it run
    login Window or register Window (if true login Window will be run else register window)

    userShaker: get users from data and append it list inside for loop i make condition to check if len ==1 (means
    there are user i don't need put all of them inside list to stop iteration i put return ) True return True if
    not return False and back it to condition in windowSwitcher to decide which window will be open

    showFromLogin AND  showFromRegister: displaying loading window wine loading window is run get user name
    privilege and put them to json file

    showMainWindow: displaying mainWindow
    imported files and class : {  bin.sync.dataBaseSyncer
                                  bin.login_.loginMain
                                  bin.reg_.registerWindow
                                  bin.main.mainW
                                  bin.loading_.MainWindow }


    """

    def __init__(self):
        self.login = None
        self.register = None
        self.loading = None
        self.mainWindow = None
        self.config = None
        settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')

        self.___config = {
            'user': settings.value('DATABASE_USER_NAME', '', str),
            # password must changed to ''
            'password': settings.value('DATABASE_PASSWORD', '', str),
            'host': settings.value('DATABASE_HOST', '', str),
            'raise_on_warnings': True
        }

        self.checkConnection()

    def checkConnection(self):
        try:
            connecter = mysql.connector.connect(**self.___config)
        except mysql.connector.Error as err:
            print(f'error from controller 555 {err}')  # for test
            self.displayConfWindow()
        else:
            self.dataBase = dataBaseSyncer('SELECT * FROM users')
            self.dataBase.result.connect(self.windowSwitcher)
            self.dataBase.start()

    def displayConfWindow(self):
        self.config = mainConfig()
        self.config.changeWindow_.connect(self.windowSwitcher)

    def windowSwitcher(self, data: list = None) -> None:
        """

        :param data: user list from dataBase syncer
        :rtype: None
        :return: None
        switching between windows
        """
        try:
            self.dataBase.terminate()
        except AttributeError:
            pass

        def usersShaker(data: list) -> bool:
            """
            :rtype: bool
            :return: true if there are users else return False
            """
            if len(data) >= 1:
                return True
            else:
                return False

        if data is None:
            try:
                connecter = mysql.connector.connect(**self.___config)
            except mysql.connector.Error as err:
                print(f'error from controller 15 {err}')  # for test
                self.displayConfWindow()
            else:
                self.dataBase = dataBaseSyncer('SELECT * FROM users')
                self.dataBase.result.connect(usersShaker)
                self.dataBase.start()
        else:
                if usersShaker(data):
                    try:
                        self.dataBase.terminate()
                    except:
                        pass
                    self.login = loginMain()
                    self.login.windowSwitcher.connect(self.showFromLogin)
                else:
                    try:
                        self.dataBase.terminate()
                    except:
                        pass
                    self.register = registerWindow()
                    self.register.windowSwitcher.connect(self.showFromRegister)

    def showFromLogin(self) -> None:
        """

        :return: None
        """
        self.loading = MainWindow()
        self.loading.switch_window.connect(self.showMainWindow)  # switch between Windows (open Main Window)
        self.login.close()  # close loading Window

    def showFromRegister(self) -> None:
        """
        get signal from login Window
        :return: None
        """
        self.loading = MainWindow()  # open loading Main Window
        self.loading.switch_window.connect(self.showMainWindow)  # switch between windows
        self.register.close()  # close register Window

    def showMainWindow(self) -> None:
        """

        :return: None
        """
        self.mainWindow = mainW()  # mainWindow class
        self.loading.close()  # close loading Window

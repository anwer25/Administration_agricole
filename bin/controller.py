from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from qrc_source import source
import mysql.connector
from bin.sync import dataBaseSyncer
from bin.login_ import loginMain
from bin.reg_ import registerWindow
from bin.main import mainW
from bin.loading_ import MainWindow
from bin.configWindow import mainConfig
from bin.mysqlError import mysqlError


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
        self.dataBase = dataBaseSyncer('SELECT * FROM users')
        self.login = None
        self.register = None
        self.loading = None
        self.mainWindow = None
        self.config = None
        self.messages = QMessageBox()
        settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')  # declare  settings class

        self.___config = {  # DataBase config
            'user': settings.value('DATABASE_USER_NAME', '', str),
            # password must changed to ''
            'password': settings.value('DATABASE_PASSWORD', '', str),
            'host': settings.value('DATABASE_HOST', '', str),
            'database': settings.value('DATABASE_NAME', '', str),
            'raise_on_warnings': True
        }

        self.checkConnection()  # method to check connection

    def ___errorCatch(self, error: str) -> None:
        """
        display Error
        :param error: error name str
        :return: None
        """
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.messages.setWindowIcon(icon)  # add Window icon to Qmessage
        self.messages.setWindowTitle('هناك خطأ')  # add title to Qmessage
        self.messages.setIcon(QMessageBox.Warning)
        self.messages.setText(error)
        self.messages.exec_()
        self.displayConfWindow()

    def checkConnection(self) -> None:
        """
        check connection if there are connection dataBaseSyncer will be run and send result to widnowSwitcher method
        to check if there are users or not
        :return: No return
        """
        # check connection
        try:
            connecter = mysql.connector.connect(**self.___config)
        except mysql.connector.Error as err:
            # if there are error will be displayed as message and run displayConfWindow
            error = mysqlError(err)
            self.___errorCatch(error.__str__())
        else:                                                  # check if there are users on database
            self.dataBase.result.connect(self.windowSwitcher)  # pass result to windowSwitcher method
            self.dataBase.start()
            self.dataBase.errorMessages.connect(lambda i: self.___errorCatch(i))

    def displayConfWindow(self) -> None:
        """
        display confWindow
        :return: No return
        """
        self.config = mainConfig()

    def windowSwitcher(self, data: list = None) -> None:
        """

        :param data: user list from dataBase syncer
        :return: No return
        switching between windows
        """
        try:
            self.dataBase.terminate()  # terminate Qthread
        except AttributeError:
            pass

        def usersShaker(_data: list) -> bool:
            """
            :rtype: bool
            :return: true if there are users else return False
            """
            if len(_data) >= 1:
                return True
            else:
                return False

        if data is None:  # check if data is not None if None check connection again
            try:
                connecter = mysql.connector.connect(**self.___config)
            except mysql.connector.Error as err:
                error = mysqlError(err)
                self.___errorCatch(error.__str__())
            else:
                self.dataBase.result.connect(usersShaker)
                self.dataBase.start()
                self.dataBase.errorMessages.connect(lambda i: self.___errorCatch(i))
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

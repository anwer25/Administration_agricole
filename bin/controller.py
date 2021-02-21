from bin.sync import dataBaseSyncer
from bin.login_ import loginMain
from bin.reg_ import registerWindow
from bin.main import mainW
from bin.loading_ import MainWindow


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
        self.data = dataBaseSyncer('SELECT * FROM users')
        self.data.result.connect(self.windowSwitcher)
        self.data.start()
        self.login = None
        self.register = None
        self.loading = None
        self.mainWindow = None

    @staticmethod
    def usersShaker(data: list) -> bool:
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

    def windowSwitcher(self, data: list) -> None:
        """

        :param data: user list from dataBase syncer
        :rtype: None
        :return: None
        switching between windows
        """
        self.data.terminate()       # to terminate thread
        if self.usersShaker(data):
            self.login = loginMain()
            self.login.windowSwitcher.connect(self.showFromLogin)
        else:
            self.register = registerWindow()
            self.register.windowSwitcher.connect(self.showFromRegister)

    def showFromLogin(self) -> None:
        """

        :return: None
        """
        self.loading = MainWindow()
        self.loading.switch_window.connect(self.showMainWindow)         # switch between Windows (open Main Window)
        self.login.close()                                              # close loading Window

    def showFromRegister(self) -> None:
        """
        get signal from login Window
        :return: None
        """
        self.loading = MainWindow()                                     # open loading Main Window
        self.loading.switch_window.connect(self.showMainWindow)         # switch between windows
        self.register.close()                                           # close register Window

    def showMainWindow(self) -> None:
        """

        :return: None
        """
        self.mainWindow = mainW()                                       # mainWindow class
        self.loading.close()                                            # close loading Window

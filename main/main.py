# fix that
from mainWindow import *


class mainW(Ui_mainwindow):

    def __init__(self):
        Ui_mainwindow.__init__(self)
        self.setupUi(self)
        self.show()

    def UI(self):
        pass

    def Buttons(self):
        pass




if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    apps = mainW()
    sys.exit(app.exec_())


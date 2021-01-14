from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from bin.loading import Ui_MainWindow
from os import path

counter = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        ##################################################
        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadwoFrame.setGraphicsEffect(self.shadow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(100)
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.switch_window.emit()
        counter += 1

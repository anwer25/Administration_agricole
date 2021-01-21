import sys
from PyQt5.QtWidgets import QApplication
from bin.controller import windowController


def run():
    apps = QApplication(sys.argv)
    controller = windowController()
    sys.exit(apps.exec_())


if __name__ == '__main__':
    run()

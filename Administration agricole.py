import sys
from PyQt5.QtWidgets import QApplication
from bin.controller import windowController


def run():
    app = QApplication(sys.argv)
    controller = windowController()
    controller.defaultPasswordShaker()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()

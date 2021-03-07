import sys
from PyQt5.QtWidgets import QApplication
from bin.controller import windowController


def run():
    """
    main programme from here every things begin
    :return: None
    controller: hold windowController class where check connection and if there ar users or not and if password and username is
    correctpip

    imported files and class {  sys
                                PyQt5.QtWidgets.QApplication
                                bin.controller.windowController
                              }
    """
    apps = QApplication(sys.argv)
    # noinspection PyUnusedLocal
    controller = windowController()
    sys.exit(apps.exec_())


if __name__ == '__main__':
    run()

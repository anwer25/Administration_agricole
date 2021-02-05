from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtGui import QDragEnterEvent, QDropEvent


class QTableDrag(QTableWidget):
    def __init__(self, parent=None):
        super(QTableDrag, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        print(f'{e.mimeData().text()}, from DRAGGABLE QTABLE FILE')
        e.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        pass

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import sys


found_words_all = int('100')
l_words_all = ['a', 'b']
data_all = {'hi': ['ab hi', 'bald'], 'hi2': ['d', 'c']}

textMargins = 12
borderMargins = 10


class main_result_all(QtWidgets.QWidget):
    def __init__(self, parent=None, data=None):
        super(main_result_all, self).__init__(parent)

        self.buttonPreview = QtWidgets.QPushButton('Druckvorschau', self)
        self.buttonPreview.setGeometry(QtCore.QRect(555, 700, 250, 30))
        self.buttonPreview.clicked.connect(self.handlePreview)

        self.table = QTableWidget(self)
        self.table.setGeometry(QtCore.QRect(15, 10, 1015, 610))
        self.table.setRowCount(found_words_all)
        self.table.setColumnCount(6)
        stylesheet = "::section{Background-color:rgb(137,137,140);border-radius:14px;font: bold}"
        self.table.horizontalHeader().setStyleSheet(stylesheet)
        self.table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.table.setSortingEnabled(True)

        horHeaders = []
        for col, key in enumerate(sorted(data_all.keys())):
            horHeaders.append(key)
            for row, item in enumerate(data_all[key]):
                clean_item = item
                if type(item) == tuple:
                    clean_item = item[0]
                newitem = QTableWidgetItem(clean_item)
                self.table.setItem(row, col, newitem)

    def handlePreview(self, printer):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.printDocument)
        dialog.exec_()
        '''
        fn, _ = QFileDialog.getSaveFileName(self, 'Speichern unter', None, 'Pdf Dateien (.pdf);;Alle Dateien()')
        if fn != '':
            if QFileInfo(fn).suffix() == "": fn += '.pdf'

            printer = QPrinter(QPrinter.HighResolution)
            printer.setPageSize(QPrinter.A4)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.printDocument.document().print_(printer)
        '''

    def mmToPixels(self, printer, mm):
        return mm * 0.039370147 * printer.resolution()

    def paintPage(self, pageNumber, pageCount, painter, doc, textRect, footerHeight):
        painter.save()
        textPageRect = QtCore.QRectF(QtCore.QPointF(0, pageNumber * doc.pageSize().height()), doc.pageSize())
        painter.setClipRect(textRect)
        painter.translate(0, -textPageRect.top())
        painter.translate(textRect.left(), textRect.top())
        doc.drawContents(painter)
        painter.restore()
        footerRect = QtCore.QRectF(textRect)
        footerRect.setTop(textRect.bottom())
        footerRect.setHeight(footerHeight)

        headerRect = QtCore.QRectF(textRect)
        headerRect.setTop(textRect.top())
        headerRect.setHeight(2 * footerHeight)

        # draw footer
        painter.save()
        pen = painter.pen()
        pen.setColor(QtCore.Qt.black)
        painter.setPen(pen)
        painter.drawText(footerRect, QtCore.Qt.AlignCenter, "Seite {} von {}".format(pageNumber + 1, pageCount))
        painter.drawText(headerRect, QtCore.Qt.AlignLeft, "{}\n{}".format('Projektname:', 'Projektnummer:'))
        #  painter.drawImage(40,40,"Bild-Programm.png")
        #################################
        #  painter.drawPicture(headerRect, QtCore.Qt.AlignRight, "beispiel_bild.png")
        #  painter.drawLine(headerRect, QtCore.Qt.AlignCenter)

        painter.restore()

    def printDocument(self, printer):

        painter = QtGui.QPainter(printer)
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        blockFormat = QtGui.QTextBlockFormat()  #
        # cursor.insertImage("Bild-Programm.png")
        # cursor.setPositon

        cursor.insertBlock(blockFormat)
        blockFormat.setPageBreakPolicy(QtGui.QTextFormat.PageBreak_AlwaysBefore)

        table = cursor.insertTable(self.table.rowCount(), self.table.columnCount())

        for row in range(table.rows()):
            for col in range(table.columns()):
                it = self.table.item(row, col)
                if it is not None:
                    cursor.insertText(it.text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)

        document.print_(printer)

        doc = document

        doc.documentLayout().setPaintDevice(printer)
        doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
        pageSize = printer.pageRect().size()
        tm = self.mmToPixels(printer, textMargins)
        footerHeight = painter.fontMetrics().height()
        textRect = QtCore.QRectF(tm, tm, pageSize.width() - 2 * tm, pageSize.height() - 2 * tm - footerHeight)
        doc.setPageSize(textRect.size())
        pageCount = doc.pageCount()

        for pageIndex in range(pageCount):
            if pageIndex != 0:
                printer.newPage()
            self.paintPage(pageIndex, pageCount, painter, doc, textRect, footerHeight)


def main():
    app = QApplication(sys.argv)
    ex = main_result_all()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
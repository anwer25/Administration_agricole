from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import QRectF, QPointF, Qt, QSizeF
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QTextDocument, QTextCursor, QTextBlockFormat, QTextFormat
from qrc_source import source

textMargins = 500
borderMargins = 300


class Preview(QPrintPreviewDialog):

    def __init__(self, tableWidget: QTableWidget, parent=None):
        super(Preview, self).__init__(parent)
        self.tableWidget = tableWidget
        self.Ui()
        self.Buttons()

    def Ui(self):
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/MainIcon/Image/pngtree-beautiful-wheat-glyph-vector-icon-png-image_2003301.jpg"),
            QIcon.Normal, QIcon.Off)
        self.setWindowTitle('طباعة')
        self.setWindowIcon(icon)

    def Buttons(self):
        self.paintRequested.connect(lambda i: self.printDocument(i))

    def mmToPixels(self, printer, mm):
        return mm * 0.039370147 * printer.resolution()

    def paintPage(self, pageNumber, pageCount, painter, doc, textRect, footerHeight):
        painter.save()
        textPageRect = QRectF(QPointF(0, pageNumber * doc.pageSize().height()), doc.pageSize())
        painter.setClipRect(textRect)
        painter.translate(0, -textPageRect.top())
        painter.translate(textRect.left(), textRect.top())
        doc.drawContents(painter)
        painter.restore()
        footerRect = QRectF(textRect)
        footerRect.setTop(textRect.bottom())
        footerRect.setHeight(footerHeight)

        headerRect = QRectF(textRect)
        headerRect.setTop(textRect.top())
        headerRect.setHeight(2 * footerHeight)

        # draw footer
        painter.save()
        pen = painter.pen()
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawText(footerRect, Qt.AlignCenter, "Seite {} von {}".format(pageNumber + 1, pageCount))
        painter.drawText(headerRect, Qt.AlignLeft, "{}\n{}".format('Projektname:', 'Projektnummer:'))

        painter.restore()

    def printDocument(self, printer):

        painter = QPainter(printer)
        document = QTextDocument()
        cursor = QTextCursor(document)
        blockFormat = QTextBlockFormat()

        cursor.insertBlock(blockFormat)
        blockFormat.setPageBreakPolicy(QTextFormat.PageBreak_AlwaysBefore)

        table = cursor.insertTable(self.tableWidget.rowCount(), self.tableWidget.columnCount())

        for row in range(table.rows()):
            for col in range(table.columns()):
                it = self.tableWidget.item(row, col)
                if it is not None:
                    cursor.insertText(it.text())
                cursor.movePosition(QTextCursor.NextCell)

        document.print_(printer)

        doc = document

        doc.documentLayout().setPaintDevice(printer)
        doc.setPageSize(QSizeF(printer.pageRect().size()))
        pageSize = printer.pageRect().size()
        tm = self.mmToPixels(printer, textMargins)
        footerHeight = painter.fontMetrics().height()
        textRect = QRectF(tm, tm, pageSize.width() - 2 * tm, pageSize.height() - 2 * tm - footerHeight)
        doc.setPageSize(textRect.size())
        pageCount = doc.pageCount()

        for pageIndex in range(pageCount):
            if pageIndex != 0:
                printer.newPage()
            self.paintPage(pageIndex, pageCount, painter, doc, textRect, footerHeight)
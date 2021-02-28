from PyQt5.QtCore import QObject, pyqtSignal
import mysql.connector
from mysql.connector import errorcode


class mysqlError(QObject):
    errorType = pyqtSignal(str)

    def __init__(self, error: mysql.connector.errors):
        super(mysqlError, self).__init__()
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            # TODO: make message here
            self.errorType.emit("Something is wrong with your user name or password")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            # TODO: make message here
            self.errorType.emit("Database does not exist")
        elif error.errno == errorcode.CR_CONN_HOST_ERROR:
            # TODO: make message here
            self.errorType.emit(f'error line  : {error}')
        elif error.errno == errorcode.ER_TRUNCATED_WRONG_VALUE_FOR_FIELD:
            # TODO: make message here
            self.errorType.emit(f'you entered str value instead int value error line : {error.errno}')
        elif error.errno == errorcode.ER_WARN_DATA_OUT_OF_RANGE:
            # TODO: make message here
            self.errorType.emit(f'you entered long value sync file  : {error.errno}')
        elif error.errno == errorcode.ER_BAD_FIELD_ERROR:
            self.errorType.emit(f'Error from line   bad field error: {error.errno}')
        elif error.errno == errorcode.ER_NO_SUCH_TABLE:
            self.errorType.emit(f'Error from line : NO SUCH TABLE: {error.errno}')
        elif error.errno == errorcode.ER_WRONG_VALUE_COUNT_ON_ROW:
            self.errorType.emit(f'Error from line  values provided in the INSERT '
                                f'statement is f bigger or smaller than the number of columns the table has: {error.errno}')
        elif error.errno == errorcode.ER_PARSE_ERROR:
            self.errorType.emit(f'Error from line : PARSE ERROR: {error.errno}')
        elif error.errno == errorcode.ER_DUP_ENTRY:
            self.errorType.emit(f'Error from line : DUP ENTRY: {error.errno}')
        else:
            self.errorType.emit(f'Error from line : {error.errno}')

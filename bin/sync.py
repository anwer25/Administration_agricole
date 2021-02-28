import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QSettings


class dataBaseSyncer(QThread):
    """
    sub class of Qthread
    object of this sub is get query from file where declared and back to the result of the query using pyqtsignal
    i usng Qthread to avoid window freezing wine Querying big data or use for loop
    used instance {
        global instance{
            result: i dont know remove it or no
            Deanshipresult: send Deanship result to window where class is declared DONT CANCEL THIS INSTANCE
            refresher: whine Query has keys(UPDATE OR REMOVE OR INSERT) refresher send signal to refresh table data
            messages : send error to user if there are problem with mysql Query I DONT WHAT TYPE I MUST SEND
        }
        local instance {
            self.com: where Query  is leave type str
            self.connection: where mysql connector class is leave
            self.settings:  where Qsettings class leave
            config:where mysql config is leave (password database name ......)
            cursor: where connection.cursor() method is leave

        }

    }
    used Method {
        global Method{
            None
        }

        local Method {
            run(self): sub method from Qthread and declared usng start method from where this class is caled
            _connecter: where quarrying data and back the result
            protected Method{
                ___error(self,error):  where save errors
            }

        }
    }
    imported files or class{
            mysql.connector:
            mysql.connector import errorcode:
            PyQt5.QtCore import QThread, pyqtSignal:
            PyQt5.QtCore import QSettings:
    }

    """
    result = pyqtSignal(list)
    Deanshipresult = pyqtSignal(str)
    refresher = pyqtSignal()
    messages = pyqtSignal()

    def __init__(self, com: str):
        super(dataBaseSyncer, self).__init__()
        self.com = com
        self.connection = None
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')

    def run(self) -> None:
        self._connecter()

    def _connecter(self) -> None:

        """
        :rtype: None
        :return:dataBase Query result 
        """
        config = {
            'user': self.settings.value('DATABASE_USER_NAME', 'root', str),
            # password must changed to ''
            'password': self.settings.value('DATABASE_PASSWORD', 'admin', str),
            'host': self.settings.value('DATABASE_HOST', 'localhost', str),
            'database': self.settings.value('DATABASE_NAME', 'administration-agricole', str),
            'raise_on_warnings': True
        }
        try:
            self.connection = mysql.connector.connect(**config)
            cursor = self.connection.cursor()
            if 'INSERT' in self.com or 'UPDATE' in self.com or 'DELETE' in self.com:
                cursor.execute(self.com)
                self.connection.commit()
                self.connection.close()
                self.refresher.emit()
            else:
                try:
                    if "DEANSHIPS" in self.com or 'prosecutionoffices' in self.com:
                        cursor.execute(self.com)
                        for Deanship in cursor.fetchall():
                            self.Deanshipresult.emit(str(Deanship))
                    else:
                        # TODO: must removed from threading
                        print(self.com)                             # for testing
                        cursor.execute(self.com)
                        self.result.emit(cursor.fetchall())
                except TypeError as e:
                    print(f'error line 42 from sync file {e}')

        except mysql.connector.Error as err:
            self.___error(err)
        else:
            self.connection.close()

        finally:
            pass

    def ___error(self, error: mysql.connector.Error):
        """

        :param error:
        :return:
        """
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            # TODO: make message here
            print("Something is wrong with your user name or password")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            # TODO: make message here
            print("Database does not exist")
        elif error.errno == errorcode.CR_CONN_HOST_ERROR:
            # TODO: make message here
            print(f'error line 63 sync : {error}')
        elif error.errno == errorcode.ER_TRUNCATED_WRONG_VALUE_FOR_FIELD:
            # TODO: make message here
            print(f'you entered str value instead int value error line 23 SYNC: {error.errno}')
        elif error.errno == errorcode.ER_WARN_DATA_OUT_OF_RANGE:
            # TODO: make message here
            print(f'you entered long value sync file line 23 : {error.errno}')
        elif error.errno == errorcode.ER_BAD_FIELD_ERROR:
            print(f'Error from line 23 sync file class dataBaseSyncer bad field error: {error.errno}')
        elif error.errno == errorcode.ER_NO_SUCH_TABLE:
            print(f'Error from line 23 sync file class dataBaseSyncer: NO SUCH TABLE: {error.errno}')
        elif error.errno == errorcode.ER_WRONG_VALUE_COUNT_ON_ROW:
            print(f'Error from line 23 sync file class dataBaseSyncer: values provided in the INSERT statement is '
                  f'bigger or smaller than the number of columns the table has: {error.errno}')
        elif error.errno == errorcode.ER_PARSE_ERROR:
            print(f'Error from line 23 sync file class dataBaseSyncer: PARSE ERROR: {error.errno}')
        elif error.errno == errorcode.ER_DUP_ENTRY:
            print(f'Error from line 23 sync file class dataBaseSyncer: DUP ENTRY: {error.errno}')
        else:
            print(f'Error from line 23 sync file class dataBaseSyncer: {error.errno}')

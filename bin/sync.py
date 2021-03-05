import mysql.connector
from bin.mysqlError import mysqlError
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap


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

            }

        }
    }
    imported files or class{
            mysql.connector:
            PyQt5.QtCore import QThread, pyqtSignal:
            PyQt5.QtCore import QSettings:
    }

    """
    result = pyqtSignal(list)
    Deanshipresult = pyqtSignal(str)
    refresher = pyqtSignal()
    errorMessages = pyqtSignal(str)

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
            'database': self.settings.value('DATABASE_NAME', 'administration_agricole', str),
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
                        cursor.execute(self.com)
                        self.result.emit(cursor.fetchall())
                except TypeError as e:
                    print(f'error line 91 or 96 from sync file {e}')

        except mysql.connector.Error as err:
            error = mysqlError(err)
            self.errorMessages.emit(error.__str__())
        else:
            self.connection.close()

        finally:
            pass

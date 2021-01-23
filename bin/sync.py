import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QSettings


class dataBaseSyncer(QThread):
    result = pyqtSignal(list)
    Deanshipresult = pyqtSignal(str)

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
            'host': self.settings.value('DATABASE HOST', 'localhost', str),
            'database': self.settings.value('DATABASE_NAME', 'administration-agricole', str),
            'raise_on_warnings': True
        }
        try:
            self.connection = mysql.connector.connect(**config)
            cursor = self.connection.cursor()
            if 'INSERT' in self.com or 'UPDATE' in self.com or 'DELETE' in self.com:
                cursor.execute(self.com)
                self.connection.commit()
            else:
                try:
                    if "DEANSHIPS" in self.com:
                        cursor.execute(self.com)

                        for Deanship in cursor.fetchall():
                            self.Deanshipresult.emit(str(Deanship))
                    else:
                        cursor.execute(self.com)
                        self.result.emit(cursor.fetchall())
                except TypeError as e:
                    print(f'error line 42 from sync file {e}')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                # TODO: make message here
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                # TODO: make message here
                print("Database does not exist")
            else:
                print(f'Error from line 23 sync file class dataBaseSyncer: {err}')
        else:
            self.connection.close()

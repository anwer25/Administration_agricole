from PyQt5.QtSql import *


class Database():
    def __init__(self, hostname, user, dbase, pword=""):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName(hostname)
        self.db.setDatabaseName(dbase)
        self.db.setUserName(user)
        self.db.setPassword(pword)
        ok = self.db.open()
        self.db.

mydb = Database("localhost", "root", "billingsys")
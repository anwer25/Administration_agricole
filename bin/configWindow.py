from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSettings
import mysql.connector
from bin.conf import Ui_config
from bin.mysqlError import mysqlError


class mainConfig(QMainWindow, Ui_config):

    def __init__(self, parent=None):
        super(mainConfig, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('ALPHASOFT', 'ADMINISTRATION_AGRICOLE')
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()

    def Buttons(self):
        self.cancel.clicked.connect(self.close)
        self.save.clicked.connect(self.saveData)

    def saveData(self):
        try:
            config = {
                'user': self.dbUserName.text(),
                'password': self.dbPassword.text(),
                'host': self.dbHost.text(),
                'raise_on_warnings': True
            }
            connection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            ___mysqlError = mysqlError(err)
            print(___mysqlError.__str__())
        else:
            def ___dataBaseBuilder(con: mysql.connector.connect):
                pass
            if connection.is_connected():
                self.settings.setValue('DATABASE_USER_NAME', self.dbUserName.text())
                self.settings.setValue('DATABASE_PASSWORD', self.dbPassword.text())
                self.settings.setValue('DATABASE_HOST', self.dbHost.text())
                self.settings.sync()
                curser = connection.cursor()
                curser.execute(f'CRATE DATABASE IF NOT EXISTS administration-agricole')
                Query = """
                
                SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
                START TRANSACTION;
                SET time_zone = "+00:00";
                SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT;
                SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS;
                SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION;
                SET NAMES utf8mb4;
                
                CREATE TABLE `deanships` (
                    `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `H_NUMBER` int(255) DEFAULT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                
                CREATE TABLE `farmers` (
                    `ID` int(11) NOT NULL,
                    `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `LASTNAME` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `DEANSHIP` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `PHONENUMBER` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `HEADNUMBERS` int(255) DEFAULT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                
                CREATE TABLE `history` (
                    `CIN` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `LASTNAME` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `DEANSHIP` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `ProsectutionOffices` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `NUMBEROFBAGS` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `DATE_` varchar(255) DEFAULT current_timestamp(),
                    `TIKETID` int(11) NOT NULL,
                    `PRINTID` varchar(255) CHARACTER SET utf8 DEFAULT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                    
                CREATE TABLE `prosecutionoffices` (
                    `NAME_` varchar(255) CHARACTER SET utf8 NOT NULL,
                    `LASTNAME` varchar(255) CHARACTER SET utf8 NOT NULL,
                    `ADDRESS` varchar(255) CHARACTER SET utf8 NOT NULL,
                    `PHONENUMBER` varchar(13) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                
                CREATE TABLE `users` (
                    `USER_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
                    `history` tinyint(1) NOT NULL DEFAULT 0,
                    `distribution` tinyint(1) NOT NULL DEFAULT 0,
                    `settings` tinyint(1) NOT NULL DEFAULT 0,
                    `password` longtext CHARACTER SET utf8 DEFAULT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                
                ALTER TABLE `deanships` ADD UNIQUE KEY `NAME_` (`NAME_`);
                ALTER TABLE `farmers` ADD PRIMARY KEY (`ID`), ADD UNIQUE KEY `ID` (`ID`);
                ALTER TABLE `history` ADD PRIMARY KEY (`TIKETID`), ADD UNIQUE KEY `PRINTID` (`PRINTID`);
                ALTER TABLE `prosecutionoffices` ADD UNIQUE KEY `NAME_` (`NAME_`);
                ALTER TABLE `users` ADD UNIQUE KEY `USER_` (`USER_`);
                ALTER TABLE `history` MODIFY `TIKETID` int(11) NOT NULL AUTO_INCREMENT;
                SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT ;
                SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS ;
                SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION ;
                """
from passlib.context import CryptContext
from PyQt5.QtCore import QObject, pyqtSignal


class Key:
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )


class Crypt(QObject):
    passwordAndUserName = pyqtSignal(str)

    def __init__(self, password: str):
        self.password = password

    def encryptUserNameAndPassword(self) -> None:
        return Key.pwd_context.encrypt(self.password)


class Dcrypt(QObject):

    def __init__(self, password: str, dbPassword: str):
        super(Dcrypt, self).__init__()
        self.password = password
        self.dbPassword = dbPassword[0]

    def passwordShaker(self) -> None:
        """

        :return: bool
        """
        if Key.pwd_context.verify(self.password, str(self.dbPassword)[2:-3]):
            return True
        else:
            return False

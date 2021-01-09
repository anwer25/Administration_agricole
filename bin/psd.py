from passlib.context import CryptContext
from PyQt5.QtCore import QThread, pyqtSignal


class Key:
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )


class Crypt(QThread):
    passwordAndUserName = pyqtSignal(str, str)

    def __init__(self, username: str, password: str):
        super(Crypt, self).__init__()
        self.username = username
        self.password = password

    def run(self) -> None:
        self.encryptUserNameAndPassword()

    def encryptUserNameAndPassword(self) -> None:
        self.passwordAndUserName.emit(Key.pwd_context.encrypt(self.password))

class Dcrypt(QThread):
    def __init__(self, password):
        super(Dcrypt, self).__init__()
        self.password = password

    def run(self) -> None:
        self.usernameShaker()

    def usernameShaker(self):
        if Key.pwd_context.verify(self.userName):
            self.passwordShaker()

    def passwordShaker(self):
        pass

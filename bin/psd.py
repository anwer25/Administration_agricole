from passlib.context import CryptContext
from PyQt5.QtCore import QThread, pyqtSignal


class Key:
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )


class Crypt(QThread):
    passwordAndUserName = pyqtSignal(str)

    def __init__(self, username, password):
        super(Crypt, self).__init__()
        self.username = username
        self.password = password

    def run(self) -> None:
        self.encryptUserName()
        self.encryptPassword()

    def encryptPassword(self) -> None:
        self.passwordAndUserName.emit(Key.pwd_context.encrypt(self.password))

    def encryptUserName(self) -> None:
        self.passwordAndUserName.emit(Key.pwd_context.encrypt(self.username))

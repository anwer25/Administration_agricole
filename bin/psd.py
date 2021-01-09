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

    def __init__(self, password: str):
        super(Crypt, self).__init__()
        self.password = password

    def run(self) -> None:
        self.encryptUserNameAndPassword()

    def encryptUserNameAndPassword(self) -> None:
        self.passwordAndUserName.emit(Key.pwd_context.encrypt(self.password))


class Dcrypt(QThread):
    state = pyqtSignal(bool)

    def __init__(self, password: str, dbPassword: str):
        super(Dcrypt, self).__init__()
        self.password = password
        self.dbPassword = dbPassword[0]

    def run(self) -> None:
        self.passwordShaker()

    def passwordShaker(self):
        if Key.pwd_context.verify(self.password, str(self.dbPassword)[2:-4]):
            self.state.emit(True)
        else:
            self.state.emit(False)

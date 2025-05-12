import hashlib
import hmac
import struct
import time

from PyQt6.QtWidgets import QMainWindow, QLineEdit, QApplication
from PyQt6.QtCore import Qt
from ui.LoginWindow import Ui_MainWindow
import sys
import sqlite3


class LoginWindow(QMainWindow, Ui_MainWindow):
    """Class for the Login window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        """Signal-slots connections"""
        self.button_login.clicked.connect(self.log_in_button)
        self.lineEdit_username.textEdited.connect(self.status_bar_reset)
        self.lineEdit_password.textEdited.connect(self.status_bar_reset)
        self.checkBox_show_password.stateChanged.connect(self.show_hide_password)

    def status_bar_reset(self):
        """This function resets color and status of statusbar"""
        self.statusBar.clearMessage()
        self.statusBar.setStyleSheet("background-color : #f0f0f0")

    def show_hide_password(self):
        """This function shows or hides text in password field"""
        if self.checkBox_show_password.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

    def hash_user_id(self,name: str) -> str:
        """
        使用 SHA256 对用户 ID 进行不可逆加密（哈希）
        """
        sha256 = hashlib.sha256()
        sha256.update(name.encode('utf-8'))
        return sha256.hexdigest()  # 返回十六进制字符串

    def generate_2fa_code(secret_hex: str, interval: int = 30, digits: int = 6) -> str:
        """
        使用 TOTP 算法基于 secret_hex 生成一个6位动态验证码
        - secret_hex：哈希后的十六进制密钥
        - interval：时间间隔（默认30秒）
        - digits：验证码位数（默认6位）
        """
        # 将十六进制的 secret 转为字节
        secret = bytes.fromhex(secret_hex)

        # 获取当前 Unix 时间段（30秒为一个时间窗口）
        counter = int(time.time() / interval)
        counter_bytes = struct.pack(">Q", counter)  # 8字节大端整数

        # HMAC-SHA1 计算
        hmac_digest = hmac.new(secret, counter_bytes, hashlib.sha1).digest()

        # 动态截取（Dynamic Truncation）
        offset = hmac_digest[-1] & 0x0F
        code = struct.unpack(">I", hmac_digest[offset:offset + 4])[0] & 0x7FFFFFFF
        return str(code % (10 ** digits)).zfill(digits)

    def log_in_button(self):
        """Login logic using sqlite3 database"""
        username = self.lineEdit_username.text()
        password = self.lineEdit_password_2.text()
        token = self.lineEdit_password.text()

        if username == "":
            self.statusBar.showMessage("Please, enter a username.")
            self.statusBar.setStyleSheet("background-color : pink")
        elif password == "":
            self.statusBar.showMessage("Please, enter a password.")
            self.statusBar.setStyleSheet("background-color : pink")
        else:
            try:
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("SELECT username FROM credentials WHERE username=? AND password=?", (username, password))

                if not cursor.fetchone():
                    self.statusBar.showMessage("Username or Password is incorrect.")
                    self.statusBar.setStyleSheet("background-color : pink")
                else:
                    self.statusBar.showMessage("Access granted!")
                    self.statusBar.setStyleSheet("background-color : lightgreen")

                    hashed_id = self.hash_user_id(username)
                    print("Hashed ID (SHA256):", hashed_id)

                    # 第二步：生成动态验证码
                    code = self.generate_2fa_code(hashed_id)
                    print("2FA Code:", code)

            except sqlite3.Error as e:
                self.statusBar.showMessage(f"Database error: {e}")
                self.statusBar.setStyleSheet("background-color : pink")

            finally:
                conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

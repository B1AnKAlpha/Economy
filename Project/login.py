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

    def log_in_button(self):
        """Login logic using sqlite3 database"""
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

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

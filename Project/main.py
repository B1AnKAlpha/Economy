# -*- coding: utf-8 -*-
# from. resources_rc import *
# https://up.ly93.cc/
# pyside6-rcc resources.qrc -o resources_rc.py
# pyside6-uic LoginWindow.ui -o LoginWindow.py
# pyside6-uic main.ui> ui_main.py
# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
import ctypes
import re
import secrets
import shutil
import socket
import stat
import subprocess
import uuid
import zipfile
from datetime import datetime
from functools import partial
from io import BytesIO

import qrcode
from PIL.ImageQt import ImageQt
from cryptography.fernet import Fernet
import psutil
import pyzipper

username = "blank"
admin = 1
debug = True
import base64
import hashlib
import hmac
import struct
import pyotp
import final.main
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import time
import socket
import uuid
import platform
import pymysql
import psutil
from datetime import datetime
import pymysql
import platform
import requests
import tkinter as tk
from tkinter import messagebox
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from PySide6.QtWidgets import QMainWindow, QLineEdit, QApplication
from PySide6.QtCore import Qt
from widgets.ui.LoginWindow import Ui_MainWindow as LoginMainWindows
import sys
import sqlite3

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
os.environ["QT_FONT_DPI"] = "150"  # FIX Problem for High DPI and Scale above 100%
current_version = "1.0.3"


class LoginWindow(QMainWindow, LoginMainWindows):
    """Class for the Login window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.main_window = None
        if debug:
            self.username = "admin"
            self.password = "admin"
            self.open_main_window()
            secret = self.get_base32_secret(self.username, self.password)
            fa = self.generate_2fa_code_base32(secret)
            totp = pyotp.TOTP(secret)

            print("Secret:", totp)

    def upload_security_event(self, event_type="抓包检测", app_version=current_version, extra_info=""):
        try:
            # 获取主板 UUID（Windows 下有效）
            try:
                import subprocess
                cmd = 'wmic csproduct get uuid'
                uuid_output = subprocess.check_output(cmd, shell=True).decode()
                motherboard = uuid_output.split('\n')[1].strip()
            except:
                motherboard = str(uuid.getnode())

            # 获取本地 IP 地址
            ip_address = socket.gethostbyname(socket.gethostname())

            # 获取 MAC 地址
            mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                                    for elements in range(0, 2 * 6, 8)][::-1])

            # 获取操作系统信息
            os_info = platform.platform()

            # 获取当前时间
            event_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 建立数据库连接
            cloud_conn = pymysql.connect(
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )
            cursor = cloud_conn.cursor()

            # 插入数据
            sql = """
            INSERT INTO security_events (
                event_time, event_type, ip_address, mac_address, 
                motherboard, os_info, app_version, extra_info
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (event_time, event_type, ip_address, mac_address,
                      motherboard, os_info, app_version, extra_info)

            cursor.execute(sql, values)
            cloud_conn.commit()
            print("异常事件已上传数据库")
        except Exception as e:
            print("上传失败：", e)
        finally:
            try:
                cursor.close()
                cloud_conn.close()
            except:
                pass

    def reset_login_fields(self):
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()
        self.lineEdit_token.clear()
        self.statusBar.showMessage("已安全退出")

    # self.statusBar.hide()  # 如果你之前 show() 过 statusBar

    def show_force_exit_popup(self, title: str, message: str, parent: QWidget = None):
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setStandardButtons(QMessageBox.Ok)

        # 禁用关闭按钮
        msg_box.setWindowFlag(Qt.WindowCloseButtonHint, False)
        msg_box.setWindowModality(Qt.ApplicationModal)

        # 阻塞式执行
        ret = msg_box.exec()

        if ret == QMessageBox.Ok:
            QApplication.quit()

    def sha256sum(self, filepath):
        """计算文件的 SHA-256 散列值"""
        h = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()

    def check_file_integrity(self, filepath, expected_hash):
        with open(filepath, 'rb') as f:
            file_data = f.read()
            actual_hash = hashlib.sha256(file_data).hexdigest()
        return actual_hash == expected_hash

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

    def generate_2fa_code_base32(self, secret_base32: str, interval: int = 30, digits: int = 6) -> str:
        """
        基于 Base32 编码密钥生成 TOTP 动态验证码
        - secret_base32: 例如 '7J64V3P3E77J3LKNUGSZ5QANTLRLTKVL'
        - interval: 时间窗口（秒），默认30
        - digits: 验证码位数，默认6
        """
        # 将 Base32 字符串转为字节（忽略大小写、空格）
        secret = base64.b32decode(secret_base32.upper(), casefold=True)

        # 当前时间窗口计数器
        counter = int(time.time() / interval)
        counter_bytes = struct.pack(">Q", counter)

        # 计算 HMAC-SHA1 摘要
        hmac_digest = hmac.new(secret, counter_bytes, hashlib.sha1).digest()

        # 动态截断获取验证码
        offset = hmac_digest[-1] & 0x0F
        code = struct.unpack(">I", hmac_digest[offset:offset + 4])[0] & 0x7FFFFFFF
        return str(code % (10 ** digits)).zfill(digits)

    def get_base32_secret(self, username: str, password: str) -> str | None:
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            # 查询base32字段
            query = "SELECT base32 FROM register WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            if result:
                return result[0]  # base32 密钥字符串
            else:
                return None
        finally:
            cursor.close()
            conn.close()

    def get_isadmin(self, username: str, password: str) -> str | None:
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            # 查询base32字段
            query = "SELECT isadmin FROM register WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            if result:
                return result[0]  # base32 密钥字符串
            else:
                return None
        finally:
            cursor.close()
            conn.close()

    def check_machinecode(self, m1):
        import pymysql

        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            query = "SELECT code FROM machinecode WHERE code = %s"
            cursor.execute(query, (m1,))
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()
            conn.close()

    def check_credentials(self, username, password):
        # 建立连接
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",  # 通常数据库名和用户名相同，如果你没建别的库
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            # 执行查询
            query = "SELECT username FROM register WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            return result is not None  # 如果查询到结果，说明账号密码正确

        finally:
            cursor.close()
            conn.close()

    def get_machine_code(self):
        system = platform.system()

        try:
            if system == "Windows":
                # 获取主板序列号
                output = subprocess.check_output("wmic baseboard get serialnumber", shell=True)
                serial = output.decode().split("\n")[1].strip()
            elif system == "Linux":
                # 获取硬盘UUID（也可替换为 MAC）
                output = subprocess.check_output("cat /etc/machine-id", shell=True)
                serial = output.decode().strip()
            elif system == "Darwin":
                # macOS 获取主板UUID
                output = subprocess.check_output("ioreg -rd1 -c IOPlatformExpertDevice", shell=True)
                serial = re.search(r'"IOPlatformUUID" = "(.+)"', output.decode()).group(1)
            else:
                # 兜底使用 MAC 地址
                serial = uuid.getnode()
            # 返回 SHA256 加密后的机器码，更安全
            return serial
        except Exception as e:
            return "UNKNOWN"

    def detect_packet_sniffer(self):
        packet_sniffer_processes = ["wireshark", "fiddler", "charles", "tcpdump", "mitmproxy"]
        # 获取当前运行的进程列表
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # 检查进程名是否与常见抓包工具匹配
                if any(sniffer in proc.info['name'].lower() for sniffer in packet_sniffer_processes):
                    print(f"Detected packet sniffer: {proc.info['name']} (PID: {proc.info['pid']})")
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def log_in_button(self):
        machinecode = self.get_machine_code()
        print("机器码", machinecode)
        self.statusBar.showMessage("正在进行基本环境检测...")
        self.statusBar.setStyleSheet("background-color : lightgreen")
        global username
        username = self.lineEdit_username.text()
        with open("./final/user.txt", "w", encoding="utf-8") as f:
            f.write(username)
        self.username = username
        self.password = self.lineEdit_password.text()
        self.token = self.lineEdit_token.text()
        # 先进行文件完整性检查
        important_file = "main.py"
        expected_hash = self.sha256sum(important_file)
        # expected_hash = 1
        if not self.check_file_integrity(important_file, expected_hash):
            self.statusBar.showMessage("检测到文件损坏或篡改，请重新下载程序")
            self.statusBar.setStyleSheet("background-color : red")
            self.upload_security_event(
                event_type="文件篡改",
            )

            QTimer.singleShot(1000, lambda: self.show_force_exit_popup("提示",
                                                                       "检测到文件损坏或篡改，请重新下载程序，已上报基本信息"))
            QTimer.singleShot(3000, sys.exit)
            return
        else:
            self.statusBar.showMessage("文件完整性检查通过")
            self.statusBar.setStyleSheet("background-color : lightgreen")

        # 延迟执行抓包检测（2 秒后）
        QTimer.singleShot(500, self.run_sniffer_check)

    def machinecode_check(self):
        machine = self.get_machine_code()
        # machine=1
        if not self.check_machinecode(machine):
            self.statusBar.showMessage("该机器码未注册，请联系管理员")
            self.statusBar.setStyleSheet("background-color : red")
            self.upload_security_event(
                event_type="机器码未注册",
            )
            QTimer.singleShot(1000,
                              lambda: self.show_force_exit_popup("提示", "该机器码未注册，请联系管理员，已上报基本信息"))
            QTimer.singleShot(3000, sys.exit)
        else:
            self.statusBar.showMessage("机器码检查通过")
            self.statusBar.setStyleSheet("background-color : lightgreen")
            QTimer.singleShot(500, self.verify_credentials)

    def run_sniffer_check(self):
        if self.detect_packet_sniffer():
            self.statusBar.showMessage("检测到抓包工具，请关闭后重试")
            self.upload_security_event(
                event_type="检测到抓包工具",
            )
            self.statusBar.setStyleSheet("background-color : red")
            QTimer.singleShot(1000,
                              lambda: self.show_force_exit_popup("提示", "检测到抓包工具，请关闭后重试，已上报基本信息"))
            QTimer.singleShot(3000, sys.exit)
        else:
            self.statusBar.showMessage("反抓包检查通过")
            self.statusBar.setStyleSheet("background-color : lightgreen")
            QTimer.singleShot(500, self.machinecode_check)

    def open_main_window(self):
        self.main_window = MainWindow(self)  # 传入当前登录窗口给主窗口
        self.main_window.show()
        self.hide()  # 隐藏登录窗口

    def verify_credentials(self):
        self.statusBar.showMessage("正在进行登录验证...")
        self.statusBar.setStyleSheet("background-color : lightgreen")

        if self.username == "":
            self.statusBar.showMessage("请输入账号")
            self.statusBar.setStyleSheet("background-color : pink")
            return

        if self.password == "":
            self.statusBar.showMessage("请输入密码")
            self.statusBar.setStyleSheet("background-color : pink")
            return

        try:
            if not self.check_credentials(self.username, self.password):
                self.statusBar.showMessage("账号或密码错误.")
                self.statusBar.setStyleSheet("background-color : pink")
                return

            secret = self.get_base32_secret(self.username, self.password)
            fa = self.generate_2fa_code_base32(secret)
            totp = pyotp.TOTP(secret)

            print("Secret:", secret)
            print("生成动态码:", fa)
            print("pyotp 代码:", totp.now())
            print("用户输入 Token:", self.token)

            if fa == self.token:
                global admin
                admin = self.get_isadmin(self.username, self.password)
                print("是否为管理员：", admin)
                username = self.username
                if admin == 1:
                    self.statusBar.showMessage("欢迎您，管理员！正在跳转中...")
                else:
                    self.statusBar.showMessage("欢迎您，认证用户！正在跳转中...")

                self.statusBar.setStyleSheet("background-color : lightgreen")
                QTimer.singleShot(1000, self.open_main_window)
            else:
                self.statusBar.showMessage("动态密码错误")
                self.statusBar.setStyleSheet("background-color : pink")

        except Exception as e:
            print("错误：", e)
            self.statusBar.showMessage(f"数据库错误: {e}")
            self.statusBar.setStyleSheet("background-color : pink")


def confirm_delete(uname):
    pass


username


class MainWindow(QMainWindow):
    def __init__(self, login_window):
        QMainWindow.__init__(self)

        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.g = 0
        self.h = 0
        self.i = 0
        self.id = 0
        self.transModelLink = None
        self.uploadtext = ""
        self.uploadfile = []
        self.str = ""
        self.login_window = login_window

        # SET AS GLOBAL

        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        if admin != 1:
            self.ui.version.setText("账户级别：操作员")
            print("fw")
            layout = self.ui.verticalLayout_46
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                widget = item.widget()
                if widget is not None:
                    widget.hide()  # 等价于 widget.setVisible(False)

        title = "金盾·FraudShield - Modern GUI"
        description = "金盾·FraudShield - 金融数据欺诈检测系统"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        UIFunctions.toggleMenu(self, True)
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_themechange.clicked.connect(self.buttonClick)
        widgets.btn_upload.clicked.connect(self.buttonClick)
        widgets.btn_update.clicked.connect(self.buttonClick)
        widgets.btn_para.clicked.connect(self.buttonClick)
        widgets.btn_information.clicked.connect(self.buttonClick)
        widgets.pushButton_50.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.pushButton_4.clicked.connect(self.buttonClick)
        widgets.pushButton_5.clicked.connect(self.buttonClick)
        widgets.pushButton_3.clicked.connect(self.buttonClick)
        widgets.pushButton_39.clicked.connect(self.buttonClick)
        widgets.pushButton_42.clicked.connect(self.buttonClick)
        widgets.pushButton_40.clicked.connect(self.buttonClick)
        widgets.pushButton_41.clicked.connect(self.buttonClick)
        widgets.pushButton_43.clicked.connect(self.buttonClick)
        widgets.pushButton_44.clicked.connect(self.buttonClick)
        widgets.pushButton_45.clicked.connect(self.buttonClick)
        widgets.pushButton_46.clicked.connect(self.buttonClick)
        widgets.pushButton_47.clicked.connect(self.buttonClick)
        widgets.pushButton_51.clicked.connect(self.buttonClick)
        widgets.pushButton_2.clicked.connect(self.buttonClick)
        global button_style1
        global button_style2
        global button_stylered
        global button_styleblack
        global button_stylewhite
        button_style1 = """
QPushButton {

    min-width: 100px;
    max-width: 100px;
    color: #000000;
}

"""
        button_stylered = """
        QPushButton {

            color: red;
        }

        """

        button_style2 = """
        QPushButton {

            min-width: 100px;
            max-width: 100px;
            color: #ffffff;
        }
        

        """
        button_styleblack = """
        QPushButton {
            color: black;
        }
        """
        button_stylewhite = """
                QPushButton {
                    color: white;
                }
                """
        row_count = widgets.tableWidget_4.rowCount()
        self.export_buttons = {}
        self.export_buttons2 = {}
        self.export_buttons3 = {}
        # for row in range(1, row_count):  # 从第二行开始，即索引1
        #
        #     button = QPushButton("导出为PDF")
        #     button.clicked.connect(lambda checked, r=row: export_to_pdf(r))
        #     button.setStyleSheet(button_style1)
        #     # 可以连接按钮点击事件，比如 button.clicked.connect(lambda: do_something(row))
        #
        #     button_widget = QWidget()
        #     layout = QHBoxLayout(button_widget)
        #     layout.addWidget(button)
        #     layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中
        #     layout.setContentsMargins(0, 0, 0, 0)  # 去除边距
        #     self.export_buttons[row] = button
        #     # 设置到表格单元格中
        #     widgets.tableWidget_4.setCellWidget(row, 2, button_widget)
        #
        #     #widgets.tableWidget_4.setCellWidget(row, 2, button)

        font = QFont()
        font.setPointSize(14)  # 设置字号为14
        font.setBold(True)  # 设置为粗体

        # 应用于 QLabel
        widgets.labelBoxBlenderInstalation_6.setFont(font)
        widgets.labelBoxBlenderInstalation_7.setFont(font)

        def resource_path(relative_path):
            """获取打包后资源的绝对路径，兼容开发环境和PyInstaller打包环境"""
            try:
                # PyInstaller打包后会把资源放在临时目录sys._MEIPASS下
                base_path = sys._MEIPASS
            except Exception:
                # 开发环境直接用当前目录
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        def update_pdflog(self):
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="yupeihao05ab",
                database="locallog",
                charset="utf8mb4"
            )

            try:
                cursor = conn.cursor()
                cursor.execute("SELECT time, username FROM localpdflog GROUP BY time, username")
                results = cursor.fetchall()

                self.ui.tableWidget_6.setRowCount(len(results) + 1)  # 第一行为表头
                self.ui.tableWidget_6.setColumnCount(4)
                headers = ["时间", "操作者账户", "导出账号", "删除日志"]
                self.ui.tableWidget_6.setHorizontalHeaderLabels(headers)

                column_widths = [140, 70, 100, 100]
                for i, w in enumerate(column_widths):
                    self.ui.tableWidget_6.setColumnWidth(i, w)

                for i, row_data in enumerate(results):
                    row_index = i + 1

                    # 插入时间、用户名
                    for col_index, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.ui.tableWidget_4.setItem(row_index, col_index, item)

                    # 添加日志按钮
                    button = QPushButton("查看分析报告")
                    time_value = row_data[0]  # 当前行的时间值
                    print(time_value)
                    button.clicked.connect(lambda checked, t=time_value: export_to_pdf(t))
                    button.setStyleSheet(button_style1)
                    # 可以连接按钮点击事件，比如 button.clicked.connect(lambda: do_something(row))

                    button_widget = QWidget()
                    layout = QHBoxLayout(button_widget)
                    layout.addWidget(button)
                    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中
                    layout.setContentsMargins(0, 0, 0, 0)  # 去除边距
                    self.export_buttons[row_index] = button
                    # 设置到表格单元格中
                    widgets.tableWidget_4.setCellWidget(row_index, 2, button_widget)

            finally:
                conn.close()

        update_pdflog(self)
        self.update_pdflog = update_pdflog(self)
        row_count = self.ui.tableWidget_6.rowCount()
        for i in range(row_count + 2):
            self.ui.tableWidget_6.setRowHeight(i, 40)
        self.ui.tableWidget_6.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        def open_edit_dialog(user_row):
            # user_row 是一个包含 username, phone, email, company, id, name 的元组
            dialog = QDialog()
            dialog.setWindowTitle("修改个人信息")

            layout = QVBoxLayout(dialog)
            labels = ["账号", "姓名", "邮箱", "单位名称", "工号", "联系电话"]
            edits = []

            for i, label_text in enumerate(labels):
                layout.addWidget(QLabel(label_text))
                edit = QLineEdit()
                edit.setText(user_row[i])
                layout.addWidget(edit)
                edits.append(edit)

            btn_save = QPushButton("保存")
            layout.addWidget(btn_save)

            def save_changes():
                new_values = [e.text() for e in edits]
                update_user_info_by_username(
                    original_username=user_row[0],
                    username=new_values[0],
                    phone=new_values[5],
                    email=new_values[2],
                    company=new_values[3],
                    id=new_values[4],
                    name=new_values[1]
                )
                dialog.accept()
                load_user_table(self)  # 刷新表格

            btn_save.clicked.connect(save_changes)
            dialog.exec()

        def update_user_info_by_username(original_username, username, phone, email, company, id, name):
            conn = pymysql.connect(
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )

            try:
                cursor = conn.cursor()
                update_query = """
                    UPDATE register SET
                        username = %s,
                        phone = %s,
                        email = %s,
                        company = %s,
                        id = %s,
                        name = %s
                    WHERE username = %s
                """
                cursor.execute(update_query, (username, phone, email, company, id, name, original_username))
                conn.commit()

            finally:
                conn.close()

        def delete_user_by_username(username):
            try:
                conn = pymysql.connect(  # 填写你的数据库连接信息
                    host="sql.wsfdb.cn",
                    port=3306,
                    user="8393455register",
                    password="yupeihao05ab",
                    database="8393455register",
                    charset="utf8mb4"
                )
                cursor = conn.cursor()
                sql = "DELETE FROM register WHERE username = %s"
                cursor.execute(sql, (username,))
                conn.commit()
                return True
            except Exception as e:
                print("删除失败：", e)
                return False
            finally:
                cursor.close()
                conn.close()

        def confirm_delete(username):
            reply = QMessageBox.question(
                self,
                "确认删除",
                f"确定要删除用户 '{username}' 吗？此操作不可恢复！",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                success = delete_user_by_username(username)  # 你需要写这个函数
                if success:
                    QMessageBox.information(self, "删除成功", f"用户 '{username}' 已被删除。")
                    self.load_user_table(self)  # 重新加载刷新
                else:
                    QMessageBox.warning(self, "删除失败", "删除操作失败，请检查数据库。")

        def load_user_table(self):
            conn = pymysql.connect(
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )

            try:
                cursor = conn.cursor()
                cursor.execute("SELECT username, name, email, company, id, phone FROM register")
                results = cursor.fetchall()

                # 设置表格列数、标题、宽度
                self.ui.tableWidget_5.setRowCount(len(results) + 1)
                self.ui.tableWidget_5.setColumnCount(8)
                headers = ["username", "name", "email", "company", "id", "phone", "修改", "删除"]
                self.ui.tableWidget_5.setHorizontalHeaderLabels(headers)

                column_widths = [60, 80, 150, 90, 50, 100, 80, 80]
                for i, w in enumerate(column_widths):
                    self.ui.tableWidget_5.setColumnWidth(i, w)
                self.export_buttons2 = {}
                self.export_buttons3 = {}
                for i, row_data in enumerate(results):
                    row_index = i + 1
                    for col_index, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.ui.tableWidget_5.setItem(row_index, col_index, item)

                    btn_edit = QPushButton("修改")
                    self.export_buttons3[i] = btn_edit
                    btn_edit.setObjectName("editButton")
                    btn_edit.setStyleSheet("color: black;")
                    btn_edit.setFixedSize(60, 30)
                    btn_edit.clicked.connect(lambda _, r=row_data: open_edit_dialog(r))

                    edit_widget = QWidget()
                    edit_layout = QHBoxLayout(edit_widget)
                    edit_layout.addWidget(btn_edit)
                    edit_layout.setContentsMargins(0, 0, 0, 0)
                    edit_layout.setAlignment(Qt.AlignCenter)  # 使按钮居中
                    edit_widget.setFixedSize(80, 40)
                    self.ui.tableWidget_5.setCellWidget(row_index, 6, edit_widget)

                    # --- 添加“删除”按钮 ---
                    btn_del = QPushButton("删除")
                    self.export_buttons2[i] = btn_del
                    btn_del.setObjectName("deleteButton")
                    btn_del.setStyleSheet("color: red;")
                    btn_del.clicked.connect(lambda _, uname=row_data[0]: confirm_delete(uname))

                    del_widget = QWidget()
                    del_layout = QHBoxLayout(del_widget)
                    del_layout.addWidget(btn_del)
                    del_layout.setContentsMargins(0, 0, 0, 0)
                    del_layout.setAlignment(Qt.AlignCenter)
                    del_widget.setFixedSize(80, 40)
                    btn_del.setFixedSize(60, 30)
                    self.ui.tableWidget_5.setCellWidget(row_index, 7, del_widget)


            finally:
                conn.close()

        self.load_user_table = load_user_table
        res = self.get_user_info(username)
        if res:
            self.ui.lineEdit_17.setText(res.get("phone", ""))
            self.ui.lineEdit_18.setText(res.get("name", ""))
            self.ui.lineEdit_19.setText(res.get("email", ""))
            self.ui.lineEdit_20.setText(res.get("company", ""))
            self.ui.lineEdit_21.setText(res.get("id", ""))
        else:
            QMessageBox.warning(self, "用户不存在", f"未找到用户 {username} 的注册信息。")

        self.load_user_table(self)
        row_count = self.ui.tableWidget_5.rowCount()
        for i in range(row_count + 1):
            self.ui.tableWidget_5.setRowHeight(i, 40)
        self.ui.tableWidget_5.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.update_cloudlog()

        self.logbotton = {}
        self.deletebutton = {}
        self.predictModelVersion = 0
        self.localpredictModelVersion = 0
        self.localparameterversion = 0
        self.parameterversion = 0
        self.trans_a = 0
        self.predict_a = 0
        self.localparameterversion = 0
        self.localtrans_a = 0
        self.localpredict_a = 0

        self.load_log()
        row_count = self.ui.tableWidget_6.rowCount()
        for i in range(row_count + 2):
            self.ui.tableWidget_6.setRowHeight(i, 40)
        self.ui.tableWidget_6.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        def export_to_pdf(requiretime):
            if isinstance(requiretime, datetime):
                requiretime = requiretime.strftime("%Y-%m-%d_%H-%M-%S")  # 先格式化，再做文件名替换
                # 若已经是字符串，确保替换非法文件名字符
            time_str = requiretime.replace(":", "-").replace(" ", "_")

            filename = f"{time_str}.pdf"

            base_dir = os.path.abspath(os.path.dirname(__file__))  # 当前脚本所在目录
            pdf_path = os.path.join(base_dir, "final", "result", filename)

            print(f"导出时间为 {time_str} 的数据为 PDF")

            if os.path.exists(pdf_path):
                try:
                    os.startfile(pdf_path)
                except AttributeError:
                    subprocess.call(["open" if sys.platform == "darwin" else "xdg-open", pdf_path])
            else:
                print(f"文件未找到: {pdf_path}")

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        def resource_path(relative_path):
            """获取打包后资源的绝对路径，兼容开发环境和PyInstaller打包环境"""
            try:
                # PyInstaller打包后会把资源放在临时目录sys._MEIPASS下
                base_path = sys._MEIPASS
            except Exception:
                # 开发环境直接用当前目录
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        self.useCustomTheme = useCustomTheme
        themeFile = resource_path("themes\py_dracula_light.qss")
        self.themeFile = themeFile

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        self.updateAll()

    def check_version(self, current_version):
        url = "https://b1ankalpha.github.io/Eco/index.html"

        try:
            # 请求获取JSON数据
            response = requests.get(url)
            response.raise_for_status()  # 如果请求失败则抛出异常
            data = response.json()

            # 获取版本号和下载链接
            latest_version = data.get("version")
            download_url = data.get("download_url")

            if latest_version > current_version:
                # 版本更新了，弹窗提示并打开下载链接
                if download_url:
                    self.open_url(download_url)
                else:
                    messagebox.showinfo("检查更新", "有新的更新、为您跳转到下载界面.")
            else:
                # 当前已经是最新版本
                messagebox.showinfo("检查更新", "您已是最新版本.")
        except requests.RequestException as e:
            messagebox.showerror("错误", f"下载链接访问失败: {e}")

    def updateAll(self):
        # 获取当前版本信息:
        widgets.label_3.setText(current_version)
        url = "https://b1ankalpha.github.io/Eco/index.html"

        try:
            # 请求获取JSON数据
            response = requests.get(url)
            response.raise_for_status()  # 如果请求失败则抛出异常
            data = response.json()

            # 获取版本号和下载链接
            latest_version = data.get("version")
            download_url = data.get("download_url")
            widgets.label_4.setText(latest_version)
        except requests.RequestException as e:
            widgets.label_4.setText(str(e))

        try:
            conn = pymysql.connect(  # 填写你的数据库连接信息
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )
            cursor = conn.cursor()
            sql = "SELECT predictModelVersion,predictModelLink FROM model"
            cursor.execute(sql, ())
            results = cursor.fetchall()
            print(results[0])
            conn.commit()
        except Exception as e:
            print("删除失败：", e)
        finally:
            cursor.close()
            conn.close()

        self.predictModelVersion = results[0][0]
        self.predictModelLink = results[0][1]
        self.transModelLink = self.predictModelLink
        print(results[0][1])
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="yupeihao05ab",
                database="locallog",
                charset="utf8mb4"
            )
            cursor = conn.cursor()
            sql = "SELECT predictModelVersion FROM localmodel"
            cursor.execute(sql, ())
            results = cursor.fetchall()
            print(results[0])
            conn.commit()
        except Exception as e:
            print("删除失败：", e)
        finally:
            cursor.close()
            conn.close()

        self.localpredictModelVersion = results[0][0]

        self.ui.label_6.setText(self.localpredictModelVersion)
        self.ui.label_5.setText(self.predictModelVersion)

        try:
            conn = pymysql.connect(
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )
            cursor = conn.cursor()
            sql = "SELECT version,a,b,c,d,e,f,g,h,i FROM parameter"
            cursor.execute(sql, ())
            results = cursor.fetchall()
            print(results[0])
            conn.commit()
        except Exception as e:
            print("删除失败：", e)
        finally:
            cursor.close()
            conn.close()
        self.parameterversion = results[0][0]
        self.a = results[0][1]
        self.b = results[0][2]
        self.c = results[0][3]
        self.d = results[0][4]
        self.e = results[0][5]
        self.f = results[0][6]
        self.g = results[0][7]
        self.h = results[0][8]
        self.i = results[0][9]
        self.ui.label_7.setText(self.parameterversion)

        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="yupeihao05ab",
                database="locallog",
                charset="utf8mb4"
            )
            cursor = conn.cursor()
            sql = "SELECT version,a,b,c,d,e,f,g,h,i FROM localparameter"
            cursor.execute(sql, ())
            results = cursor.fetchall()
            print(results[0])
            conn.commit()
        except Exception as e:
            print("删除失败：", e)
        finally:
            cursor.close()
            conn.close()
        self.localparameterversion = results[0][0]
        self.locala = results[0][1]
        self.localb = results[0][2]
        self.localc = results[0][3]
        self.locald = results[0][4]
        self.locale = results[0][5]
        self.localf = results[0][6]
        self.localg = results[0][7]
        self.localh = results[0][8]
        self.locali = results[0][9]
        self.ui.label_8.setText(self.localparameterversion)
        self.ui.lineEdit_9.setText(self.locala)
        self.ui.lineEdit_10.setText(self.localb)
        self.ui.lineEdit_11.setText(self.localc)
        self.ui.lineEdit_12.setText(self.locald)
        self.ui.lineEdit_27.setText(self.locale)
        self.ui.lineEdit_13.setText(self.localf)
        self.ui.lineEdit_14.setText(self.localg)
        self.ui.lineEdit_15.setText(self.localh)
        self.ui.lineEdit_16.setText(self.locali)

    def update_cloudlog(self):
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()

            # 清除 tableWidget_3 除第一行外的内容
            row_count = self.ui.tableWidget_2.rowCount()
            for i in range(row_count - 1, 0, -1):
                self.ui.tableWidget_2.removeRow(i)

            # 查询该时间点的所有 account
            query = "SELECT account FROM cloudaccount  GROUP BY account"
            cursor.execute(query, ())
            accounts = cursor.fetchall()

            # 填入 tableWidget_3，从第 2 行起写入
            for i, (account,) in enumerate(accounts, start=1):
                self.ui.tableWidget_2.insertRow(i)
                item = QTableWidgetItem(account)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_2.setItem(i, 0, item)  # 只填一列

        finally:
            conn.close()

    def delete_log(self, requiretime):
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="yupeihao05ab",
                database="locallog",
                charset="utf8mb4"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM locallog WHERE time = %s"
            cursor.execute(sql, (requiretime,))
            conn.commit()
            return True
        except Exception as e:
            print("删除失败：", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def confirm_delete_log(self, requiretime):
        reply = QMessageBox.question(
            self,
            "确认删除",
            f"确定要删除时间为 '{requiretime}' 的记录吗？此操作不可恢复！",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            success = self.delete_log(requiretime)  # 你需要写这个函数
            if success:
                QMessageBox.information(self, "删除成功", f"时间为 '{requiretime}' 的记录已被删除。")
                self.load_log()  # 重新加载刷新
            else:
                QMessageBox.warning(self, "删除失败", "删除操作失败，请检查数据库。")

    def handle_add_log(self, time_str):
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="yupeihao05ab",
            database="locallog",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()

            # 清除 tableWidget_3 除第一行外的内容
            row_count = self.ui.tableWidget_3.rowCount()
            for i in range(row_count - 1, 0, -1):
                self.ui.tableWidget_3.removeRow(i)

            # 查询该时间点的所有 account
            query = "SELECT distinct zhdh FROM locallog WHERE time = %s"
            cursor.execute(query, (time_str,))
            accounts = cursor.fetchall()

            # 填入 tableWidget_3，从第 2 行起写入
            for i, (account,) in enumerate(accounts, start=1):
                self.ui.tableWidget_3.insertRow(i)
                item = QTableWidgetItem(account)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_3.setItem(i, 0, item)  # 只填一列

        finally:
            conn.close()

    def load_log(self):
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="yupeihao05ab",
            database="locallog",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT time, username FROM locallog GROUP BY time, username")
            results = cursor.fetchall()

            self.ui.tableWidget_6.setRowCount(len(results) + 1)  # 第一行为表头
            self.ui.tableWidget_6.setColumnCount(4)
            headers = ["时间", "操作者账户", "导出账号", "删除日志"]
            self.ui.tableWidget_6.setHorizontalHeaderLabels(headers)

            column_widths = [140, 70, 100, 100]
            for i, w in enumerate(column_widths):
                self.ui.tableWidget_6.setColumnWidth(i, w)

            for i, row_data in enumerate(results):
                row_index = i + 1

                # 插入时间、用户名
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.tableWidget_6.setItem(row_index, col_index, item)

                # 添加日志按钮
                btn_add_log = QPushButton("导出账号")
                btn_add_log.setObjectName("addLogButton")
                btn_add_log.setStyleSheet("color: green;")
                btn_add_log.setFixedSize(80, 30)
                btn_add_log.clicked.connect(partial(self.handle_add_log, row_data[0]))  # 只传 time

                add_widget = QWidget()
                add_layout = QHBoxLayout(add_widget)
                add_layout.addWidget(btn_add_log)
                add_layout.setContentsMargins(0, 0, 0, 0)
                add_layout.setAlignment(Qt.AlignCenter)
                add_widget.setFixedSize(100, 40)

                self.ui.tableWidget_6.setCellWidget(row_index, 2, add_widget)

                # 删除日志按钮
                btn_delete_log = QPushButton("删除日志")
                btn_delete_log.setObjectName("deleteLogButton")
                btn_delete_log.setStyleSheet("color: red;")
                btn_delete_log.setFixedSize(80, 30)
                btn_delete_log.clicked.connect(partial(self.confirm_delete_log, row_data[0]))  # 只传 time

                del_widget = QWidget()
                del_layout = QHBoxLayout(del_widget)
                del_layout.addWidget(btn_delete_log)
                del_layout.setContentsMargins(0, 0, 0, 0)
                del_layout.setAlignment(Qt.AlignCenter)
                del_widget.setFixedSize(100, 40)

                self.ui.tableWidget_6.setCellWidget(row_index, 3, del_widget)

        finally:
            conn.close()

    def rename_single_file_in_dir(self, dir_path, new_name):
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        if len(files) == 1:
            old_path = os.path.join(dir_path, files[0])
            new_path = os.path.join(dir_path, new_name)
            os.rename(old_path, new_path)
            return new_path
        else:
            raise FileNotFoundError(f"{dir_path} 目录下文件数不是1，无法自动改名")

    def decrypt_temp_model(self, enc_path, temp_dir, cipher):
        # 读取加密数据
        with open(enc_path, 'rb') as f:
            encrypted_data = f.read()

        # 解密
        decrypted = cipher.decrypt(encrypted_data)

        # 从加密文件中提取文件名，构造解密后的路径
        filename = os.path.basename(enc_path)  # e.g. "model.enc"
        decrypted_filename = os.path.splitext(filename)[0]  # e.g. "model"
        output_path = os.path.join(temp_dir, decrypted_filename)  # e.g. "final/model/model"

        # 写入解密后的数据
        with open(output_path, 'wb') as f:
            f.write(decrypted)

    def cleanup(self, path):
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception as e:
                        print(f"删除文件失败: {file}，原因: {e}")
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir))
                    except Exception as e:
                        print(f"删除子目录失败: {dir}，原因: {e}")
        elif os.path.isfile(path):
            try:
                os.remove(path)
            except Exception as e:
                print(f"删除文件失败: {path}，原因: {e}")
        else:
            print(f"路径不存在或类型未知：{path}")

    def encrypt_file(self, input_path, output_path, cipher):
        with open(input_path, 'rb') as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(output_path, 'wb') as f:
            f.write(encrypted)

    def download_zip(self, url, output_path):
        if not url or not url.startswith("http"):
            raise ValueError(f"无效下载链接：{url}")

        response = requests.get(url)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"下载完成：{output_path}")

    def unzip_with_password(self, zip_path, extract_to, password):
        with pyzipper.AESZipFile(zip_path) as zf:
            zf.pwd = password.encode()
            for zi in zf.infolist():
                extracted_path = os.path.join(extract_to, zi.filename)
                # 如果文件已存在，先去掉只读属性再删除
                if os.path.exists(extracted_path):
                    os.chmod(extracted_path, stat.S_IWRITE)
                    os.remove(extracted_path)
            zf.extractall(path=extract_to)

    def set_readonly(self, path):
        for root, dirs, files in os.walk(path):
            for name in files:
                full_path = os.path.join(root, name)
                os.chmod(full_path, 0o444)

    def set_hidden(self, path):
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)
        print(f"{path} 已设置为隐藏文件夹")

    def delete_cloudlog(self, account):
        try:
            conn = pymysql.connect(  # 填写你的数据库连接信息
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM cloudlog WHERE zhdh = %s"
            cursor.execute(sql, (account,))
            conn.commit()
            return True
        except Exception as e:
            print("删除失败：", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def delete_cloudaccount(self, account):
        try:
            conn = pymysql.connect(  # 填写你的数据库连接信息
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM cloudaccount WHERE account = %s"
            cursor.execute(sql, (account,))
            conn.commit()
            return True
        except Exception as e:
            print("删除失败：", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def update_cloudlog(self):
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()

            # 清除 tableWidget_3 除第一行外的内容
            row_count = self.ui.tableWidget_2.rowCount()
            for i in range(row_count - 1, 0, -1):
                self.ui.tableWidget_2.removeRow(i)

            # 查询该时间点的所有 account
            query = "SELECT account FROM cloudaccount GROUP BY account"
            cursor.execute(query, ())
            accounts = cursor.fetchall()

            # 填入 tableWidget_3，从第 2 行起写入
            for i, (account,) in enumerate(accounts, start=1):
                self.ui.tableWidget_2.insertRow(i)
                item = QTableWidgetItem(account)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget_2.setItem(i, 0, item)  # 只填一列

        finally:
            conn.close()

    def upload_important(self, account):
        if not account:
            print("账号为空")
            return

        try:
            # 连接本地数据库
            local_conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="yupeihao05ab",
                database="locallog",
                charset="utf8mb4"
            )
            local_cursor = local_conn.cursor()

            # 查询本地数据
            select_sql = "SELECT * FROM locallog WHERE zhdh = %s"
            local_cursor.execute(select_sql, (account,))
            records = local_cursor.fetchall()

            if not records:
                print("本地未找到该账号的记录")
                return

            # 获取字段数量，用于构造 INSERT 语句
            column_count = len(local_cursor.description)
            placeholders = ','.join(['%s'] * column_count)

            # 连接云端数据库
            cloud_conn = pymysql.connect(
                host="sql.wsfdb.cn",
                port=3306,
                user="8393455register",
                password="yupeihao05ab",
                database="8393455register",
                charset="utf8mb4"
            )
            cloud_cursor = cloud_conn.cursor()

            insert_sql = f"INSERT INTO cloudlog VALUES ({placeholders})"

            # 执行插入操作
            cloud_cursor.executemany(insert_sql, records)
            cloud_conn.commit()

            print(f"成功上传 {len(records)} 条记录到云端 cloudlog")

        except Exception as e:
            print("上传出错:", e)

        finally:
            try:
                local_cursor.close()
                local_conn.close()
            except:
                pass
            try:
                cloud_cursor.close()
                cloud_conn.close()
            except:
                pass

    def logout(self):
        self.close()  # 关闭主窗口
        self.login_window.show()
        self.login_window.reset_login_fields()

    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)

    def export_to_pdf(self, requiretime):
        if isinstance(requiretime, datetime):
            requiretime = requiretime.strftime("%Y-%m-%d_%H-%M-%S")  # 先格式化，再做文件名替换
            # 若已经是字符串，确保替换非法文件名字符
        time_str = requiretime.replace(":", "-").replace(" ", "_")

        filename = f"{time_str}.pdf"
        pdf_path = os.path.join("./final/result/", filename)

        print(f"导出时间为 {time_str} 的数据为 PDF")

        if os.path.exists(pdf_path):
            try:
                os.startfile(pdf_path)
            except AttributeError:
                subprocess.call(["open" if sys.platform == "darwin" else "xdg-open", pdf_path])
        else:
            print(f"文件未找到: {pdf_path}")

    def update_pdflog_selecttime(self):
        input_time = self.ui.plainTextEdit_14.toPlainText().strip()

        # 构造模糊查询时间
        if re.fullmatch(r"\d{4}", input_time):  # 年
            like_time = f"{input_time}%"  # e.g., 2025%
        elif re.fullmatch(r"\d{4}-\d{2}", input_time):  # 年-月
            like_time = f"{input_time}%"  # e.g., 2025-05%
        elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", input_time):  # 年-月-日
            like_time = f"{input_time}%"  # 一定要加 % 才能匹配这一天所有时间
        else:
            self.ui.plainTextEdit_14.setPlainText("时间格式不合法，应为 YYYY 或 YYYY-MM 或 YYYY-MM-DD")
            return

        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="yupeihao05ab",
            database="locallog",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            sql = "SELECT time, username FROM localpdflog WHERE time LIKE %s GROUP BY time, username"
            cursor.execute(sql, (like_time,))
            results = cursor.fetchall()

            if not results:
                self.ui.plainTextEdit_14.clear()
                self.ui.plainTextEdit_14.setPlaceholderText("暂无结果")
                return
            else:
                self.ui.plainTextEdit_14.setPlaceholderText("查询成功")

            self.ui.tableWidget_4.setRowCount(len(results) + 1)
            self.ui.tableWidget_4.setColumnCount(3)
            headers = ["时间", "操作者账户", "导出账号", "删除日志"]
            self.ui.tableWidget_4.setHorizontalHeaderLabels(headers)

            for i, row_data in enumerate(results):
                row_index = i + 1
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.tableWidget_4.setItem(row_index, col_index, item)

                button = QPushButton("导出为PDF")
                time_value = row_data[0]
                button.clicked.connect(lambda checked, t=time_value: self.export_to_pdf(t))
                button.setStyleSheet(button_style1)

                button_widget = QWidget()
                layout = QHBoxLayout(button_widget)
                layout.addWidget(button)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                self.export_buttons[row_index] = button
                self.ui.tableWidget_4.setCellWidget(row_index, 2, button_widget)

        finally:
            conn.close()

    def update_pdflog_selectusername(self):
        username = self.ui.plainTextEdit_14.toPlainText()
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="yupeihao05ab",
            database="locallog",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            sql = "SELECT time, username FROM localpdflog WHERE username = %s GROUP BY time, username"
            cursor.execute(sql, (username,))
            results = cursor.fetchall()
            if not results:
                self.ui.plainTextEdit_14.clear()
                self.ui.plainTextEdit_14.setPlaceholderText("暂无结果")
                return
            else:
                self.ui.plainTextEdit_14.setPlaceholderText("查询成功")
            self.ui.tableWidget_4.setRowCount(len(results) + 1)  # 第一行为表头
            self.ui.tableWidget_4.setColumnCount(3)
            headers = ["时间", "操作者账户", "导出账号", "删除日志"]
            self.ui.tableWidget_4.setHorizontalHeaderLabels(headers)

            for i, row_data in enumerate(results):
                row_index = i + 1

                # 插入时间、用户名
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.tableWidget_4.setItem(row_index, col_index, item)

                # 添加日志按钮
                button = QPushButton("导出为PDF")
                time_value = row_data[0]  # 当前行的时间值
                button.clicked.connect(lambda checked, t=time_value: self.export_to_pdf(t))
                button.setStyleSheet(button_style1)

                button_widget = QWidget()
                layout = QHBoxLayout(button_widget)
                layout.addWidget(button)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                self.export_buttons[row_index] = button
                self.ui.tableWidget_4.setCellWidget(row_index, 2, button_widget)

        finally:
            conn.close()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def upload_account(self, account_value):
        """
        将指定的 account 上传到 cloudaccount 表中
        """
        cloud_conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )
        try:
            with cloud_conn.cursor() as cursor:
                sql = "INSERT IGNORE INTO cloudaccount (account) VALUES (%s)"
                cursor.execute(sql, (account_value,))
            cloud_conn.commit()
            print(f"已成功插入账号：{account_value}")
        except Exception as e:
            print("插入失败，错误信息：", e)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_information":
            widgets.stackedWidget.setCurrentWidget(widgets.information)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.load_log()
            self.update_cloudlog()

        if btnName == "btn_para":
            widgets.stackedWidget.setCurrentWidget(widgets.page_2)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_exit":
            self.logout()

        if btnName == "pushButton_4":
            files, _ = QFileDialog.getOpenFileNames(
                self,
                "选择图片文件",
                "",
                "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif)"
            )
            if files:
                # 输出 1：文件名拼接字符串
                filenames = [os.path.basename(f) for f in files]
                result_str = "、".join(filenames)
                if self.str:
                    self.str += "、" + result_str
                else:
                    self.str = result_str
                self.uploadfile = self.uploadfile + files
                widgets.lineEdit_2.setText(self.str)
                # 输出 2：文件路径列表
                print("图片文件名字符串：", self.str)
                print("总图片路径列表：", self.uploadfile)
                print(username)

        if btnName == "pushButton_42":
            account = widgets.plainTextEdit_13.toPlainText()
            print(account)
            win1 = self.delete_cloudlog(account)
            win2 = self.delete_cloudaccount(account)
            if win1 and win2:
                print("删除成功")
            self.update_cloudlog()

        if btnName == "pushButton_51":
            from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout
            from PySide6.QtGui import QPixmap
            from PySide6.QtCore import Qt
            from PIL.ImageQt import ImageQt
            import pyotp
            import qrcode

            dialog = QDialog()
            dialog.setWindowTitle("添加新用户")

            layout = QVBoxLayout(dialog)
            labels = ["账号", "姓名", "密码", "邮箱", "单位名称", "工号", "联系电话"]
            edits = []

            for label in labels:
                layout.addWidget(QLabel(label))
                edit = QLineEdit()
                layout.addWidget(edit)
                edits.append(edit)

            btn_save = QPushButton("保存")
            layout.addWidget(btn_save)

            def generate_base32_key():
                # 生成20字节的随机密钥并编码为 Base32（TOTP 标准）
                return base64.b32encode(secrets.token_bytes(20)).decode("utf-8")

            def insert_user_info(username, phone, password, email, company, id_, name):
                conn = pymysql.connect(
                    host="sql.wsfdb.cn",
                    port=3306,
                    user="8393455register",
                    password="yupeihao05ab",
                    database="8393455register",
                    charset="utf8mb4"
                )
                try:
                    with conn.cursor() as cursor:
                        base32_key = generate_base32_key()
                        sql = """
                            INSERT INTO register (username, phone, password, email, company, id, name, base32,isadmin)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,0)
                        """
                        cursor.execute(sql, (username, phone, password, email, company, id_, name, base32_key))
                    conn.commit()
                    return base32_key  # ✅ 插入成功后返回密钥
                finally:
                    conn.close()

            def show_qr_code(user, base32_key):
                # 生成二维码内容
                totp_uri = pyotp.totp.TOTP(base32_key).provisioning_uri(name=user, issuer_name="FraudShield")
                qr_img = qrcode.make(totp_uri)

                # 保存二维码为 PNG 到内存中
                buffer = BytesIO()
                qr_img.save(buffer, format="PNG")
                img_data = buffer.getvalue()

                # 转换为 QImage → QPixmap
                qimage = QImage.fromData(img_data)
                pixmap = QPixmap.fromImage(qimage)
                pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

                # 创建对话框
                qr_dialog = QDialog()
                qr_dialog.setWindowTitle("绑定二次验证密钥")
                layout = QVBoxLayout(qr_dialog)

                label = QLabel(f"✅ 用户【{user}】已成功添加！\n请使用验证器扫码以下二维码绑定账号：")
                layout.addWidget(label)

                qr_label = QLabel()
                qr_label.setPixmap(pixmap)
                qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(qr_label)

                qr_dialog.exec()

            def save_new_user():
                values = [e.text().strip() for e in edits]
                if any(v == "" for v in values):
                    QMessageBox.warning(dialog, "输入错误", "所有字段不能为空")
                    return

                username, name, password, email, company, id_, phone = values

                try:
                    base32_key = insert_user_info(username, phone, password, email, company, id_, name)
                    self.load_user_table(self)

                    print(username, base32_key)
                    try:
                        show_qr_code(username, base32_key)
                    except Exception as e2:
                        QMessageBox.critical(dialog, "CODE失败", f"错误信息：{e2}")
                        print(e2)
                except Exception as e:
                    print("a")
                    # QMessageBox.critical(dialog, "添加失败", f"错误信息：{e}")

            btn_save.clicked.connect(save_new_user)
            dialog.exec()

        if btnName == "pushButton_39":
            index = self.ui.comboBox_2.currentIndex()
            if index == 0:
                print(index)
                account = widgets.plainTextEdit_13.toPlainText()
                print(account)
                if account is not None and account != '':
                    win = self.upload_important(account)
                if account is not None and account != '':
                    win2 = self.upload_account(account)
                if win and win2:
                    print("上传成功")
                self.update_cloudlog()

            else:
                print(index)
                account = widgets.plainTextEdit_13.toPlainText()
                if account is not None and account != '':
                    self.upload_account(account)
                cloud_conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="yupeihao05ab",
                    database="locallog",
                    charset="utf8mb4"
                )

                try:
                    with cloud_conn.cursor() as cursor:
                        # 查询 cloudlog 表中 account 等于变量 account 的所有 counterparty_account
                        sql = "SELECT dfzh FROM locallog WHERE zhdh = %s"
                        cursor.execute(sql, (account,))  # 参数化防止SQL注入

                        results = cursor.fetchall()
                        counterparty_list = list(set(row[0] for row in results))

                        print("匹配的 counterparty_account 列表：", counterparty_list)

                finally:
                    cloud_conn.close()
                for acc in counterparty_list:
                    if acc is not None and acc != '':
                        self.upload_account(acc)
                self.update_cloudlog()

        if btnName == "pushButton_5":

            files, _ = QFileDialog.getOpenFileNames(
                self,
                "选择任意文件",
                "",
                "所有文件 (*.*)"
            )

            if files:  # files 是文件路径组成的列表
                filenames = [os.path.basename(f) for f in files]
                result_str = "、".join(filenames)

                if self.str:
                    self.str += "、" + result_str
                else:
                    self.str = result_str

                self.uploadfile += files  # 或 self.uploadfile.extend(files)

                widgets.lineEdit_2.setText(self.str)
                print("总文件名字符串：", self.str)
                print("总路径列表：", self.uploadfile)

        if btnName == "pushButton_3":
            widgets.plainTextEdit_2.setPlaceholderText("待分析数据已上传成功")

            print("uploadtext", self.uploadtext)

            id_value = widgets.plainTextEdit_2.toPlainText()
            id = self.id
            id_filename = str(id) + ".txt"  # 文件名固定
            if self.str:
                self.str += "、" + id_filename
            else:
                self.str = id_filename
            widgets.lineEdit_2.setText(self.str)

            output_dir = "./final/"
            output_path = os.path.abspath(os.path.join(output_dir, id_filename))  # 转为绝对路径
            self.uploadfile += [output_path]  # 添加到上传文件列表
            print("总路径列表：", self.uploadfile)
            # 确保目录存在
            os.makedirs(output_dir, exist_ok=True)

            # 写入文件，覆盖写入模式
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(str(id_value))
            widgets.plainTextEdit_2.setPlainText("")

        if btnName == "btn_save":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            print("Save BTN clicked!")
            self.update_pdflog()
            # QMessageBox.information(self, "Save", "该功能未实现!")

        def resource_path(relative_path):
            """获取打包后资源的绝对路径，兼容开发环境和PyInstaller打包环境"""
            try:
                # PyInstaller打包后会把资源放在临时目录sys._MEIPASS下
                base_path = sys._MEIPASS
            except Exception:
                # 开发环境直接用当前目录
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        if btnName == "btn_themechange":
            print("Save BTN clicked!")
            if self.useCustomTheme:
                # LOAD AND APPLY STYLE
                self.themeFile = resource_path("themes\py_dracula_dark.qss")
                UIFunctions.theme(self, self.themeFile, True)

                # SET HACKS
                AppFunctions.setThemeHack(self, target=2)
                self.useCustomTheme = False
                for button in self.export_buttons.values():
                    button.setStyleSheet(button_style2)

                for button in self.export_buttons2.values():
                    button.setStyleSheet(button_stylered)

                for button in self.export_buttons3.values():
                    button.setStyleSheet(button_stylewhite)

                for button in self.logbotton.values():
                    button.setStyleSheet(button_stylewhite)
            else:
                # LOAD AND APPLY STYLE

                self.themeFile = resource_path("themes\py_dracula_light.qss")
                UIFunctions.theme(self, self.themeFile, True)

                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = True
                for button in self.export_buttons.values():
                    button.setStyleSheet(button_styleblack)

                for button in self.export_buttons2.values():
                    button.setStyleSheet(button_stylered)

                for button in self.export_buttons3.values():
                    button.setStyleSheet(button_styleblack)

                for button in self.logbotton.values():
                    button.setStyleSheet(button_styleblack)

            row_count = self.ui.tableWidget_5.rowCount()
            for i in range(row_count + 1):
                self.ui.tableWidget_5.setRowHeight(i, 40)
            header = self.ui.tableWidget_5.verticalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        if btnName == "btn_tukit":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_upload":
            widgets.stackedWidget.setCurrentWidget(widgets.upload)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "pushButton_40":
            self.update_pdflog_selecttime()
            print(111)

        if btnName == "pushButton_41":
            self.update_pdflog_selectusername()
            print(222)

        if btnName == "pushButton_50":
            inputsecret = self.ui.lineEdit_22.text()
            phone = self.ui.lineEdit_17.text()
            name = self.ui.lineEdit_18.text()
            email = self.ui.lineEdit_19.text()
            company = self.ui.lineEdit_20.text()
            id = self.ui.lineEdit_21.text()

            secret = self.get_base32_secret(username)
            print("username", username)
            print("secret", secret)
            print("inputsecret", inputsecret)
            print("truesecret", self.generate_2fa_code_base32(secret))
            if inputsecret == self.generate_2fa_code_base32(secret):
                self.ui.labelBoxBlenderInstalation_41.setText("动态密码验证成功")
                self.ui.labelBoxBlenderInstalation_41.setStyleSheet("color : lightgreen")
                if self.update_user_info(username, phone, email, company, id, name):
                    self.ui.labelBoxBlenderInstalation_41.setText("动态密码验证成功 修改成功")
                    self.ui.labelBoxBlenderInstalation_41.setStyleSheet("color : lightgreen")
                else:
                    self.ui.labelBoxBlenderInstalation_41.setText("动态密码验证成功 修改失败")
                    self.ui.labelBoxBlenderInstalation_41.setStyleSheet("color : red")

            else:
                self.ui.labelBoxBlenderInstalation_41.setText("动态密码验证失败")
                self.ui.labelBoxBlenderInstalation_41.setStyleSheet("color : red")

        if btnName == "btn_update":
            root = tk.Tk()
            root.withdraw()  # 隐藏主窗口

            # 设定当前版本

            # 检查版本
            self.check_version(current_version)

        if btnName == "pushButton_43":
            root = tk.Tk()
            root.withdraw()  # 隐藏主窗口

            # 设定当前版本

            # 检查版本
            self.check_version(current_version)

        if btnName == "pushButton_44":
            print("目前版本", self.localpredictModelVersion)
            print("最新版本", self.predictModelVersion)
            if self.predictModelVersion > self.localpredictModelVersion:
                # 版本更新了，弹窗提示并打开下载链接
                zip_path = 'model/model.zip'
                extract_path = "model"
                password = "HULY62ZZ5TFEW6UL2OPES7XNVE"

                folder = 'model'
                if not os.path.exists(folder):
                    print(f"目录 {folder} 不存在。")
                    return

                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    try:
                        if os.path.isfile(file_path):
                            # 先清除只读属性（Windows 下防止拒绝访问）
                            os.chmod(file_path, stat.S_IWRITE)
                            os.remove(file_path)
                            print(f"已删除文件: {file_path}")
                    except Exception as e:
                        print(f"删除 {file_path} 时出错：{e}")
                self.download_zip(self.transModelLink, zip_path)
                # self.unzip_with_password(zip_path, extract_path, password)
                model_path = self.rename_single_file_in_dir("model/", "model.zip")
                self.set_hidden(extract_path)
                self.set_readonly(extract_path)

                # global username

                raw_key = self.get_base32_secret(username)
                padded_bytes = raw_key.encode('utf-8').ljust(32, b'0')

                # Base64 URL-safe 编码
                key = base64.urlsafe_b64encode(padded_bytes)
                print("key", username)
                print("key", key)
                cipher = Fernet(key)
                self.encrypt_file("model/model.zip", "model/model.enc", cipher)
                os.chmod("model/model.zip", stat.S_IWRITE)
                os.remove("model/model.zip")
                self.set_readonly(extract_path)
                messagebox.showinfo("检查更新", "有新的模型架构、已更新至最新版本")

                conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="yupeihao05ab",
                    database="locallog",
                    charset="utf8mb4"
                )

                try:
                    cursor = conn.cursor()
                    update_query = """
                                    UPDATE localmodel SET
                                        predictModelVersion = %s
                                    WHERE predictModelVersion = %s
                                """
                    cursor.execute(update_query, (self.predictModelVersion, self.localpredictModelVersion))
                    self.localpredictModelVersion = self.predictModelVersion
                    self.ui.label_6.setText(self.localpredictModelVersion)
                    self.ui.label_5.setText(self.predictModelVersion)
                    conn.commit()

                finally:
                    conn.close()
            else:
                # 当前已经是最新版本
                messagebox.showinfo("检查更新", "您已是最新版本.")

            '''
            decrypt_temp_model("model/model.enc", "model/temp_model", cipher)

            # 加载模型或做你要做的事情（例如 torch.load("model/temp_model")）

            # 用后销毁
            cleanup("model/temp_model")
            '''
        if btnName == "pushButton_2":
            raw_key = self.get_base32_secret(username)
            padded_bytes = raw_key.encode('utf-8').ljust(32, b'0')

            # Base64 URL-safe 编码
            key = base64.urlsafe_b64encode(padded_bytes)
            print("key", username)
            print("key", key)
            cipher = Fernet(key)
            self.cleanup("final/model")
            self.decrypt_temp_model("model/model.enc", "final/model/", cipher)
            folder = "final/model"
            old_path = os.path.join(folder, "model")
            zip_path = os.path.join(folder, "model.zip")

            # 重命名 model -> model.zip
            if os.path.isfile(old_path):
                os.rename(old_path, zip_path)
            else:
                print("未找到 model 文件")
                return

            # 解压 model.zip
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(folder)
                print("解压完成")
            except zipfile.BadZipFile:
                print("model.zip 不是一个有效的 ZIP 文件")
            final.main.process_input_files(self.uploadfile)

            # self.cleanup("final/model")
            self.cleanup("final/model")
        if btnName == "pushButton_45":
            print("目前版本", self.localparameterversion)
            print("最新版本", self.parameterversion)
            if self.parameterversion > self.localparameterversion:
                # 版本更新了，弹窗提示并打开下载链接
                messagebox.showinfo("检查更新", "有新的模型参数、已更新至最新版本")

                conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="yupeihao05ab",
                    database="locallog",
                    charset="utf8mb4"
                )

                try:
                    cursor = conn.cursor()
                    update_query = """
                                                UPDATE localparameter SET
                                                    version = %s,
                                                    a = %s,
                                                    b = %s,
                                                    c = %s,
                                                    d = %s,
                                                    e = %s,
                                                    f = %s,
                                                    g = %s,
                                                    h = %s,
                                                    i = %s
                                                WHERE version = %s
                                            """
                    cursor.execute(update_query, (
                    self.parameterversion, self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i,
                    self.localparameterversion))
                    self.localparameterversion = self.parameterversion
                    self.localtrans_a = self.trans_a
                    self.localpredict_a = self.predict_a
                    self.ui.lineEdit_9.setText(str(self.localtrans_a))
                    self.ui.lineEdit_13.setText(str(self.localpredict_a))
                    conn.commit()

                finally:
                    conn.close()
            else:
                # 当前已经是最新版本
                messagebox.showinfo("检查更新", "您已是最新版本.")

            self.updateAll()

        if btnName == "pushButton_46":
            # 版本更新了，弹窗提示并打开下载链接
            messagebox.showinfo("保存成功", "您自定义的配置已保存至本地")

            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="yupeihao05ab",
                database="locallog",
                charset="utf8mb4"
            )

            try:
                cursor = conn.cursor()
                update_query = """
                                            UPDATE localparameter SET
                                                a = %s,
                                                b = %s,
                                                c = %s,
                                                d = %s,
                                                e = %s,
                                                f = %s,
                                                g = %s,
                                                h = %s,
                                                i = %s
                                            WHERE version = %s
                                        """
                cursor.execute(update_query, (
                self.ui.lineEdit_9.text(), self.ui.lineEdit_10.text(), self.ui.lineEdit_11.text(),
                self.ui.lineEdit_12.text(), self.ui.lineEdit_27.text(), self.ui.lineEdit_13.text(),
                self.ui.lineEdit_14.text(), self.ui.lineEdit_15.text(), self.ui.lineEdit_16.text(),
                self.localparameterversion))
                conn.commit()

            finally:
                conn.close()

        if btnName == "pushButton_47":
            # 版本更新了，弹窗提示并打开下载链接
            messagebox.showinfo("保存成功", "您自定义的配置已保存至本地")

            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="yupeihao05ab",
                database="locallog",
                charset="utf8mb4"
            )

            try:
                cursor = conn.cursor()
                update_query = """
                                            UPDATE localparameter SET
                                                a = %s,
                                                b = %s,
                                                c = %s,
                                                d = %s,
                                                e = %s,
                                                f = %s,
                                                g = %s,
                                                h = %s,
                                                i = %s
                                            WHERE version = %s
                                        """
                cursor.execute(update_query, (
                self.ui.lineEdit_9.text(), self.ui.lineEdit_10.text(), self.ui.lineEdit_11.text(),
                self.ui.lineEdit_12.text(), self.ui.lineEdit_27.text(), self.ui.lineEdit_13.text(),
                self.ui.lineEdit_14.text(), self.ui.lineEdit_15.text(), self.ui.lineEdit_16.text(),
                self.localparameterversion))
                conn.commit()

            finally:
                conn.close()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def update_user_info(self, username, phone, email, company, id, name):
        # 建立连接
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            # 执行更新操作
            update_query = """
                UPDATE register
                SET phone = %s,
                    email = %s,
                    company = %s,
                    id = %s,
                    name = %s
                WHERE username = %s
            """
            cursor.execute(update_query, (phone, email, company, id, name, username))
            conn.commit()

            # 返回是否修改成功
            return cursor.rowcount > 0  # 如果受影响行数 > 0，说明修改成功

        finally:
            cursor.close()
            conn.close()

    import pymysql

    def get_user_info(self, username):
        # 建立连接
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            # 执行查询
            query = """
                SELECT phone, email, company, id, name
                FROM register
                WHERE username = %s
            """
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                # 返回字典形式便于使用
                return {
                    "phone": result[0],
                    "email": result[1],
                    "company": result[2],
                    "id": result[3],
                    "name": result[4]
                }
            else:
                return {}  # 未找到该用户

        finally:
            cursor.close()
            conn.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def generate_2fa_code_base32(self, secret_base32: str, interval: int = 30, digits: int = 6) -> str:
        """
        基于 Base32 编码密钥生成 TOTP 动态验证码
        - secret_base32: 例如 '7J64V3P3E77J3LKNUGSZ5QANTLRLTKVL'
        - interval: 时间窗口（秒），默认30
        - digits: 验证码位数，默认6
        """
        # 将 Base32 字符串转为字节（忽略大小写、空格）
        secret = base64.b32decode(secret_base32.upper(), casefold=True)

        # 当前时间窗口计数器
        counter = int(time.time() / interval)
        counter_bytes = struct.pack(">Q", counter)

        # 计算 HMAC-SHA1 摘要
        hmac_digest = hmac.new(secret, counter_bytes, hashlib.sha1).digest()

        # 动态截断获取验证码
        offset = hmac_digest[-1] & 0x0F
        code = struct.unpack(">I", hmac_digest[offset:offset + 4])[0] & 0x7FFFFFFF
        return str(code % (10 ** digits)).zfill(digits)

    def get_base32_secret(self, username: str) -> str | None:
        conn = pymysql.connect(
            host="sql.wsfdb.cn",
            port=3306,
            user="8393455register",
            password="yupeihao05ab",
            database="8393455register",
            charset="utf8mb4"
        )

        try:
            cursor = conn.cursor()
            # 查询base32字段
            query = "SELECT base32 FROM register WHERE username=%s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return result[0]  # base32 密钥字符串
            else:
                return None
        finally:
            cursor.close()
            conn.close()

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()  # 已是 QPoint
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    login = LoginWindow()
    login.show()

    # if debug:
    # mi = MainWindow()
    # mi.show()

    sys.exit(app.exec())

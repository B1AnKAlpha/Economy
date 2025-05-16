# from. resources_rc import *
#pyside6-rcc resources.qrc -o resources_rc.py
#pyside6-uic LoginWindow.ui -o LoginWindow.py
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
import re
import subprocess
import uuid

import psutil
username = "admin"
debug = True
import base64
import hashlib
import hmac
import struct
import pyotp
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import time

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

    def reset_login_fields(self):
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()
        self.lineEdit_token.clear()
        self.statusBar.showMessage("已安全退出")
       # self.statusBar.hide()  # 如果你之前 show() 过 statusBar

    def show_force_exit_popup(self,title: str, message: str, parent: QWidget = None):
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

    def sha256sum(self,filepath):
        """计算文件的 SHA-256 散列值"""
        h = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()

    def check_file_integrity(self,filepath, expected_hash):
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

    def generate_2fa_code_base32(self,secret_base32: str, interval: int = 30, digits: int = 6) -> str:
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

    def get_base32_secret(self,username: str, password: str) -> str | None:
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

    def get_isadmin(self,username: str, password: str) -> str | None:
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
        print("机器码",machinecode)
        self.statusBar.showMessage("正在进行基本环境检测...")
        self.statusBar.setStyleSheet("background-color : lightgreen")
        global username
        username = self.lineEdit_username.text()
        self.username = username
        self.password = self.lineEdit_password.text()
        self.token = self.lineEdit_token.text()
        # 先进行文件完整性检查
        important_file = "main.py"
        expected_hash = self.sha256sum(important_file)

        if not self.check_file_integrity(important_file, expected_hash):
            self.statusBar.showMessage("检测到文件损坏或篡改，请重新下载程序")
            self.statusBar.setStyleSheet("background-color : red")
            QTimer.singleShot(1000, lambda: self.show_force_exit_popup("提示",
                                                                       "检测到文件损坏或篡改，请重新下载程序，已上报基本信息"))
            QTimer.singleShot(3000, sys.exit)
            return
        else:
            self.statusBar.showMessage("文件完整性检查通过")
            self.statusBar.setStyleSheet("background-color : lightgreen")

        # 延迟执行抓包检测（2 秒后）
        QTimer.singleShot(1000, self.run_sniffer_check)
    def machinecode_check(self):
        machine = self.get_machine_code()
        if not self.check_machinecode(machine):
            self.statusBar.showMessage("该机器码未注册，请联系管理员")
            self.statusBar.setStyleSheet("background-color : red")
            QTimer.singleShot(1000,
                              lambda: self.show_force_exit_popup("提示", "该机器码未注册，请联系管理员，已上报基本信息"))
            QTimer.singleShot(3000, sys.exit)
        else:
            self.statusBar.showMessage("机器码检查通过")
            self.statusBar.setStyleSheet("background-color : lightgreen")
            QTimer.singleShot(1000, self.verify_credentials)
    def run_sniffer_check(self):
        if self.detect_packet_sniffer():
            self.statusBar.showMessage("检测到抓包工具，请关闭后重试")
            self.statusBar.setStyleSheet("background-color : red")
            QTimer.singleShot(1000,
                              lambda: self.show_force_exit_popup("提示", "检测到抓包工具，请关闭后重试，已上报基本信息"))
            QTimer.singleShot(3000, sys.exit)
        else:
            self.statusBar.showMessage("反抓包检查通过")
            self.statusBar.setStyleSheet("background-color : lightgreen")
            QTimer.singleShot(1000, self.machinecode_check)

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
                print("是否为管理员：",admin)
                if admin == 1:
                    self.statusBar.showMessage("欢迎您，管理员！正在跳转中...")
                else:
                    self.statusBar.showMessage("欢迎您，认证用户！正在跳转中...")

                self.statusBar.setStyleSheet("background-color : lightgreen")
                QTimer.singleShot(2000, self.open_main_window)
            else:
                self.statusBar.showMessage("动态密码错误")
                self.statusBar.setStyleSheet("background-color : pink")

        except Exception as e:
            print("错误：",e)
            self.statusBar.showMessage(f"数据库错误: {e}")
            self.statusBar.setStyleSheet("background-color : pink")


class MainWindow(QMainWindow):
    def __init__(self,login_window):
        QMainWindow.__init__(self)

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
        if admin!=1:
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
        self.export_buttons3= {}
        for row in range(1, row_count):  # 从第二行开始，即索引1

            button = QPushButton("导出为PDF")
            button.clicked.connect(lambda checked, r=row: export_to_pdf(r))
            button.setStyleSheet(button_style1)
            # 可以连接按钮点击事件，比如 button.clicked.connect(lambda: do_something(row))

            button_widget = QWidget()
            layout = QHBoxLayout(button_widget)
            layout.addWidget(button)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中
            layout.setContentsMargins(0, 0, 0, 0)  # 去除边距
            self.export_buttons[row] = button
            # 设置到表格单元格中
            widgets.tableWidget_4.setCellWidget(row, 2, button_widget)

            #widgets.tableWidget_4.setCellWidget(row, 2, button)


        font = QFont()
        font.setPointSize(14)  # 设置字号为14
        font.setBold(True)  # 设置为粗体

        # 应用于 QLabel
        widgets.labelBoxBlenderInstalation_6.setFont(font)
        widgets.labelBoxBlenderInstalation_7.setFont(font)



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
                load_user_table()  # 刷新表格

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
                    load_user_table()  # 重新加载刷新
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
                self.ui.tableWidget_5.setRowCount(len(results)+1)
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

        res = self.get_user_info(username)
        self.ui.lineEdit_17.setText(res["phone"])
        self.ui.lineEdit_18.setText(res["name"])
        self.ui.lineEdit_19.setText(res["email"])
        self.ui.lineEdit_20.setText(res["company"])
        self.ui.lineEdit_21.setText(res["id"])
        load_user_table(self)
        row_count = self.ui.tableWidget_5.rowCount()
        for i in range(row_count+1):
            self.ui.tableWidget_5.setRowHeight(i, 40)
        self.ui.tableWidget_5.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)







        def export_to_pdf(row_index):
            print(f"导出第 {row_index + 1} 行数据为 PDF")  # 实际逻辑替换这里

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

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
        themeFile = "themes\py_dracula_light.qss"
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


    def logout(self):
        self.close()                     # 关闭主窗口
        self.login_window.show()
        self.login_window.reset_login_fields()

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

    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
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
                self.uploadfile = self.uploadfile+files
                widgets.lineEdit_2.setText(self.str)
                # 输出 2：文件路径列表
                print("图片文件名字符串：", self.str)
                print("总图片路径列表：", self.uploadfile)

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

        if btnName=="pushButton_3":
            self.uploadtext += widgets.plainTextEdit_2.toPlainText()+" "
            widgets.plainTextEdit_2.setPlaceholderText("待分析数据已上传成功")
            widgets.plainTextEdit_2.setPlainText("")
            print("uploadtext",self.uploadtext)

        if btnName == "btn_save":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            print("Save BTN clicked!")
            #QMessageBox.information(self, "Save", "该功能未实现!")

        if btnName == "btn_themechange":
            print("Save BTN clicked!")
            if self.useCustomTheme:
                # LOAD AND APPLY STYLE
                self.themeFile = "themes\py_dracula_dark.qss"
                UIFunctions.theme(self, self.themeFile, True)

                # SET HACKS
                AppFunctions.setThemeHack(self, target=2)
                self.useCustomTheme = False
                for button in self.export_buttons.values():
                    button.setStyleSheet(button_style2)

                for button in self.export_buttons2.values():
                    button.setStyleSheet(button_stylewhite)

                for button in self.export_buttons3.values():
                    button.setStyleSheet(button_stylewhite)
            else:
                # LOAD AND APPLY STYLE
                self.themeFile = "themes\py_dracula_light.qss"
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

        if btnName == "pushButton_50":
            inputsecret = self.ui.lineEdit_22.text()
            phone = self.ui.lineEdit_17.text()
            name = self.ui.lineEdit_18.text()
            email = self.ui.lineEdit_19.text()
            company = self.ui.lineEdit_20.text()
            id=self.ui.lineEdit_21.text()
            global username

            secret = self.get_base32_secret(username)
            print("username",username)
            print("secret",secret)
            print("inputsecret",inputsecret)
            print("truesecret",self.generate_2fa_code_base32(secret))
            if inputsecret ==self.generate_2fa_code_base32(secret):
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
                return None  # 未找到该用户

        finally:
            cursor.close()
            conn.close()


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def generate_2fa_code_base32(self,secret_base32: str, interval: int = 30, digits: int = 6) -> str:
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

    def get_base32_secret(self,username: str) -> str | None:
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
            cursor.execute(query, (username, ))
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
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    admin = 1

    login = LoginWindow()
    login.show()

    #if debug:
        # mi = MainWindow()
        # mi.show()

    sys.exit(app.exec())

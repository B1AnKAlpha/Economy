# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(362, 582)
        MainWindow.setMinimumSize(QSize(362, 582))
        MainWindow.setMaximumSize(QSize(362, 582))
        font = QFont()
        font.setPointSize(7)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(98, 114, 164)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(98, 114, 164)")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setPixmap(QPixmap(u"login.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(17)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"color: rgb(134, 134, 134);\n"
"\n"
"\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineEdit_username = QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(9)
        self.lineEdit_username.setFont(font2)
        self.lineEdit_username.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(238, 238, 236);\n"
"    border-radius: 10px;\n"
"    padding: 2px;\n"
"    background-color: #fff;\n"
"   /* color: rgb(200, 200, 200); */\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid   rgb(114, 159, 207);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.lineEdit_username.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_username)

        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 30))
        self.lineEdit_password.setFont(font2)
        self.lineEdit_password.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(238, 238, 236);\n"
"    border-radius: 10px;\n"
"    padding: 2px;\n"
"    background-color: #fff;\n"
"   /* color: rgb(200, 200, 200); */\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid   rgb(114, 159, 207);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_password)

        self.checkBox_show_password = QCheckBox(self.centralwidget)
        self.checkBox_show_password.setObjectName(u"checkBox_show_password")
        self.checkBox_show_password.setMinimumSize(QSize(0, 30))
        self.checkBox_show_password.setFont(font2)

        self.verticalLayout.addWidget(self.checkBox_show_password)

        self.button_login = QPushButton(self.centralwidget)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        self.button_login.setFont(font3)
        self.button_login.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color:#2ecc71;\n"
"	color:#fff;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border:1px solid;\n"
"	border-color: #27ae60;\n"
"	background-color: rgb(50, 227, 124);\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"    background-color: #27ae60;\n"
"	border-radius: 10px;\n"
"	border:1px solid rgb(0, 223, 108);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.button_login)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(9)
        self.statusBar.setFont(font4)
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.button_login, self.lineEdit_username)
        QWidget.setTabOrder(self.lineEdit_username, self.lineEdit_password)
        QWidget.setTabOrder(self.lineEdit_password, self.checkBox_show_password)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5458 \u5de5 \u767b \u5f55", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox_show_password.setText(QCoreApplication.translate("MainWindow", u"Show password", None))
        self.button_login.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
    # retranslateUi


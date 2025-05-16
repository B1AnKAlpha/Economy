# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
from. resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1127, 576)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_84 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(0, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy1)
        self.topMenu.setMinimumSize(QSize(0, 0))
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_upload = QPushButton(self.topMenu)
        self.btn_upload.setObjectName(u"btn_upload")
        sizePolicy.setHeightForWidth(self.btn_upload.sizePolicy().hasHeightForWidth())
        self.btn_upload.setSizePolicy(sizePolicy)
        self.btn_upload.setMinimumSize(QSize(0, 45))
        self.btn_upload.setFont(font)
        self.btn_upload.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_upload.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_upload.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.btn_upload)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-window-restore.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png);")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_para = QPushButton(self.topMenu)
        self.btn_para.setObjectName(u"btn_para")
        sizePolicy.setHeightForWidth(self.btn_para.sizePolicy().hasHeightForWidth())
        self.btn_para.setSizePolicy(sizePolicy)
        self.btn_para.setMinimumSize(QSize(0, 45))
        self.btn_para.setFont(font)
        self.btn_para.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_para.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_para.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_para)

        self.btn_information = QPushButton(self.topMenu)
        self.btn_information.setObjectName(u"btn_information")
        sizePolicy.setHeightForWidth(self.btn_information.sizePolicy().hasHeightForWidth())
        self.btn_information.setSizePolicy(sizePolicy)
        self.btn_information.setMinimumSize(QSize(0, 45))
        self.btn_information.setFont(font)
        self.btn_information.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_information.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_information.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")

        self.verticalLayout_8.addWidget(self.btn_information)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy1)
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.formLayout_2 = QFormLayout(self.home)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 287, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.row_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.row_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(150, 30))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_7.setIcon(icon4)

        self.horizontalLayout_12.addWidget(self.pushButton_7)


        self.gridLayout_4.addWidget(self.frame_5, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_6 = QFrame(self.new_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(300, 16777215))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_9)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.labelBoxBlenderInstalation_7 = QLabel(self.frame_9)
        self.labelBoxBlenderInstalation_7.setObjectName(u"labelBoxBlenderInstalation_7")
        self.labelBoxBlenderInstalation_7.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_7.setFont(font)
        self.labelBoxBlenderInstalation_7.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.labelBoxBlenderInstalation_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.plainTextEdit_14 = QPlainTextEdit(self.frame_9)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")
        self.plainTextEdit_14.setMinimumSize(QSize(100, 50))
        self.plainTextEdit_14.setAutoFillBackground(False)
        self.plainTextEdit_14.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.plainTextEdit_14.setTabStopDistance(78.000000000000000)

        self.verticalLayout_34.addWidget(self.plainTextEdit_14)

        self.pushButton_40 = QPushButton(self.frame_9)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(150, 30))
        self.pushButton_40.setFont(font)
        self.pushButton_40.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_40.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpenRecent))
        self.pushButton_40.setIcon(icon6)

        self.verticalLayout_34.addWidget(self.pushButton_40)

        self.pushButton_41 = QPushButton(self.frame_9)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(150, 30))
        self.pushButton_41.setFont(font)
        self.pushButton_41.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_41.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.pushButton_41.setIcon(icon7)

        self.verticalLayout_34.addWidget(self.pushButton_41)


        self.horizontalLayout_13.addWidget(self.frame_9)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.labelBoxBlenderInstalation_6 = QLabel(self.frame_6)
        self.labelBoxBlenderInstalation_6.setObjectName(u"labelBoxBlenderInstalation_6")
        self.labelBoxBlenderInstalation_6.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_6.setFont(font)
        self.labelBoxBlenderInstalation_6.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.labelBoxBlenderInstalation_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget_4 = QTableWidget(self.frame_6)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        if (self.tableWidget_4.rowCount() < 16):
            self.tableWidget_4.setRowCount(16)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font4);
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(8, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(9, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(10, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(11, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(12, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(13, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(14, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(15, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, __qtablewidgetitem45)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        sizePolicy4.setHeightForWidth(self.tableWidget_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_4.setSizePolicy(sizePolicy4)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_4.setPalette(palette1)
        self.tableWidget_4.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_4.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_4.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_4.setShowGrid(True)
        self.tableWidget_4.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.verticalHeader().setHighlightSections(False)
        self.tableWidget_4.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_31.addWidget(self.tableWidget_4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_31)


        self.verticalLayout_20.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.new_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_38 = QVBoxLayout(self.page_2)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_85 = QVBoxLayout()
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.row_7 = QFrame(self.page_2)
        self.row_7.setObjectName(u"row_7")
        self.row_7.setMinimumSize(QSize(0, 150))
        self.row_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.row_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_10 = QFrame(self.row_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(300, 16777215))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.labelBoxBlenderInstalation_10 = QLabel(self.frame_10)
        self.labelBoxBlenderInstalation_10.setObjectName(u"labelBoxBlenderInstalation_10")
        self.labelBoxBlenderInstalation_10.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_10.setFont(font)
        self.labelBoxBlenderInstalation_10.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.labelBoxBlenderInstalation_10)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_19.addWidget(self.lineEdit_3)


        self.verticalLayout_35.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.labelBoxBlenderInstalation_11 = QLabel(self.frame_10)
        self.labelBoxBlenderInstalation_11.setObjectName(u"labelBoxBlenderInstalation_11")
        self.labelBoxBlenderInstalation_11.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_11.setFont(font)
        self.labelBoxBlenderInstalation_11.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.labelBoxBlenderInstalation_11)

        self.lineEdit_4 = QLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_20.addWidget(self.lineEdit_4)


        self.verticalLayout_35.addLayout(self.horizontalLayout_20)


        self.verticalLayout_41.addLayout(self.verticalLayout_35)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_2)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.labelBoxBlenderInstalation_13 = QLabel(self.frame_10)
        self.labelBoxBlenderInstalation_13.setObjectName(u"labelBoxBlenderInstalation_13")
        self.labelBoxBlenderInstalation_13.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_13.setFont(font)
        self.labelBoxBlenderInstalation_13.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.labelBoxBlenderInstalation_13)

        self.lineEdit_6 = QLineEdit(self.frame_10)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_22.addWidget(self.lineEdit_6)


        self.verticalLayout_39.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.labelBoxBlenderInstalation_12 = QLabel(self.frame_10)
        self.labelBoxBlenderInstalation_12.setObjectName(u"labelBoxBlenderInstalation_12")
        self.labelBoxBlenderInstalation_12.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_12.setFont(font)
        self.labelBoxBlenderInstalation_12.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.labelBoxBlenderInstalation_12)

        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_21.addWidget(self.lineEdit_5)


        self.verticalLayout_39.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_3)


        self.verticalLayout_41.addLayout(self.verticalLayout_39)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.labelBoxBlenderInstalation_15 = QLabel(self.frame_10)
        self.labelBoxBlenderInstalation_15.setObjectName(u"labelBoxBlenderInstalation_15")
        self.labelBoxBlenderInstalation_15.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_15.setFont(font)
        self.labelBoxBlenderInstalation_15.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.labelBoxBlenderInstalation_15)

        self.lineEdit_8 = QLineEdit(self.frame_10)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 30))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_24.addWidget(self.lineEdit_8)


        self.verticalLayout_40.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.labelBoxBlenderInstalation_14 = QLabel(self.frame_10)
        self.labelBoxBlenderInstalation_14.setObjectName(u"labelBoxBlenderInstalation_14")
        self.labelBoxBlenderInstalation_14.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_14.setFont(font)
        self.labelBoxBlenderInstalation_14.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.labelBoxBlenderInstalation_14)

        self.lineEdit_7 = QLineEdit(self.frame_10)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_23.addWidget(self.lineEdit_7)


        self.verticalLayout_40.addLayout(self.horizontalLayout_23)


        self.verticalLayout_41.addLayout(self.verticalLayout_40)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_4)

        self.pushButton_43 = QPushButton(self.frame_10)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMinimumSize(QSize(150, 30))
        self.pushButton_43.setFont(font)
        self.pushButton_43.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_43.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_41.addWidget(self.pushButton_43)

        self.pushButton_44 = QPushButton(self.frame_10)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(150, 30))
        self.pushButton_44.setFont(font)
        self.pushButton_44.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_44.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_41.addWidget(self.pushButton_44)

        self.pushButton_45 = QPushButton(self.frame_10)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(150, 30))
        self.pushButton_45.setFont(font)
        self.pushButton_45.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_45.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_41.addWidget(self.pushButton_45)


        self.horizontalLayout_15.addWidget(self.frame_10)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, -1, -1, 10)
        self.labelBoxBlenderInstalation_8 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_8.setObjectName(u"labelBoxBlenderInstalation_8")
        self.labelBoxBlenderInstalation_8.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_8.setFont(font)
        self.labelBoxBlenderInstalation_8.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.labelBoxBlenderInstalation_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)

        self.labelBoxBlenderInstalation_16 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_16.setObjectName(u"labelBoxBlenderInstalation_16")
        self.labelBoxBlenderInstalation_16.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_16.setFont(font)
        self.labelBoxBlenderInstalation_16.setStyleSheet(u"")

        self.horizontalLayout_25.addWidget(self.labelBoxBlenderInstalation_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_9 = QLineEdit(self.row_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 30))
        self.lineEdit_9.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_25.addWidget(self.lineEdit_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)


        self.verticalLayout_36.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_3)

        self.labelBoxBlenderInstalation_17 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_17.setObjectName(u"labelBoxBlenderInstalation_17")
        self.labelBoxBlenderInstalation_17.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_17.setFont(font)
        self.labelBoxBlenderInstalation_17.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.labelBoxBlenderInstalation_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_10 = QLineEdit(self.row_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 30))
        self.lineEdit_10.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_26.addWidget(self.lineEdit_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_4)


        self.verticalLayout_36.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)

        self.labelBoxBlenderInstalation_18 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_18.setObjectName(u"labelBoxBlenderInstalation_18")
        self.labelBoxBlenderInstalation_18.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_18.setFont(font)
        self.labelBoxBlenderInstalation_18.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.labelBoxBlenderInstalation_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_11 = QLineEdit(self.row_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 30))
        self.lineEdit_11.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_27.addWidget(self.lineEdit_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_6)


        self.verticalLayout_36.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_7)

        self.labelBoxBlenderInstalation_19 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_19.setObjectName(u"labelBoxBlenderInstalation_19")
        self.labelBoxBlenderInstalation_19.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_19.setFont(font)
        self.labelBoxBlenderInstalation_19.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.labelBoxBlenderInstalation_19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_12 = QLineEdit(self.row_7)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 30))
        self.lineEdit_12.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_28.addWidget(self.lineEdit_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_8)


        self.verticalLayout_36.addLayout(self.horizontalLayout_28)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_5)

        self.pushButton_46 = QPushButton(self.row_7)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(250, 30))
        self.pushButton_46.setMaximumSize(QSize(250, 16777215))
        self.pushButton_46.setFont(font)
        self.pushButton_46.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_46.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_36.addWidget(self.pushButton_46, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_36)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, -1, -1, 10)
        self.labelBoxBlenderInstalation_9 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_9.setObjectName(u"labelBoxBlenderInstalation_9")
        self.labelBoxBlenderInstalation_9.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_9.setFont(font)
        self.labelBoxBlenderInstalation_9.setStyleSheet(u"")

        self.verticalLayout_37.addWidget(self.labelBoxBlenderInstalation_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_9)

        self.labelBoxBlenderInstalation_20 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_20.setObjectName(u"labelBoxBlenderInstalation_20")
        self.labelBoxBlenderInstalation_20.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_20.setFont(font)
        self.labelBoxBlenderInstalation_20.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.labelBoxBlenderInstalation_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_13 = QLineEdit(self.row_7)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(0, 30))
        self.lineEdit_13.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_29.addWidget(self.lineEdit_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_10)


        self.verticalLayout_37.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_11)

        self.labelBoxBlenderInstalation_21 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_21.setObjectName(u"labelBoxBlenderInstalation_21")
        self.labelBoxBlenderInstalation_21.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_21.setFont(font)
        self.labelBoxBlenderInstalation_21.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.labelBoxBlenderInstalation_21, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_14 = QLineEdit(self.row_7)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 30))
        self.lineEdit_14.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_30.addWidget(self.lineEdit_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_12)


        self.verticalLayout_37.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_13)

        self.labelBoxBlenderInstalation_22 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_22.setObjectName(u"labelBoxBlenderInstalation_22")
        self.labelBoxBlenderInstalation_22.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_22.setFont(font)
        self.labelBoxBlenderInstalation_22.setStyleSheet(u"")

        self.horizontalLayout_31.addWidget(self.labelBoxBlenderInstalation_22, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_15 = QLineEdit(self.row_7)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 30))
        self.lineEdit_15.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_31.addWidget(self.lineEdit_15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_14)


        self.verticalLayout_37.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_15)

        self.labelBoxBlenderInstalation_23 = QLabel(self.row_7)
        self.labelBoxBlenderInstalation_23.setObjectName(u"labelBoxBlenderInstalation_23")
        self.labelBoxBlenderInstalation_23.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_23.setFont(font)
        self.labelBoxBlenderInstalation_23.setStyleSheet(u"")

        self.horizontalLayout_32.addWidget(self.labelBoxBlenderInstalation_23, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_16 = QLineEdit(self.row_7)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 30))
        self.lineEdit_16.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_32.addWidget(self.lineEdit_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_16)


        self.verticalLayout_37.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_6)

        self.pushButton_47 = QPushButton(self.row_7)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(250, 30))
        self.pushButton_47.setMaximumSize(QSize(250, 16777215))
        self.pushButton_47.setFont(font)
        self.pushButton_47.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_47.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_37.addWidget(self.pushButton_47, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_15.addLayout(self.verticalLayout_37)


        self.verticalLayout_85.addWidget(self.row_7)


        self.verticalLayout_38.addLayout(self.verticalLayout_85)

        self.stackedWidget.addWidget(self.page_2)
        self.information = QWidget()
        self.information.setObjectName(u"information")
        self.verticalLayout_48 = QVBoxLayout(self.information)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_86 = QVBoxLayout()
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.row_8 = QFrame(self.information)
        self.row_8.setObjectName(u"row_8")
        self.row_8.setMinimumSize(QSize(0, 150))
        self.row_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.row_8)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_11 = QFrame(self.row_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 0))
        self.frame_11.setMaximumSize(QSize(300000, 16777215))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_11)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.labelBoxBlenderInstalation_40 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_40.setObjectName(u"labelBoxBlenderInstalation_40")
        self.labelBoxBlenderInstalation_40.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_40.setFont(font)
        self.labelBoxBlenderInstalation_40.setStyleSheet(u"")

        self.verticalLayout_42.addWidget(self.labelBoxBlenderInstalation_40, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.labelBoxBlenderInstalation_24 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_24.setObjectName(u"labelBoxBlenderInstalation_24")
        self.labelBoxBlenderInstalation_24.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_24.setFont(font)
        self.labelBoxBlenderInstalation_24.setStyleSheet(u"")

        self.horizontalLayout_33.addWidget(self.labelBoxBlenderInstalation_24)

        self.lineEdit_17 = QLineEdit(self.frame_11)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 30))
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_33.addWidget(self.lineEdit_17)


        self.verticalLayout_43.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.labelBoxBlenderInstalation_25 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_25.setObjectName(u"labelBoxBlenderInstalation_25")
        self.labelBoxBlenderInstalation_25.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_25.setFont(font)
        self.labelBoxBlenderInstalation_25.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.labelBoxBlenderInstalation_25)

        self.lineEdit_18 = QLineEdit(self.frame_11)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(0, 30))
        self.lineEdit_18.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_34.addWidget(self.lineEdit_18)


        self.verticalLayout_43.addLayout(self.horizontalLayout_34)


        self.verticalLayout_42.addLayout(self.verticalLayout_43)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.labelBoxBlenderInstalation_26 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_26.setObjectName(u"labelBoxBlenderInstalation_26")
        self.labelBoxBlenderInstalation_26.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_26.setFont(font)
        self.labelBoxBlenderInstalation_26.setStyleSheet(u"")

        self.horizontalLayout_35.addWidget(self.labelBoxBlenderInstalation_26)

        self.lineEdit_19 = QLineEdit(self.frame_11)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(0, 30))
        self.lineEdit_19.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_35.addWidget(self.lineEdit_19)


        self.verticalLayout_44.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.labelBoxBlenderInstalation_27 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_27.setObjectName(u"labelBoxBlenderInstalation_27")
        self.labelBoxBlenderInstalation_27.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_27.setFont(font)
        self.labelBoxBlenderInstalation_27.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.labelBoxBlenderInstalation_27)

        self.lineEdit_20 = QLineEdit(self.frame_11)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(0, 30))
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_36.addWidget(self.lineEdit_20)


        self.verticalLayout_44.addLayout(self.horizontalLayout_36)


        self.verticalLayout_42.addLayout(self.verticalLayout_44)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.labelBoxBlenderInstalation_28 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_28.setObjectName(u"labelBoxBlenderInstalation_28")
        self.labelBoxBlenderInstalation_28.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_28.setFont(font)
        self.labelBoxBlenderInstalation_28.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.labelBoxBlenderInstalation_28)

        self.lineEdit_21 = QLineEdit(self.frame_11)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 30))
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_37.addWidget(self.lineEdit_21)


        self.verticalLayout_45.addLayout(self.horizontalLayout_37)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_45.addItem(self.verticalSpacer_7)


        self.verticalLayout_42.addLayout(self.verticalLayout_45)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.labelBoxBlenderInstalation_29 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_29.setObjectName(u"labelBoxBlenderInstalation_29")
        self.labelBoxBlenderInstalation_29.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_29.setFont(font)
        self.labelBoxBlenderInstalation_29.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.labelBoxBlenderInstalation_29)

        self.lineEdit_22 = QLineEdit(self.frame_11)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(0, 30))
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_38.addWidget(self.lineEdit_22)


        self.verticalLayout_42.addLayout(self.horizontalLayout_38)

        self.pushButton_50 = QPushButton(self.frame_11)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(150, 30))
        self.pushButton_50.setFont(font)
        self.pushButton_50.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_50.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_42.addWidget(self.pushButton_50)

        self.labelBoxBlenderInstalation_41 = QLabel(self.frame_11)
        self.labelBoxBlenderInstalation_41.setObjectName(u"labelBoxBlenderInstalation_41")

        self.verticalLayout_42.addWidget(self.labelBoxBlenderInstalation_41)


        self.horizontalLayout_18.addWidget(self.frame_11)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.labelBoxBlenderInstalation_30 = QLabel(self.row_8)
        self.labelBoxBlenderInstalation_30.setObjectName(u"labelBoxBlenderInstalation_30")
        self.labelBoxBlenderInstalation_30.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_30.setFont(font)
        self.labelBoxBlenderInstalation_30.setStyleSheet(u"")

        self.verticalLayout_46.addWidget(self.labelBoxBlenderInstalation_30, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget_5 = QTableWidget(self.row_8)
        if (self.tableWidget_5.columnCount() < 9):
            self.tableWidget_5.setColumnCount(9)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, __qtablewidgetitem54)
        if (self.tableWidget_5.rowCount() < 4):
            self.tableWidget_5.setRowCount(4)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFont(font4);
        self.tableWidget_5.setVerticalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 3, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 4, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 5, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 6, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 7, __qtablewidgetitem66)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        sizePolicy.setHeightForWidth(self.tableWidget_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_5.setSizePolicy(sizePolicy)
        self.tableWidget_5.setSizeIncrement(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_5.setPalette(palette2)
        self.tableWidget_5.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_5.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_5.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_5.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_5.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_5.setShowGrid(True)
        self.tableWidget_5.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.verticalHeader().setHighlightSections(False)
        self.tableWidget_5.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_46.addWidget(self.tableWidget_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_10)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_13)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_8)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_14)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_11)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_12)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_9)


        self.horizontalLayout_18.addLayout(self.verticalLayout_46)


        self.verticalLayout_86.addWidget(self.row_8)


        self.verticalLayout_48.addLayout(self.verticalLayout_86)

        self.stackedWidget.addWidget(self.information)
        self.upload = QWidget()
        self.upload.setObjectName(u"upload")
        self.upload.setStyleSheet(u"b")
        self.verticalLayout_27 = QVBoxLayout(self.upload)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.row_5 = QFrame(self.upload)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setEnabled(True)
        self.row_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.row_5)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_3 = QFrame(self.row_5)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_title_wid_3.sizePolicy().hasHeightForWidth())
        self.frame_title_wid_3.setSizePolicy(sizePolicy1)
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.labelBoxBlenderInstalation_3)


        self.verticalLayout_25.addWidget(self.frame_title_wid_3)

        self.frame = QFrame(self.row_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_3)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 813, 184))
        self.scrollAreaWidgetContents_3.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(200, 50))
        self.plainTextEdit_2.setAutoFillBackground(False)
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.plainTextEdit_2.setTabStopDistance(78.000000000000000)

        self.horizontalLayout_7.addWidget(self.plainTextEdit_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_29.addWidget(self.scrollArea_2)

        self.labelVersion_5 = QLabel(self.frame_3)
        self.labelVersion_5.setObjectName(u"labelVersion_5")
        self.labelVersion_5.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelVersion_5.setMargin(5)

        self.verticalLayout_29.addWidget(self.labelVersion_5)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_21 = QVBoxLayout(self.frame_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, 20)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(150, 30))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-satelite.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon8)

        self.verticalLayout_21.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-text-square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon9)

        self.verticalLayout_21.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(150, 30))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_5.setIcon(icon4)

        self.verticalLayout_21.addWidget(self.pushButton_5)


        self.horizontalLayout_6.addWidget(self.frame_2)


        self.horizontalLayout_8.addWidget(self.frame_4)


        self.verticalLayout_25.addWidget(self.frame)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")

        self.verticalLayout_25.addLayout(self.verticalLayout_28)


        self.verticalLayout_27.addWidget(self.row_5)

        self.row_4 = QFrame(self.upload)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setEnabled(True)
        self.row_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.row_4)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.row_4)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_title_wid_2.sizePolicy().hasHeightForWidth())
        self.frame_title_wid_2.setSizePolicy(sizePolicy1)
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_24.addWidget(self.labelBoxBlenderInstalation_2)


        self.verticalLayout_22.addWidget(self.frame_title_wid_2)

        self.frame_div_content_2 = QFrame(self.row_4)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setEnabled(True)
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_2 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelVersion_4, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_content_wid_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon10)

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_3)


        self.verticalLayout_23.addWidget(self.frame_content_wid_2)


        self.verticalLayout_22.addWidget(self.frame_div_content_2)


        self.verticalLayout_27.addWidget(self.row_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.upload)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_15 = QVBoxLayout(self.page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_83 = QVBoxLayout()
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.row_6 = QFrame(self.page)
        self.row_6.setObjectName(u"row_6")
        self.row_6.setMinimumSize(QSize(0, 150))
        self.row_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.row_6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_8 = QFrame(self.row_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(450, 0))
        self.frame_8.setMaximumSize(QSize(300, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_8)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.labelBoxBlenderInstalation_31 = QLabel(self.frame_8)
        self.labelBoxBlenderInstalation_31.setObjectName(u"labelBoxBlenderInstalation_31")
        self.labelBoxBlenderInstalation_31.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_31.setFont(font)
        self.labelBoxBlenderInstalation_31.setStyleSheet(u"")

        self.verticalLayout_47.addWidget(self.labelBoxBlenderInstalation_31, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget_6 = QTableWidget(self.frame_8)
        if (self.tableWidget_6.columnCount() < 4):
            self.tableWidget_6.setColumnCount(4)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem70)
        if (self.tableWidget_6.rowCount() < 16):
            self.tableWidget_6.setRowCount(16)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font4);
        self.tableWidget_6.setVerticalHeaderItem(0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(2, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(3, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(4, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(5, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(6, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(7, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(8, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(9, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(10, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(11, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(12, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(13, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(14, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(15, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setItem(0, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget_6.setItem(0, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setItem(0, 2, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_6.setItem(0, 3, __qtablewidgetitem90)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        sizePolicy4.setHeightForWidth(self.tableWidget_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_6.setSizePolicy(sizePolicy4)
        self.tableWidget_6.setMinimumSize(QSize(0, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_6.setPalette(palette3)
        self.tableWidget_6.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_6.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_6.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_6.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_6.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_6.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_6.setShowGrid(True)
        self.tableWidget_6.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_6.setSortingEnabled(False)
        self.tableWidget_6.horizontalHeader().setVisible(False)
        self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_6.verticalHeader().setHighlightSections(False)
        self.tableWidget_6.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_47.addWidget(self.tableWidget_6)


        self.verticalLayout_30.addLayout(self.verticalLayout_47)

        self.verticalSpacer_15 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_15)

        self.plainTextEdit_13 = QPlainTextEdit(self.frame_8)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setMinimumSize(QSize(100, 0))
        self.plainTextEdit_13.setMaximumSize(QSize(16777215, 45))
        self.plainTextEdit_13.setAutoFillBackground(False)
        self.plainTextEdit_13.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.plainTextEdit_13.setTabStopDistance(78.000000000000000)

        self.verticalLayout_30.addWidget(self.plainTextEdit_13)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_39 = QPushButton(self.frame_8)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(90, 30))
        self.pushButton_39.setMaximumSize(QSize(200, 30))
        self.pushButton_39.setFont(font)
        self.pushButton_39.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_39.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_39.setIcon(icon11)

        self.horizontalLayout_39.addWidget(self.pushButton_39)

        self.pushButton_42 = QPushButton(self.frame_8)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(90, 30))
        self.pushButton_42.setMaximumSize(QSize(16777215, 30))
        self.pushButton_42.setFont(font)
        self.pushButton_42.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_42.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_42.setIcon(icon12)

        self.horizontalLayout_39.addWidget(self.pushButton_42)


        self.verticalLayout_30.addLayout(self.horizontalLayout_39)

        self.comboBox_2 = QComboBox(self.frame_8)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(16777215, 40))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_2.setIconSize(QSize(16, 16))
        self.comboBox_2.setFrame(True)

        self.verticalLayout_30.addWidget(self.comboBox_2)


        self.horizontalLayout_17.addWidget(self.frame_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.labelBoxBlenderInstalation_4 = QLabel(self.row_6)
        self.labelBoxBlenderInstalation_4.setObjectName(u"labelBoxBlenderInstalation_4")
        self.labelBoxBlenderInstalation_4.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_4.setFont(font)
        self.labelBoxBlenderInstalation_4.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.labelBoxBlenderInstalation_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget_3 = QTableWidget(self.row_6)
        if (self.tableWidget_3.columnCount() < 1):
            self.tableWidget_3.setColumnCount(1)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem91)
        if (self.tableWidget_3.rowCount() < 16):
            self.tableWidget_3.setRowCount(16)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setFont(font4);
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem108)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy4.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy4)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_3.setPalette(palette4)
        self.tableWidget_3.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_33.addWidget(self.tableWidget_3)


        self.horizontalLayout_14.addLayout(self.verticalLayout_33)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.labelBoxBlenderInstalation_5 = QLabel(self.row_6)
        self.labelBoxBlenderInstalation_5.setObjectName(u"labelBoxBlenderInstalation_5")
        self.labelBoxBlenderInstalation_5.setMaximumSize(QSize(167, 16777215))
        self.labelBoxBlenderInstalation_5.setFont(font)
        self.labelBoxBlenderInstalation_5.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.labelBoxBlenderInstalation_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget_2 = QTableWidget(self.row_6)
        if (self.tableWidget_2.columnCount() < 1):
            self.tableWidget_2.setColumnCount(1)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem109)
        if (self.tableWidget_2.rowCount() < 16):
            self.tableWidget_2.setRowCount(16)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setFont(font4);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem126)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy4.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy4)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_2.setPalette(palette5)
        self.tableWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_32.addWidget(self.tableWidget_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_32)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_14)


        self.verticalLayout_83.addWidget(self.row_6)


        self.verticalLayout_15.addLayout(self.verticalLayout_83)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout_16.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setMinimumSize(QSize(0, 0))
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_themechange = QPushButton(self.topMenus)
        self.btn_themechange.setObjectName(u"btn_themechange")
        sizePolicy.setHeightForWidth(self.btn_themechange.sizePolicy().hasHeightForWidth())
        self.btn_themechange.setSizePolicy(sizePolicy)
        self.btn_themechange.setMinimumSize(QSize(0, 45))
        self.btn_themechange.setFont(font)
        self.btn_themechange.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_themechange.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_themechange.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-highligt.png);")

        self.verticalLayout_14.addWidget(self.btn_themechange)

        self.btn_update = QPushButton(self.topMenus)
        self.btn_update.setObjectName(u"btn_update")
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        self.btn_update.setMinimumSize(QSize(0, 45))
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_update.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloud-upload.png);")

        self.verticalLayout_14.addWidget(self.btn_update)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x-circle.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.version_2 = QLabel(self.bottomBar)
        self.version_2.setObjectName(u"version_2")
        self.version_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version_2)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.extraCloseColumnBtn.setIcon(icon3)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)


        self.verticalLayout_84.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u91d1\u76feFraudShield</p></body></html>", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"AI\u8d4b\u80fd\u91d1\u878d\u5b89\u5168\uff0c\u4ece\u6b64\u66f4\u5b89\u5fc3", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u5217\u8868", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_upload.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5206\u6790", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u70b9\u76d1\u6d4b", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u65e5\u5fd7", None))
        self.btn_para.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8c03\u6574", None))
        self.btn_information.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u6237\u8bbe\u7f6e", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5f55", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u4fe1\u606f", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u76fe\u00b7FraudShield - \u91d1\u878d\u6570\u636e\u6b3a\u8bc8\u68c0\u6d4b\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelBoxBlenderInstalation_7.setText(QCoreApplication.translate("MainWindow", u"\u4fbf\u6377\u67e5\u8be2", None))
        self.plainTextEdit_14.setPlainText("")
        self.plainTextEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5728\u6b64\u8f93\u5165\u9700\u8981\u67e5\u8be2\u7684\u65f6\u95f4\u6216\u767b\u5f55ID", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"\u6309\u65f6\u95f4\u67e5\u8be2", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"\u6309\u767b\u5f55ID\u67e5\u8be2", None))
        self.labelBoxBlenderInstalation_6.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u65e5\u5fd7\u6570\u636e", None))
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem25 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem26 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget_4.verticalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_4.verticalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_4.verticalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_4.verticalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_4.verticalHeaderItem(8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget_4.verticalHeaderItem(9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget_4.verticalHeaderItem(10)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget_4.verticalHeaderItem(11)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget_4.verticalHeaderItem(12)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget_4.verticalHeaderItem(13)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget_4.verticalHeaderItem(14)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.tableWidget_4.verticalHeaderItem(15)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        ___qtablewidgetitem43 = self.tableWidget_4.item(0, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem44 = self.tableWidget_4.item(0, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55ID", None));
        ___qtablewidgetitem45 = self.tableWidget_4.item(0, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u9009\u64cd\u4f5c", None));
        self.tableWidget_4.setSortingEnabled(__sortingEnabled1)

        self.labelBoxBlenderInstalation_10.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_11.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u6700\u65b0\u7248\u672c\uff1a", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_13.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6a21\u578b\u7248\u672c\uff1a", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_12.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u6700\u65b0\u7248\u672c\uff1a", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_15.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u53c2\u6570\u7248\u672c\uff1a", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_14.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u6700\u65b0\u7248\u672c\uff1a", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u8f6f\u4ef6\u66f4\u65b0", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u67b6\u6784\u66f4\u65b0", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u53c2\u6570\u66f4\u65b0", None))
        self.labelBoxBlenderInstalation_8.setText(QCoreApplication.translate("MainWindow", u"\u5927\u8bed\u8a00\u6a21\u578b\u53c2\u6570", None))
        self.labelBoxBlenderInstalation_16.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText("")
        self.labelBoxBlenderInstalation_17.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_18.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_19.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u53c2\u6570\u66f4\u65b0", None))
        self.labelBoxBlenderInstalation_9.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u878d\u6b3a\u8bc8\u8bc6\u522b\u6a21\u578b\u53c2\u6570", None))
        self.labelBoxBlenderInstalation_20.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_21.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_22.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_23.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u53c2\u6570\u66f4\u65b0", None))
        self.labelBoxBlenderInstalation_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u4fee\u6539\u4e2a\u4eba\u4fe1\u606f</span></p></body></html>", None))
        self.labelBoxBlenderInstalation_24.setText(QCoreApplication.translate("MainWindow", u"\u8054 \u7cfb \u7535 \u8bdd \uff1a", None))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_25.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u5458\u59d3\u540d\uff1a", None))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_26.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u5458\u90ae\u7bb1\uff1a", None))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_27.setText(QCoreApplication.translate("MainWindow", u"\u5355 \u4f4d \u540d \u79f0 \uff1a", None))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_28.setText(QCoreApplication.translate("MainWindow", u"\u5458 \u5de5 \u5de5 \u53f7 \uff1a", None))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelBoxBlenderInstalation_29.setText(QCoreApplication.translate("MainWindow", u"\u52a8 \u6001 \u5bc6 \u7801 \uff1a", None))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4e0a\u4f20", None))
        self.labelBoxBlenderInstalation_41.setText("")
        self.labelBoxBlenderInstalation_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u8d26\u6237\u4fee\u6539</span></p></body></html>", None))
        ___qtablewidgetitem46 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem47 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem48 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem49 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem50 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem51 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem52 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem53 = self.tableWidget_5.horizontalHeaderItem(7)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem54 = self.tableWidget_5.verticalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem55 = self.tableWidget_5.verticalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem56 = self.tableWidget_5.verticalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem57 = self.tableWidget_5.verticalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        ___qtablewidgetitem58 = self.tableWidget_5.item(0, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None));
        ___qtablewidgetitem59 = self.tableWidget_5.item(0, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem60 = self.tableWidget_5.item(0, 2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1", None));
        ___qtablewidgetitem61 = self.tableWidget_5.item(0, 3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\u540d\u79f0", None));
        ___qtablewidgetitem62 = self.tableWidget_5.item(0, 4)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u53f7", None));
        ___qtablewidgetitem63 = self.tableWidget_5.item(0, 5)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u7535\u8bdd", None));
        ___qtablewidgetitem64 = self.tableWidget_5.item(0, 6)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None));
        ___qtablewidgetitem65 = self.tableWidget_5.item(0, 7)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None));
        self.tableWidget_5.setSortingEnabled(__sortingEnabled2)

        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u5f85\u5206\u6790\u6570\u636e", None))
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5728\u6b64\u8f93\u5165\u5f85\u5206\u6790\u6570\u636e\u6216\u5728\u53f3\u4fa7\u4e0a\u4f20\u6587\u4ef6", None))
        self.labelVersion_5.setText(QCoreApplication.translate("MainWindow", u"\u652f\u6301\u4e0a\u4f20\u591a\u6a21\u6001\u7684\u6570\u636e\uff0c\u5305\u62ec\u6587\u5b57\u3001\u56fe\u7247\u3001\u6216\u6587\u4ef6", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u6587\u5b57", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u6587\u4ef6", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u4e0a\u4f20\u6570\u636e", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5df2\u4e0a\u4f20\u6587\u4ef6\u5217\u8868", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u4e0a\u4f20\u5b8c\u6210\u540e\u3001\u53ef\u4e8e\u53f3\u4fa7\u70b9\u51fb\u5f00\u59cb\u5206\u6790", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5206\u6790", None))
        self.labelBoxBlenderInstalation_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u64cd\u4f5c\u65e5\u5fd7\u5217\u8868</span></p></body></html>", None))
        ___qtablewidgetitem66 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem67 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem68 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem69 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem70 = self.tableWidget_6.verticalHeaderItem(0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem71 = self.tableWidget_6.verticalHeaderItem(1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem72 = self.tableWidget_6.verticalHeaderItem(2)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem73 = self.tableWidget_6.verticalHeaderItem(3)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem74 = self.tableWidget_6.verticalHeaderItem(4)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem75 = self.tableWidget_6.verticalHeaderItem(5)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem76 = self.tableWidget_6.verticalHeaderItem(6)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem77 = self.tableWidget_6.verticalHeaderItem(7)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem78 = self.tableWidget_6.verticalHeaderItem(8)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem79 = self.tableWidget_6.verticalHeaderItem(9)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem80 = self.tableWidget_6.verticalHeaderItem(10)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem81 = self.tableWidget_6.verticalHeaderItem(11)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem82 = self.tableWidget_6.verticalHeaderItem(12)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem83 = self.tableWidget_6.verticalHeaderItem(13)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem84 = self.tableWidget_6.verticalHeaderItem(14)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem85 = self.tableWidget_6.verticalHeaderItem(15)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.tableWidget_6.isSortingEnabled()
        self.tableWidget_6.setSortingEnabled(False)
        ___qtablewidgetitem86 = self.tableWidget_6.item(0, 0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem87 = self.tableWidget_6.item(0, 1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u8005id", None));
        ___qtablewidgetitem88 = self.tableWidget_6.item(0, 2)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8d26\u53f7", None));
        ___qtablewidgetitem89 = self.tableWidget_6.item(0, 3)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u65e5\u5fd7", None));
        self.tableWidget_6.setSortingEnabled(__sortingEnabled3)

        self.plainTextEdit_13.setPlainText("")
        self.plainTextEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5728\u6b64\u8f93\u5165\u9700\u8981\u64cd\u4f5c\u7684\u4ea4\u6613\u8d26\u6237", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5165\u91cd\u70b9\u5173\u6ce8", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u9664\u91cd\u70b9\u5173\u6ce8", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6b63\u5e38\u8ffd\u8e2a", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6df1\u5ea6\u8ffd\u8e2a", None))

        self.labelBoxBlenderInstalation_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u64cd\u4f5c\u8d26\u53f7</span></p></body></html>", None))
        ___qtablewidgetitem90 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem91 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem92 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem93 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem94 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem95 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem96 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem97 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem98 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem99 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem100 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem101 = self.tableWidget_3.verticalHeaderItem(10)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem102 = self.tableWidget_3.verticalHeaderItem(11)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem103 = self.tableWidget_3.verticalHeaderItem(12)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem104 = self.tableWidget_3.verticalHeaderItem(13)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem105 = self.tableWidget_3.verticalHeaderItem(14)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem106 = self.tableWidget_3.verticalHeaderItem(15)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled4 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem107 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u8d26\u53f7", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled4)

        self.labelBoxBlenderInstalation_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u4e91\u7aef\u91cd\u70b9\u5173\u6ce8\u8d26\u53f7</span></p></body></html>", None))
        ___qtablewidgetitem108 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem109 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem110 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem111 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem112 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem113 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem114 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem115 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem116 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem117 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem118 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem119 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem120 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem121 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem122 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem123 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem124 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled5 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem125 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u8d26\u53f7", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled5)

        self.btn_themechange.setText(QCoreApplication.translate("MainWindow", u"\u6539\u53d8\u4e3b\u9898", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u9000\u51fa", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2025 \u91d1\u76fe FraudShield \u9879\u76ee\u7ec4 \u7248\u6743\u6240\u6709\uff0c\u4ec5\u7528\u4e8e\u777f\u6297\u673a\u5668\u4eba\u5f00\u53d1\u8005\u5927\u8d5b\u5c55\u793a\u4e0e\u8bc4\u5ba1", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u6237\u7ea7\u522b\uff1a\u7ba1\u7406\u5458\u8d26\u6237", None))
        self.version_2.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**\u91d1\u76feFraudShied**\n"
"\n"
"\u91d1\u76fe\u00b7FraudShield \u662f\u4e00\u6b3e\u9762\u5411\u91d1\u878d\u9886\u57df\u7684\u6570\u636e\u6b3a\u8bc8\u68c0\u6d4b\u7cfb\u7edf\uff0c\u65e8\u5728\u901a\u8fc7\u591a\u6a21\u6001\u6570\u636e\u878d\u5408\u4e0e\u667a\u80fd\u7b97\u6cd5\u5206\u6790\uff0c\u4e3a\u7528\u6237\u63d0\u4f9b\u9ad8\u6548\u3001\u51c6\u786e\u7684\u53cd\u6b3a\u8bc8\u89e3\u51b3\u65b9\u6848\u3002\n"
"\n"
"**\u514d\u8d23\u58f0\u660e**\n"
"\n"
"\u672c\u8f6f\u4ef6\u4e3a\u975e\u5546\u4e1a\u6027\u7814\u7a76\u539f\u578b\uff0c\u5904\u7406\u6570\u636e\u4ec5\u7528\u4e8e\u5c55\u793a\u4e0e\u6d4b\u8bd5\u3002\u8f6f\u4ef6\u4e2d\u6240\u6d89\u53ca\u7684\u91d1\u878d\u5206\u6790\u3001\u6a21\u578b\u8f93\u51fa\u53ca\u53ef\u89c6\u5316\u7ed3\u679c\u4e0d\u6784\u6210\u4efb\u4f55\u6295\u8d44\u5efa\u8bae\u6216\u771f\u5b9e\u98ce\u9669\u5224\u65ad\uff0c\u4f7f\u7528\u8005\u9700\u81ea\u884c\u627f\u62c5\u76f8\u5173\u8d23\u4efb\u3002\n"
"\n"
"**\u7248\u6743\u58f0\u660e**\n"
"\n"
"\u672c\u8f6f\u4ef6\u201c\u91d1\u76fe FraudShield\u201d"
                        "\u7531\u91d1\u76fe\u9879\u76ee\u7ec4\u5f00\u53d1\uff0c\u4ec5\u7528\u4e8e**\u777f\u6297\u673a\u5668\u4eba\u5f00\u53d1\u8005\u5927\u8d5b**\n"
"\u53c2\u8d5b\u53ca\u5c55\u793a\u76ee\u7684\u3002\u6240\u6709\u6e90\u4ee3\u7801\u3001\u754c\u9762\u8bbe\u8ba1\u3001\u6570\u636e\u5904\u7406\u6a21\u578b\u3001\u7b97\u6cd5\u7ed3\u6784\u53ca\u5176\u6587\u6863\u8d44\u6599\u5747\u5f52\u91d1\u76fe\u9879\u76ee\u7ec4\u6240\u6709\uff0c\u53d7\u300a\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u8457\u4f5c\u6743\u6cd5\u300b\u53ca\u76f8\u5173\u6cd5\u5f8b\u6cd5\u89c4\u4fdd\u62a4\u3002\n"
"\n"
"\n"
"\u672a\u7ecf\u8bb8\u53ef\uff0c\u4efb\u4f55\u5355\u4f4d\u6216\u4e2a\u4eba\u4e0d\u5f97\u4ee5\u4efb\u4f55\u5f62\u5f0f\u590d\u5236\u3001\u4f20\u64ad\u3001\u4fee\u6539\u3001\u53d1\u5e03\u3001\u5546\u7528\u6216\u4ee5\u5176\u5b83\u65b9\u5f0f\u4f7f\u7528\u672c\u8f6f\u4ef6\u7684\u5168\u90e8\u6216\u90e8\u5206\u5185\u5bb9\u3002\u82e5\u9700\u4f7f\u7528\u6216\u5f15\u7528\u672c\u8f6f\u4ef6\u4e2d\u7684\u76f8\u5173\u6210\u679c\uff0c\u987b\u83b7\u5f97\u672c\u9879"
                        "\u76ee\u7ec4\u660e\u786e\u4e66\u9762\u6388\u6743\u3002\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u91d1\u76feFraudShied</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u91d1\u76fe\u00b7FraudShield \u662f\u4e00\u6b3e\u9762\u5411\u91d1\u878d\u9886\u57df\u7684\u6570\u636e\u6b3a\u8bc8\u68c0\u6d4b\u7cfb\u7edf\uff0c\u65e8\u5728\u901a\u8fc7\u591a\u6a21\u6001\u6570\u636e\u878d\u5408\u4e0e\u667a\u80fd\u7b97\u6cd5\u5206\u6790\uff0c\u4e3a\u7528\u6237\u63d0\u4f9b\u9ad8\u6548\u3001\u51c6\u786e\u7684\u53cd\u6b3a\u8bc8\u89e3\u51b3\u65b9\u6848\u3002</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u514d\u8d23\u58f0\u660e</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u672c\u8f6f\u4ef6\u4e3a\u975e\u5546\u4e1a\u6027\u7814\u7a76\u539f\u578b\uff0c\u5904\u7406\u6570\u636e\u4ec5\u7528\u4e8e\u5c55\u793a\u4e0e"
                        "\u6d4b\u8bd5\u3002\u8f6f\u4ef6\u4e2d\u6240\u6d89\u53ca\u7684\u91d1\u878d\u5206\u6790\u3001\u6a21\u578b\u8f93\u51fa\u53ca\u53ef\u89c6\u5316\u7ed3\u679c\u4e0d\u6784\u6210\u4efb\u4f55\u6295\u8d44\u5efa\u8bae\u6216\u771f\u5b9e\u98ce\u9669\u5224\u65ad\uff0c\u4f7f\u7528\u8005\u9700\u81ea\u884c\u627f\u62c5\u76f8\u5173\u8d23\u4efb\u3002</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u7248\u6743\u58f0\u660e</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u672c\u8f6f\u4ef6\u201c\u91d1\u76fe FraudShield\u201d\u7531\u91d1\u76fe\u9879\u76ee\u7ec4\u5f00\u53d1\uff0c\u4ec5\u7528\u4e8e</span><span style=\" font-size:9pt; font-weight:700; color:#ffffff;\">\u777f\u6297\u673a\u5668\u4eba\u5f00\u53d1\u8005\u5927"
                        "\u8d5b</span><span style=\" font-size:9pt; color:#ffffff;\">\u53c2\u8d5b\u53ca\u5c55\u793a\u76ee\u7684\u3002\u6240\u6709\u6e90\u4ee3\u7801\u3001\u754c\u9762\u8bbe\u8ba1\u3001\u6570\u636e\u5904\u7406\u6a21\u578b\u3001\u7b97\u6cd5\u7ed3\u6784\u53ca\u5176\u6587\u6863\u8d44\u6599\u5747\u5f52\u91d1\u76fe\u9879\u76ee\u7ec4\u6240\u6709\uff0c\u53d7\u300a\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u8457\u4f5c\u6743\u6cd5\u300b\u53ca\u76f8\u5173\u6cd5\u5f8b\u6cd5\u89c4\u4fdd\u62a4</span><span style=\" color:#ffffff;\">\u3002</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u672a\u7ecf\u8bb8\u53ef\uff0c\u4efb\u4f55\u5355\u4f4d\u6216\u4e2a\u4eba\u4e0d\u5f97\u4ee5\u4efb\u4f55\u5f62\u5f0f\u590d\u5236\u3001\u4f20\u64ad\u3001\u4fee\u6539\u3001\u53d1\u5e03\u3001\u5546\u7528\u6216\u4ee5\u5176\u5b83\u65b9\u5f0f\u4f7f\u7528\u672c\u8f6f\u4ef6\u7684\u5168\u90e8\u6216\u90e8\u5206\u5185"
                        "\u5bb9\u3002\u82e5\u9700\u4f7f\u7528\u6216\u5f15\u7528\u672c\u8f6f\u4ef6\u4e2d\u7684\u76f8\u5173\u6210\u679c\uff0c\u987b\u83b7\u5f97\u672c\u9879\u76ee\u7ec4\u660e\u786e\u4e66\u9762\u6388\u6743\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi


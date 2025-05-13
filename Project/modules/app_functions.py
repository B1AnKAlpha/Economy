# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    def setThemeHack(self,target=1):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        if target==1:
            print("1")
            self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
            self.ui.lineEdit_2.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_2.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_3.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_4.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_5.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_7.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_8.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_9.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_38.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_39.setStyleSheet("background-color: #6272a4;")
            self.ui.pushButton_42.setStyleSheet("background-color: #6272a4;")
            self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
            self.ui.plainTextEdit_2.setStyleSheet("background-color: #6272a4;")
            self.ui.plainTextEdit_13.setStyleSheet("background-color: #363f5c;")
            self.ui.tableWidget_2.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.tableWidget_3.setStyleSheet(
                "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.tableWidget.setStyleSheet(
                "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
            self.ui.comboBox_2.setStyleSheet("background-color: #363f5c;")
            self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
            self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
            self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")
            '''
            self.ui.tableWidget_2.setStyleSheet("""
                QHeaderView::section {
                    color: black;
                    background-color: lightgray;
                    font-weight: bold;
                }
            """)
            self.ui.tableWidget_3.setStyleSheet("""
                QHeaderView::section {
                    color: black;
                    background-color: lightgray;
                    font-weight: bold;
                }
            """)
            '''
        else:
            self.ui.lineEdit.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.pushButton.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.pushButton_2.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.pushButton_3.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.pushButton_4.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.pushButton_5.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.pushButton_7.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.pushButton_8.setStyleSheet("background-color: rgb(33, 37, 43)4;")
            self.ui.pushButton_9.setStyleSheet("background-color: rgb(33, 37, 43)4;")
            self.ui.pushButton_38.setStyleSheet("background-color: rgb(33, 37, 43)4;")
            self.ui.pushButton_9.setStyleSheet("background-color: rgb(33, 37, 43)4;")
            self.ui.pushButton_39.setStyleSheet("background-color: rgb(33, 37, 43)4;")
            self.ui.pushButton_42.setStyleSheet("background-color: rgb(33, 37, 43)4;")
            self.ui.plainTextEdit.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.plainTextEdit_2.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.plainTextEdit_13.setStyleSheet("background-color: rgb(33, 37, 43);")
            '''
            self.ui.tableWidget_2.setStyleSheet("""
                QHeaderView::section {
                    color: black;
                    background-color: lightgray;
                    font-weight: bold;
                }
            """)
            self.ui.tableWidget_3.setStyleSheet("""
                QHeaderView::section {
                    color: black;
                    background-color: lightgray;
                    font-weight: bold;
                }
            """)
            '''
            self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: rgb(33, 37, 43); } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.tableWidget_2.setStyleSheet(
                "QScrollBar:vertical { background: rgb(33, 37, 43); } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.tableWidget_3.setStyleSheet(
                "QScrollBar:vertical { background: rgb(33, 37, 43); } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: rgb(33, 37, 43); } QScrollBar:horizontal { background: #6272a4; }")
            self.ui.comboBox.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.comboBox_2.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.horizontalScrollBar.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.verticalScrollBar.setStyleSheet("background-color: rgb(33, 37, 43);")
            self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

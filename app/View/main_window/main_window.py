from common import resource
from common.setting import APP_NAME, VERSION
from .ui_main import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QWidget, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QFrame, QCheckBox
from PyQt5.QtGui import QFont, QIcon


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.file_name = ""
        self.total_num = 0
        self.used_num = 0
        self.status_bar = QStatusBar()
        self.setupUi(self)
        self.ui_init()
        self.setWindowTitle(f"{APP_NAME} {VERSION}")
        self.setWindowIcon(QIcon(":/images/logo/logo.ico"))
        self.setStatusBar(self.status_bar)

    def ui_init(self):
        print("ui_init")
        # self.le_encry_refresh()
        font = QFont("微软雅黑", 10)
        font.setBold(True)

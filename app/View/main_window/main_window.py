# coding:utf-8
import sys

from common import resource
from common.setting import APP_NAME
from common.style_sheet import setStyleSheet

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QMainWindow

from qframelesswindow import FramelessWindow, AcrylicWindow
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge)
from qfluentwidgets import FluentIcon as FIF

from View.page01 import Page01Test
from View.page02 import Page02Test
from View.setting_interface import SettingInterface

from .ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        # create sub interface
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        self.resize(1600, 1200)
        self.setWindowIcon(QIcon(':/images/logo/logo.png'))
        self.setWindowTitle(APP_NAME)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def initWidget(self):
        self.setQss()

    def setQss(self):
        setStyleSheet(self, 'main_window')

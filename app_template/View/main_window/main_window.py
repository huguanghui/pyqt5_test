# coding:utf-8
import sys

import resource_rc
from common.config import config
from common.setting import APP_NAME, RELEASE_URL
from common.style_sheet import setStyleSheet
# from common.version_manager import VersionManager
# from components.dialog_box.dialog import Dialog

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow

from View.setting_interface import SettingInterface
from View.update import CheckUpdate

from .ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        self.resize(800, 600)
        self.setWindowIcon(QIcon(':/images/logo/logo.png'))
        self.setWindowTitle(APP_NAME)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def initWidget(self):
        self.setQss()
        self.connectSignalToSlot()
        self.onInitFinished()

    def onInitFinished(self):
        """ initialize finished slot """
        pass

    def setQss(self):
        setStyleSheet(self, 'main_window')

    def connectSignalToSlot(self):
        """ connect signal to slot """

        self.actionVersion.triggered.connect(self.add_checkupdate_window)
        self.actionHelp.triggered.connect(self.helpDoc)

    def helpDoc(self):
        print('Help')
        QDesktopServices.openUrl(QUrl.fromLocalFile("Readme.html"))

    def add_checkupdate_window(self):
        sub_win = CheckUpdate(parent=self)
        sub_win.show()

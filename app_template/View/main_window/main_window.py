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
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
)

from View.setting_interface import SettingInterface
from View.update import CheckUpdate
from View.tool import ToolDemo

from .ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        self.resize(800, 600)
        self.setWindowIcon(QIcon(":/images/logo/logo.png"))
        self.setWindowTitle(APP_NAME)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.sub_windows = list()

    def initWidget(self):
        self.setQss()
        self.connectSignalToSlot()
        self.onInitFinished()

    def onInitFinished(self):
        """initialize finished slot"""
        pass

    def setQss(self):
        setStyleSheet(self, "main_window")

    def connectSignalToSlot(self):
        """connect signal to slot"""
        self.subwindow_function = {
            "ToolDemo": [self.actionDemo, ToolDemo],
        }

        self.actionVersion.triggered.connect(self.add_checkupdate_window)
        self.actionHelp.triggered.connect(self.helpDoc)

        for key, value in self.subwindow_function.items():
            value[0].triggered.connect(
                lambda win_name=key, win_object=value[1]: self.add_sub_window(
                    win_name, win_object
                )
            )

    def add_sub_window(self, name, win_object):
        sub_window = win_object(parent=self)
        self.mdiArea.addSubWindow(sub_window)
        self.sub_windows.append(sub_window)
        sub_window.show()

    def helpDoc(self):
        print("Help")
        QDesktopServices.openUrl(QUrl.fromLocalFile("Readme.html"))

    def add_checkupdate_window(self):
        sub_win = CheckUpdate(parent=self)
        sub_win.show()

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        msgBox = QMessageBox()
        msgBox.setWindowFlags(msgBox.windowFlags() | Qt.WindowStaysOnTopHint)
        msgBox.setWindowFlags(msgBox.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
        msgBox.setWindowTitle("ImageTools")
        msgBox.setText("是否要退出程序？")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("是")
        msgBox.button(QMessageBox.No).setText("否")
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

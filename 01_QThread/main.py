#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

if hasattr(sys, "frozen"):
    os.environ["PATH"] = sys._MEIPASS + ";" + os.environ["PATH"]

from GUI.Ui_Main import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStatusBar


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.status_bar = QStatusBar()
        self.setupUi(self)
        self.ui_init()
        self.setWindowTitle("Test V1.0.0")
        # self.setWindowIcon(QIcon(":/app.ico"))
        self.setStatusBar(self.status_bar)

    def ui_init(self):
        print("ui_init")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = MainWindow()
    loginWindow.show()
    sys.exit(app.exec_())

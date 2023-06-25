#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time

if hasattr(sys, "frozen"):
    os.environ["PATH"] = sys._MEIPASS + ";" + os.environ["PATH"]

from GUI.Ui_Main import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStatusBar
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QMutex

qmut_1 = QMutex()
# qmut_2 = QMutex()


class Thread_1(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        qmut_1.lock()
        values = [1, 2, 3, 4, 5]
        for i in values:
            print(i)
            time.sleep(0.5)
        qmut_1.unlock()


class Thread_2(QThread):
    _signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        # qmut_2.lock()
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            time.sleep(0.5)
        # qmut_2.unlock()
        self._signal.emit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.status_bar = QStatusBar()
        self.setupUi(self)
        self.ui_init()
        self.setWindowTitle("Test V1.0.0")
        # self.setWindowIcon(QIcon(":/app.ico"))
        self.setStatusBar(self.status_bar)
        self.pb_1.clicked.connect(self.click_1)
        self.pb_2.clicked.connect(self.click_2)

    def ui_init(self):
        print("ui_init")

    def click_1(self):
        self.thread_1 = Thread_1()
        self.thread_1.start()

    def click_2(self):
        self.pb_2.setEnabled(False)
        self.thread_2 = Thread_2()
        self.thread_2._signal.connect(self.set_btn)
        self.thread_2.start()

    def set_btn(self):
        self.pb_2.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = MainWindow()
    loginWindow.show()
    sys.exit(app.exec_())

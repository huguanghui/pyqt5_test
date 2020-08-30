#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: tool.py
# @描述: 实现IPC常用工具
# @日期: 2020/01/16

import os
import time
import sys
# 引入 PyQt5.QtWidgetes 模块
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI import Ui_Main
from GUI import Ui_unpack

class MainWindow(object):
	def __init__(self):
		app = QtWidgets.QApplication(sys.argv)
		MainWin = QtWidgets.QMainWindow()
		self.ui = Ui_Main.Ui_MainWindow()
		self.ui.setupUi(MainWin)
		self.ui_init()

		MainWin.setWindowTitle('HghTool')
		MainWin.show()
		sys.exit(app.exec_())
	
	def ui_init(self):
		pass

if __name__ == "__main__":
	MainWindow()
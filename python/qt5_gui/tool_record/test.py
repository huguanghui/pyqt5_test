#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 实现一个计算码率和录像时长的工具
# @创建者: huguanghui
# @日期: 2019/10/23

from GUI import Ui_Main
from PyQt5 import QtCore, QtWidgets, QtGui
import time

class MainWindow(object):
	def __init__(self):
		import sys
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		self.ui = Ui_Main.Ui_MainWindow()
		self.ui.setupUi(MainWindow)
		self.ui_init()

		MainWindow.show()
		sys.exit(app.exec_())
	
	def ui_init(self):
		self.ui.lineEdit.setText(str(int(1)))
		self.ui.pushButton.clicked.connect(self.genPushButton)

	def genPushButton(self):
		lt = self.ui.lineEdit.text()
		# TF_capacity = 23792*1024
		TF_capacity = (30240-1024)*1024
		seg_len = 13800
		bitrate = seg_len/float(lt)*8
		self.ui.lineEdit_3.setText(str(int(bitrate)))
		time = TF_capacity/((seg_len/float(lt))*3600)
		self.ui.lineEdit_2.setText(str(int(time)))

if __name__ == "__main__":
	MainWindow()
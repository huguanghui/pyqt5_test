#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 基于Pyqt5使用QSS技巧
# @创建者: huguanghui
# @日期: 2019/10/23

from GUI import Ui_Hello
from PyQt5 import QtCore, QtWidgets, QtGui
import time

class RunThread(QtCore.QThread):
	counter_value = QtCore.pyqtSignal(int)

	def __init__(self, parent=None, counter_start=0):
		super(RunThread, self).__init__(parent)
		self.counter = counter_start
		self.is_running = True
	
	def run(self):
		while self.counter < 100 and self.is_running == True:
			time.sleep(0.1)
			self.counter += 1
			print(self.counter)
			self.counter_value.emit(self.counter)

	def stop(self):
		self.is_running = False
		print('线程停止中...')
		self.terminate()

class MainWindow(object):
	def __init__(self):
		import sys
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QWidget()
		self.ui = Ui_Hello.Ui_Form()
		self.ui.setupUi(MainWindow)
		MainWindow.setWindowOpacity(0.9)
		# MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.ui_init()

		MainWindow.show()
		sys.exit(app.exec_())

	def ui_init(self):
		pass

if __name__ == "__main__":
	MainWindow()
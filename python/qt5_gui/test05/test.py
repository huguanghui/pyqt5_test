#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 基于Pyqt5创建复杂的GUI
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

class DragDropButton(QtWidgets.QPushButton):
	def __init__(self, text, parent):
		super().__init__(text, parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat('text/plain'):
			event.accept()
		else:
			event.ignore()
	
	def dropEvent(self, event):
		self.setText(event.mimeData().text())

class MainWindow(object):
	def __init__(self):
		import sys
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		self.ui = Ui_Hello.Ui_MainWindow()
		self.ui.setupUi(MainWindow)

		self.ui.pushButton.hide()
		self.pushButton = DragDropButton("拖放按钮", MainWindow)
		self.ui.gridLayout.addWidget(self.pushButton, 0, 1, 1, 2)

		MainWindow.show()
		sys.exit(app.exec_())

if __name__ == "__main__":
	MainWindow()
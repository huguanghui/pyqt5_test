#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test02.py
# @描述: 基于Pyqt5实现对话框跳转
# @创建者: huguanghui
# @日期: 2019/10/23

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QFileDialog
import sys
from Ui_main import Ui_MainWindow
from Ui_dialog import Ui_Dialog as Ui_Echo

class dialog_echo(QDialog, Ui_Echo):
	def __init__(self):
		super(dialog_echo, self).__init__()
		self.setupUi(self)

class mywindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.click_button)

	def click_button(self):
		form = dialog_echo()
		form.show()
		rsp = form.exec_()
		if rsp == QDialog.Accepted:
			self.label.setText('点击了OK')
		else:
			self.label.setText('点击了Cannel')
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = mywindow()
	window.show()
	sys.exit(app.exec_())
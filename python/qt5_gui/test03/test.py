#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 基于Pyqt5解耦逻辑
# @创建者: huguanghui
# @日期: 2019/10/23

from GUI import Ui_Hello
from PyQt5 import QtCore, QtWidgets, QtGui

def button_clicked():
	ui.pushButton.setText('按钮被点击')
	set_table_item(item2='数据2被改变')

def set_table_item(item1='数据1', item2='数据2', item3='数据3'):
	ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(item1))
	ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(item2))
	ui.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(item3))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_Hello.Ui_MainWindow()
	ui.setupUi(MainWindow)

	set_table_item()
	ui.pushButton.clicked.connect(button_clicked)

	MainWindow.show()
	sys.exit(app.exec_())
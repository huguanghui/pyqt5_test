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

class MainWindow(object):
	def __init__(self):
		import sys
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		self.ui = Ui_Hello.Ui_MainWindow()
		self.ui.setupUi(MainWindow)

		self.update_date()
		self.update_calendar()
		
		self.set_led()
		self.set_dial()

		# self.zero_progress()
		# self.click_radio3()

		self.update_progressbar()

		self.set_font()

		MainWindow.show()
		sys.exit(app.exec_())

	# 修改日期修改器数值
	def update_date(self):
		self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

	# 设置日历信号槽
	def update_calendar(self):
		self.ui.calendarWidget.selectionChanged.connect(self.update_date)

	# 修改LED显示器数字
	def set_led(self):
		self.ui.lcdNumber.display(self.ui.dial.value())

	# 设置刻度盘信号槽
	def set_dial(self):
		self.ui.dial.valueChanged['int'].connect(self.set_led)

	# 重置进度条
	def zero_progress(self):
		self.ui.radioButton_2.clicked.connect(self.ui.progressBar.reset)

	# 更新进度条
	def update_progress(self):
		value = self.ui.lcdNumber.value()
		self.ui.progressBar.setValue(value)
	
	# 点击按钮3
	def click_radio3(self):
		self.ui.radioButton_3.clicked.connect(self.update_progress)

	# 刷新字体显示
	def set_font(self):
		self.ui.fontComboBox.activated['QString'].connect(self.ui.label.setText)

	# 按钮信号槽配置
	def update_progressbar(self):
		self.ui.radioButton.clicked.connect(self.start_progressbar)
		self.ui.radioButton_2.clicked.connect(self.stop_progressbar)
		self.ui.radioButton_3.clicked.connect(self.reset_progressbar)
		self.progress_value = 0
		self.stop_progress = False

	# 启动进度条
	def start_progressbar(self):
		self.stop_progress = False
		self.progress_value = self.ui.progressBar.value()
		self.progressbar_counter(self.progress_value)

	# 停止进度条
	def stop_progressbar(self):
		self.stop_progress = True
		try:
			self.run_thread.stop()
		except:
			pass

	# 重设进度条
	def reset_progressbar(self):
		self.progress_value = 0
		self.ui.progressBar.reset()
		self.stop_progress = False

	def progressbar_counter(self, start_value=0):
		self.run_thread = RunThread(parent=None, counter_start=start_value)
		self.run_thread.start()
		self.run_thread.counter_value.connect(self.set_progressbar)

	def set_progressbar(self, counter):
		if not self.stop_progress:
			self.ui.progressBar.setValue(counter)

if __name__ == "__main__":
	MainWindow()
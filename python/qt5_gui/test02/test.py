#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 基于Pyqt5实现显示CPU实时状态的图形界面
# @创建者: huguanghui
# @日期: 2019/10/23

from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import pyqtgraph as pg
import traceback
import psutil

class MainUi(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('CPU使用率监控')
		# 创建主控件
		self.main_widget = QtWidgets.QWidget()  
		# 创建一个网格布局
		self.main_layout = QtWidgets.QGridLayout()
		# 设置主控件的布局为网格
		self.main_widget.setLayout(self.main_layout)
		# 设置窗口默认部件
		self.setCentralWidget(self.main_widget)
		# 实例化一个widget部件作为K线图
		self.plot_widget = QtWidgets.QWidget()
		# 实例化一个网格布局层
		self.plot_layout = QtWidgets.QGridLayout()
		# 设置plot部件的布局为网格
		self.plot_widget.setLayout(self.plot_layout)
		# 实例化一个绘图部件
		self.plot_plt = pg.PlotWidget()
		# 显示图形栅格
		self.plot_plt.showGrid(x=True,y=True)
		# 添加绘图布局到plot部件的网格布局层中
		self.plot_layout.addWidget(self.plot_plt)
		# 将上述布局添加到主控件的布局层中
		self.main_layout.addWidget(self.plot_widget, 1, 0, 3, 3)
		self.setCentralWidget(self.main_widget)
		self.plot_plt.setYRange(max=100, min=0)
		self.plot_plt.setMouseEnabled(x=True,y=False)
		self.data_list = []
		self.timer_start()

	def timer_start(self):
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.get_cpu_info)
		self.timer.start(1000)

	def get_cpu_info(self):
		try:
			cpu = "%0.2f" % psutil.cpu_percent(interval=1)
			self.data_list.append(float(cpu))
			print(float(cpu))
			self.plot_plt.plot().setData(self.data_list, pen='g')
		except Exception as e:
			print(traceback.print_exc())

def main():
	app = QtWidgets.QApplication(sys.argv)
	gui = MainUi()
	gui.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
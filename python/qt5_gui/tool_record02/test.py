#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 根据时间段计算录像的平均码率的工具
# @创建者: huguanghui
# @日期: 2019/10/23

import os
import sys
import yaml
import requests
import xlwt
from lxml import etree
from GUI import Ui_Main
from PyQt5 import QtCore, QtWidgets, QtGui
import time

config_path = os.path.join(os.path.dirname(__file__), 'config.yml')


with open(config_path) as f:
	cont = f.read()

cf = yaml.load(cont, Loader=yaml.FullLoader)

def save_yaml():
	with open(config_path, "w") as f:
		yaml.dump(cf, f)

wb = xlwt.Workbook()
ws = wb.add_sheet("A Test Sheet")

headers = {
  'Authorization': 'Basic YWRtaW46',
  'Content-Type': 'application/xml'
}

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
		self.ui.dateTimeEdit.setDate(QtCore.QDate.currentDate())
		self.ui.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
		tr_ipaddr = cf.get('IP')
		if tr_ipaddr != None:
			self.ui.lineEdit.setText(str(tr_ipaddr))
			self.ui.pushButton.clicked.connect(self.genPushButton)

	def searchRecord(self, ip, starttime, endtime):
		print(ip, starttime, endtime)
		url = 'http://' + ip + '/RecordFileList/Attribute'
		# 设置查询参数 PUT
		payload = "<?xml version='1.0' encoding='UTF-8' ?>\r\n<RecordFileListAttribute Version='1.0'>\r\n    <begin_time>%s</begin_time>\r\n    <end_time>%s</end_time>\r\n    <timezone_min_between_utc>480</timezone_min_between_utc>\r\n    <RecordFileSumCount>0</RecordFileSumCount>\r\n    <RecordFileCountPerPage>50</RecordFileCountPerPage>\r\n</RecordFileListAttribute>" % (starttime, endtime)
		response = requests.put(url, headers=headers, data=payload.encode("utf-8"))
		# print(response.text.encode('utf8'))
		# 查询录像信息 GET
		response = requests.get(url, headers=headers)
		recordlists = etree.XML(response.text.encode('utf8'))
		sum_count = int(recordlists.xpath("//RecordFileListAttribute/RecordFileSumCount")[0].text)
		sigle_page_num = int(recordlists.xpath("//RecordFileListAttribute/RecordFileCountPerPage")[0].text)
		page_nums = int(sum_count/sigle_page_num) + 1
		print(sum_count)
		self.ui.lineEdit_3.setText(str(sum_count))
		print(sigle_page_num)
		print(page_nums)
		# print(etree.tostring(recordlists))
		sum_a = 0
		for page_idx in range(page_nums):
			# 数据获取 (片段大小, 时间间隔)
			url = 'http://'+ ip + '/RecordFileList/Pages/%d' % (page_idx+1)
			response = requests.get(url, headers=headers)
			seg_lists = etree.XML(response.text.encode('utf8'))
			seg_info = seg_lists.xpath("//RecordFileList/RecordFile")
			seg_len = len(seg_info)
			for seg_idx in range(seg_len):
				ws_idx = sum_count - (sum_a+seg_idx)
				ws.write(ws_idx, 0 , ws_idx)
				start_time = time.strptime(seg_info[seg_idx].xpath("//RecordFile/StartTime")[seg_idx].text, "%Y%m%d %H:%M:%S")
				stop_time = time.strptime(seg_info[seg_idx].xpath("//RecordFile/StopTime")[seg_idx].text, "%Y%m%d %H:%M:%S")
				start_stamp = int(time.mktime(start_time))
				stop_stamp = int(time.mktime(stop_time))
				keeping_stamp = stop_stamp - start_stamp
				ws.write(ws_idx, 1, seg_info[seg_idx].xpath("//RecordFile/StartTime")[seg_idx].text)
				ws.write(ws_idx, 2, seg_info[seg_idx].xpath("//RecordFile/StopTime")[seg_idx].text)
				file_size = int(seg_info[seg_idx].xpath("//RecordFile/FileSize")[seg_idx].text)
				ws.write(ws_idx, 3, int(int(file_size/1024)))
				ws.write(ws_idx, 4, int(keeping_stamp))
				bitrate_avr =  int((file_size*8)/(keeping_stamp*1024))
				ws.write(ws_idx, 5, int(bitrate_avr))
			sum_a += seg_len
			print(seg_len)
			# print(response.text.encode('utf8'))
		print(sum_a)

	def genPushButton(self):
		g_IP = self.ui.lineEdit.text()
		g_time_begin = self.ui.dateTimeEdit.dateTime().toString("yyyyMMdd hhmmss")
		g_time_end = self.ui.dateTimeEdit_2.dateTime().toString("yyyyMMdd hhmmss")
		cf['IP'] = g_IP
		save_yaml()
		
		ws.write(0, 0, '编号')
		ws.write(0, 1, '开始时间')
		ws.write(0, 2, '结束时间')
		ws.write(0, 3, '大小(Kb)')
		ws.write(0, 4, '持续时间(s)')
		ws.write(0, 5, '平均帧率(KBps')
		self.searchRecord(g_IP, g_time_begin, g_time_end)
		wb.save('exp.xls')

if __name__ == "__main__":
	MainWindow()
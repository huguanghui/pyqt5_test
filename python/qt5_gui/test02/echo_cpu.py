#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: echo_cpu.py
# @创建者: huguanghui
# @日期: 2019/10/23

import psutil
import time

def get_cpu_info():
	cpu = "CPU:%0.2f" % psutil.cpu_percent(interval=1) + "%"
	return cpu

def main():
	while True:
		info = get_cpu_info()
		print(info)
		time.sleep(1)

if __name__ == "__main__":
	main()

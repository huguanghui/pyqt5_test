#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 巩固PyQt的页面布局
# @创建者: huguanghui
# @日期: 2020/08/29

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GUI import Ui_Main
from GUI import Ui_tab_1 

styleFile = os.path.join(os.path.dirname(__file__), 'style.css')
langCN = os.path.join(os.path.dirname(__file__), 'languages/lang_cn')
langEN = os.path.join(os.path.dirname(__file__), 'languages/lang_en')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initGui()
        self.loadStyleSheet()
        
    def initGui(self):
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.tb = Ui_tab_1.Ui_Form()
        self.tb.setupUi(self.ui.tab)
        self.initTab1()
        self.show()

    def loadStyleSheet(self):
        global styleFile
        try:
            with open(styleFile, 'r', encoding='utf-8') as style:
                self.setStyleSheet(style.read())
        except:
            with open(styleFile, 'r', encoding='gbk') as style:
                self.setStyleSheet(style.read())

    def initTab1(self):
        self.sim = QStandardItemModel()
        self.sim.appendRow(QStandardItem("Item1"))
        self.sim.appendRow(QStandardItem("Item2"))
        self.sim.appendRow(QStandardItem("Item3"))
        self.sim.appendRow(QStandardItem("Item4"))
        self.tb.listView.setModel(self.sim)
        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['序号', '姓名', '年龄', '地址'])
        for row in range(4):
            for column in range(4):
                i = QStandardItem(" row %s, column %s"%(row, column))
                self.model.setItem(row, column, i)
        self.tb.tableView.setModel(self.model)
        self.tb.pushButton.clicked.connect(self.addList)
        self.tb.pushButton_3.clicked.connect(self.addTabView)
        self.tb.pushButton_2.clicked.connect(self.delTabView)

    def addList(self):
        self.sim.appendRow(QStandardItem("item5"))

    def addTabView(self):
        self.model.appendRow([
            QStandardItem(" row %s, column %s"%(11, 11)),
            QStandardItem(" row %s, column %s"%(11, 11)),
            QStandardItem(" row %s, column %s"%(11, 11)),
            QStandardItem(" row %s, column %s"%(11, 11))
        ])

    def delTabView(self):
        r = self.tb.tableView.selectionModel().selectedRows()
        print(r)
        if r:
            index = self.tb.tableView.currentIndex()
            # print(index.row())
            self.model.removeRow(index.row())

def main():
    global app, translator, mainWindow
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load(langCN)
    app.installTranslator(translator)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
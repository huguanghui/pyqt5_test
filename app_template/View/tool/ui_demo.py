# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/tool/demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Demo(object):
    def setupUi(self, Demo):
        Demo.setObjectName("Demo")
        Demo.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Demo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        Demo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Demo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Demo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Demo)
        self.statusbar.setObjectName("statusbar")
        Demo.setStatusBar(self.statusbar)

        self.retranslateUi(Demo)
        QtCore.QMetaObject.connectSlotsByName(Demo)

    def retranslateUi(self, Demo):
        _translate = QtCore.QCoreApplication.translate
        Demo.setWindowTitle(_translate("Demo", "Demo"))
        self.pushButton.setText(_translate("Demo", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Demo = QtWidgets.QMainWindow()
    ui = Ui_Demo()
    ui.setupUi(Demo)
    Demo.show()
    sys.exit(app.exec_())

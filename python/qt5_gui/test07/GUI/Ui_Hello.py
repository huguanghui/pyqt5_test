# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\GIT\AIGame\python\qt5_gui\test07\GUI\Hello.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 700)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.right_widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_widget.sizePolicy().hasHeightForWidth())
        self.right_widget.setSizePolicy(sizePolicy)
        self.right_widget.setObjectName("right_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.right_widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.right_widget)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.left_widget = QtWidgets.QWidget(self.widget)
        self.left_widget.setObjectName("left_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.left_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.left_widget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.left_widget)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.left_widget)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.left_widget, 1, 0, 1, 1)
        self.right_widget_2 = QtWidgets.QWidget(self.widget)
        self.right_widget_2.setObjectName("right_widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.right_widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.right_widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.right_widget_2, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(2, 9)
        self.gridLayout_3.addWidget(self.widget, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.right_widget, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))

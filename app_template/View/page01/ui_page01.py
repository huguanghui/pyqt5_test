# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/page01/page01.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Page01Test(object):
    def setupUi(self, Page01Test):
        Page01Test.setObjectName("Page01Test")
        Page01Test.resize(960, 715)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Page01Test)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 40, 20, 20)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.CardWidget = CardWidget(Page01Test)
        self.CardWidget.setObjectName("CardWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.CardWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.SwitchButton = SwitchButton(self.CardWidget)
        self.SwitchButton.setObjectName("SwitchButton")
        self.verticalLayout.addWidget(self.SwitchButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.CardWidget, 0, 0, 1, 1)
        self.CardWidget_3 = CardWidget(Page01Test)
        self.CardWidget_3.setObjectName("CardWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.CardWidget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RadioButton = RadioButton(self.CardWidget_3)
        self.RadioButton.setObjectName("RadioButton")
        self.verticalLayout_3.addWidget(self.RadioButton)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.CardWidget_3, 1, 0, 1, 1)
        self.CardWidget_2 = CardWidget(Page01Test)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ToggleButton = ToggleButton(self.CardWidget_2)
        self.ToggleButton.setObjectName("ToggleButton")
        self.verticalLayout_2.addWidget(self.ToggleButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.CardWidget_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Page01Test)
        QtCore.QMetaObject.connectSlotsByName(Page01Test)

    def retranslateUi(self, Page01Test):
        _translate = QtCore.QCoreApplication.translate
        Page01Test.setWindowTitle(_translate("Page01Test", "Form"))
        self.RadioButton.setText(_translate("Page01Test", "Radio button"))
        self.ToggleButton.setText(_translate("Page01Test", "Toggle button"))
from qfluentwidgets import CardWidget, RadioButton, SwitchButton, ToggleButton


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Page01Test = QtWidgets.QWidget()
    ui = Ui_Page01Test()
    ui.setupUi(Page01Test)
    Page01Test.show()
    sys.exit(app.exec_())

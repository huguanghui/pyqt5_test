# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Demo(object):
    def setupUi(self, Demo):
        if not Demo.objectName():
            Demo.setObjectName(u"Demo")
        Demo.resize(800, 600)
        self.centralwidget = QWidget(Demo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        Demo.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Demo)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        Demo.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Demo)
        self.statusbar.setObjectName(u"statusbar")
        Demo.setStatusBar(self.statusbar)

        self.retranslateUi(Demo)

        QMetaObject.connectSlotsByName(Demo)
    # setupUi

    def retranslateUi(self, Demo):
        Demo.setWindowTitle(QCoreApplication.translate("Demo", u"Demo", None))
        self.pushButton.setText(QCoreApplication.translate("Demo", u"PushButton", None))
    # retranslateUi


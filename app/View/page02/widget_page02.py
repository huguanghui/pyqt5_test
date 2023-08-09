# coding:utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap

from .ui_page02 import Ui_Page02Test


class Page02Test(Ui_Page02Test, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ui_init()

    def ui_init(self):
        print("ui_init")
        self.videostream.setPixmap(QPixmap(':/images/test.jpg').scaled(
            160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # self.videostream

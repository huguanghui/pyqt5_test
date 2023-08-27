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
        video_w = self.videostream.width()
        video_h = self.videostream.height()
        print(video_w, video_h)
        m_w = self.videostream.geometry().width()
        m_h = self.videostream.geometry().height()
        print(m_w, m_h)
        # self.videostream.setPixmap(QPixmap(':/images/test.jpg').scaled(
        #     260, 260, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.videostream.setPixmap(QPixmap(':/images/test.jpg'))
        # self.videostream

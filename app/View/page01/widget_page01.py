# coding:utf-8

from PyQt5.QtWidgets import QWidget
from .ui_page01 import Ui_Page01Test


class Page01Test(Ui_Page01Test, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ui_init()

    def ui_init(self):
        print("ui_init")

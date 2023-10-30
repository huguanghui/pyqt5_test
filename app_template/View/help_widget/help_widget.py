# coding:utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .ui_help import Ui_Help


class HelpDoc(Ui_Help, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ui_init()

    def ui_init(self):
        print("ui_init")

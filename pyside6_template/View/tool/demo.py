# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from components.widgets.subwin import SubWindow

from .ui_demo import Ui_Demo


class ToolDemo(SubWindow):
    def __init__(self, name="ToolDemo", parent=None):
        super().__init__(name, parent, Ui_Demo())

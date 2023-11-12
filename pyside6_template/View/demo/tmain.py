from PySide6.QtWidgets import (
    QMainWindow,
    QSizeGrip,
)

from .ui_main import Ui_MainWindow


class MainWindowB(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

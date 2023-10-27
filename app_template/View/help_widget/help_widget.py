# coding:utf-8

from PyQt5.QtCore import Qt, pyqtSignal, QOperatingSystemVersion
from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout

from .ui_help import Ui_Help

class SettingInterface(QFrame):
    """ Setting interface """

    checkUpdateSig = pyqtSignal()
    crawlMetaDataFinished = pyqtSignal()
    musicFoldersChanged = pyqtSignal(list)
    acrylicEnableChanged = pyqtSignal(bool)
    downloadFolderChanged = pyqtSignal(str)
    minimizeToTrayChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)

        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName("settings")
        # setting label
        # self.settingLabel = QLabel(self.tr("Settings"), self)
        # self.settingLabel.setAlignment(Qt.AlignCenter)

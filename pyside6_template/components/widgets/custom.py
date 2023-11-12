# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox


def critical_win(string: str, parent=None):
    if string is not None:
        msgBox = QMessageBox()
        msgBox.setWindowFlags(msgBox.windowFlags() | Qt.WindowStaysOnTopHint)
        msgBox.setWindowFlags(msgBox.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
        msgBox.setWindowTitle("警告")
        msgBox.setText(string)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("是")
        msgBox.button(QMessageBox.No).setText("否")
        msgBox.exec_()
    return


def info_win(string: str, parent=None):
    if string is not None:
        msgBox = QMessageBox()
        msgBox.setWindowFlags(msgBox.windowFlags() | Qt.WindowStaysOnTopHint)
        msgBox.setWindowFlags(msgBox.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
        msgBox.setWindowTitle("提示")
        msgBox.setText(string)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("是")
        msgBox.button(QMessageBox.No).setText("否")
        msgBox.exec_()
    return

# coding:utf-8
from PySide6.QtCore import QObject, Signal

from .singleton import Singleton


class SignalBus(Singleton, QObject):
    """ Signal bus in App """
    appMessageSig = Signal(object)          # APP 发来消息
    appErrorSig = Signal(str)               # APP 发生异常
    appRestartSig = Signal()                # APP 需要重启
    selectionModeStateChanged = Signal(bool)  # 进入/退出 选择模式


signalBus = SignalBus()

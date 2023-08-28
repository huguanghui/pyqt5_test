# coding:utf-8
from PyQt5.QtCore import QLocale, Qt, QTranslator
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import (NavigationItemPosition, NavigationAvatarWidget, SplitFluentWindow, FluentTranslator)
from qfluentwidgets import FluentIcon as FIF

from common.application import SingletonApplication
# from common.config import config, Language
from common.setting import APP_NAME
# from common.dpi_manager import DPI_SCALE
from View.main_window import MainWindow

import os
import sys
from inspect import getsourcefile
from pathlib import Path
os.chdir(Path(getsourcefile(lambda: 0)).resolve().parent)

# fix bug: qt.qpa.plugin: Could not load the Qt platform plugin "xcb"
if "QT_QPA_PLATFORM_PLUGIN_PATH" in os.environ:
    os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

# enable high dpi scale
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
# os.environ["QT_SCALE_FACTOR"] = str(DPI_SCALE)


# class Window(SplitFluentWindow):
#     def __init__(self):
#         super().__init__()

#         # create sub interface
#         self.page01 = Page01Test(self)
#         self.page02 = Page02Test(self)
#         self.settingInterface = SettingInterface(self)

#         self.initNavigation()

#     def initNavigation(self):
#         # add sub interface
#         self.addSubInterface(self.page01, FIF.RINGER, '专注时段')
#         self.addSubInterface(self.page02, FIF.CODE, '流播放')
#         # self.addSubInterface(self.stopWatchInterface, FIF.STOP_WATCH, '秒表')

#         # self.navigationInterface.addWidget(
#         #     routeKey='avatar',
#         #     widget=NavigationAvatarWidget('zhiyiYo', 'resource/images/shoko.png'),
#         #     onClick=self.showMessageBox,
#         #     position=NavigationItemPosition.BOTTOM,
#         # )
#         self.navigationInterface.addItem(
#             routeKey='settingInterface',
#             icon=FIF.SETTING,
#             text='设置',
#             position=NavigationItemPosition.BOTTOM,
#         )

#         self.navigationInterface.setExpandWidth(280)

#     def switchTo(self, interface):
#         print(interface)
#         self.stackedWidget.setCurrentWidget(interface, popOut=False)
#         # 实现切换界面的逻辑
#         if interface == self.page01:
#             print("Switching to page01")
#         elif interface == self.page02:
#             print("Switching to page02")
#             m_w = self.page02.videostream.geometry().width()
#             m_h = self.page02.videostream.geometry().height()
#             print(m_w, m_h)
#             print(self.page02.width(), self.page02.height())

#     def showMessageBox(self):
#         print('showMessageBox')

if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    # translator = FluentTranslator()
    translator = QTranslator()
    translator.load(f":/i18n/ptool.zh_CN.qm")
    app.installTranslator(translator)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

# app = SingletonApplication(sys.argv, APP_NAME)
# app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
# app.setApplicationName(APP_NAME)

# Internationalization
# translator = QTranslator()
# language = config.get(config.language)  # type: Language

# if language == Language.AUTO:
#     translator.load(QLocale.system(), ":/i18n/Groove_")
# elif language != Language.ENGLISH:
#     translator.load(f":/i18n/ptools_{language.value}.qm")

# app.installTranslator(translator)


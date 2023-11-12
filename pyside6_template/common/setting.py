# coding: utf-8
from pathlib import Path
from PySide6.QtCore import QStandardPaths

# change DEBUG to False if you want to compile the code to exe
DEBUG = True


YEAR = 2023
AUTHOR = "hgh"
VERSION = "v0.0.1"
APP_NAME = "Demo"
HELP_URL = ""
FEEDBACK_URL = "https://github.com/huguanghui/pyqt5_test/issues"
RELEASE_URL = "https://github.com/huguanghui/pyqt5_test/releases/latest"

ENABLE_CUSTOM_TITLE_BAR = True
MENU_WIDTH = 240
LEFT_BOX_WIDTH = 240
RIGHT_BOX_WIDTH = 240
TIME_ANIMATION = 500

# BTNS LEFT AND RIGHT BOX COLORS
BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

# MENU SELECTED STYLESHEET
MENU_SELECTED_STYLESHEET = """
border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
background-color: rgb(40, 44, 52);
"""

if DEBUG:
    CONFIG_FOLDER = Path('AppData').absolute()
else:
    CONFIG_FOLDER = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)) / APP_NAME

CONFIG_FILE = CONFIG_FOLDER / "config.json"

print(f"FOLDER: {CONFIG_FOLDER}")

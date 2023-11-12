# coding:utf-8
import sys

import resource_rc
from common.config import config, Theme
from common.setting import APP_NAME, RELEASE_URL, RIGHT_BOX_WIDTH, BTN_RIGHT_BOX_COLOR, BTN_LEFT_BOX_COLOR, TIME_ANIMATION, MENU_WIDTH, LEFT_BOX_WIDTH, MENU_SELECTED_STYLESHEET
from common.style_sheet import setStyleSheet

from components.widgets.custom_grips import CustomGrip

from PySide6.QtCore import Qt, QUrl, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
from PySide6.QtGui import QIcon, QDesktopServices, QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QSizeGrip,
    QGraphicsDropShadowEffect,
    QPushButton,
)

from View.setting_interface import SettingInterface
from View.update import CheckUpdate
from View.tool import ToolDemo

from .ui_main import Ui_MainWindow

GLOBAL_STATE = False


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        self.resize(800, 600)
        self.setWindowIcon(QIcon(":/images/logo/logo.png"))
        self.setWindowTitle(APP_NAME)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # desktop = QApplication.desktop().availableGeometry()
        # w, h = desktop.width(), desktop.height()
        # self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.sub_windows = list()

        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

    def initWidget(self):
        self.setQss()
        self.connectSignalToSlot()
        self.onInitFinished()

    def onInitFinished(self):
        """initialize finished slot"""
        pass

    def setQss(self):
        setStyleSheet(self, "main_window", Theme.DARK)

    def connectSignalToSlot(self):
        """connect signal to slot"""
        def dobleClickMaximizeRestore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: self.maximize_restore())
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        def moveWindow(event):
            if self.returStatus():
                self.maximize_restore()
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.titleRightInfo.mouseMoveEvent = moveWindow

        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        self.ui.settingsTopBtn.clicked.connect(self.openCloseRightBox)
        self.ui.toggleButton.clicked.connect(self.toggleMenu)
        self.ui.toggleLeftBox.clicked.connect(self.toggleLeftBoxFunc)
        self.ui.extraCloseColumnBtn.clicked.connect(self.toggleLeftBoxFunc)
        self.ui.btn_home.clicked.connect(self.buttonClick)
        self.ui.btn_widgets.clicked.connect(self.buttonClick)
        self.ui.btn_new.clicked.connect(self.buttonClick)
        self.ui.btn_save.clicked.connect(self.buttonClick)

        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        # self.subwindow_function = {
        #     "ToolDemo": [self.actionDemo, ToolDemo],
        # }

        # self.actionVersion.triggered.connect(self.add_checkupdate_window)
        # self.actionHelp.triggered.connect(self.helpDoc)

        # for key, value in self.subwindow_function.items():
        #     value[0].triggered.connect(
        #         lambda win_name=key, win_object=value[1]: self.add_sub_window(
        #             win_name, win_object
        #         )
        #     )

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.widgets)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            self.ui.stackedWidget.setCurrentWidget(self.ui.new_page)  # SET PAGE
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # SELECT
    def selectMenu(self, getStyle):
        select = getStyle + MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(self, getStyle):
        deselect = getStyle.replace(MENU_SELECTED_STYLESHEET, "")
        return deselect

    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet()))

    def toggleLeftBoxFunc(self):
        width = self.ui.extraLeftBox.width()
        widthRightBox = self.ui.extraRightBox.width()
        maxExtend = LEFT_BOX_WIDTH
        color = BTN_LEFT_BOX_COLOR
        standard = 0

        # GET BTN STYLE
        style = self.ui.toggleLeftBox.styleSheet()

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            self.ui.toggleLeftBox.setStyleSheet(style + color)
            if widthRightBox != 0:
                style = self.ui.settingsTopBtn.styleSheet()
                self.ui.settingsTopBtn.setStyleSheet(style.replace(BTN_RIGHT_BOX_COLOR, ''))
        else:
            widthExtended = standard
            self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        self.start_box_animation(width, widthRightBox, "left")

    def toggleMenu(self):
        width = self.ui.leftMenuBg.width()
        maxExtend = MENU_WIDTH
        standard = 60

        # SET MAX WIDTH
        if width == 60:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
        self.animation.setDuration(TIME_ANIMATION)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def openCloseRightBox(self):
        print("settings")
        # GET WIDTH
        width = self.ui.extraRightBox.width()
        widthLeftBox = self.ui.extraLeftBox.width()
        maxExtend = RIGHT_BOX_WIDTH
        color = BTN_RIGHT_BOX_COLOR
        standard = 0

        # GET BTN STYLE
        style = self.ui.settingsTopBtn.styleSheet()

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            # SELECT BTN
            self.ui.settingsTopBtn.setStyleSheet(style + color)
            if widthLeftBox != 0:
                style = self.ui.toggleLeftBox.styleSheet()
                self.ui.toggleLeftBox.setStyleSheet(style.replace(BTN_LEFT_BOX_COLOR, ''))
        else:
            widthExtended = standard
            # RESET BTN
            self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

        self.start_box_animation(widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0

        # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def add_sub_window(self, name, win_object):
        sub_window = win_object(parent=self)
        self.ui.mdiArea.addSubWindow(sub_window)
        self.sub_windows.append(sub_window)
        sub_window.show()

    def helpDoc(self):
        print("Help")
        QDesktopServices.openUrl(QUrl.fromLocalFile("Readme.html"))

    def add_checkupdate_window(self):
        sub_win = CheckUpdate(parent=self)
        sub_win.show()

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status is False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/images/icons/icon_restore.png"))
            self.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/images/icons/icon_maximize.png"))
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    def returStatus(self):
        return GLOBAL_STATE

    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def resizeEvent(self, event):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        msgBox = QMessageBox()
        msgBox.setWindowFlags(msgBox.windowFlags() | Qt.WindowStaysOnTopHint)
        msgBox.setWindowFlags(msgBox.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
        msgBox.setWindowTitle("ImageTools")
        msgBox.setText("是否要退出程序？")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("是")
        msgBox.button(QMessageBox.No).setText("否")
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class MainWindowA(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

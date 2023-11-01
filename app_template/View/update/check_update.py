# coding:utf-8

from PyQt5.QtCore import (
    QThread,
    pyqtSignal,
)

from PyQt5.QtWidgets import QDialog

from os import startfile, mkdir
from os.path import exists, abspath, dirname
from sys import exit
import requests
import time

from components.widgets.custom import critical_win
from common.config import config

from .ui_check_update import Ui_CheckUpdate

VERSION_NUMS_LEN = 3
VERSION_FILE = "http://1.13.20.3/ptool/version.md"

CURRENT_VERSION_FILE = "version.md"
REMOTE_INSTALL_PACK = "http://1.13.20.3/ptool/PTool.exe"
DOWNLOAD_INSTALL_PACK = ".\\latest_installer\\installer.exe"


def check_is_latest(current, new) -> bool:
    """
    func: 检查是否为最新版本
    """
    current_version = current.split(".")
    new_version = new.split(".")
    for i in range(VERSION_NUMS_LEN):
        if int(current_version[i]) < int(new_version[i]):
            return False
        if int(current_version[i]) > int(new_version[i]):
            return True
    return True


def get_latest_version_log():
    """
    func: 获取最新的版本日志文件
    把日志转换成UTF-8格式
    """
    try:
        res = requests.get(VERSION_FILE, timeout=2)
        if res.status_code != 200:
            return ""
        res.encoding = "utf-8"
        res.close()
        return res.text
    except Exception as e:
        print(e)
        # error(e)
        return ""


def get_current_version_log():
    """
    func: 获取当前版本日志
    """
    with open(CURRENT_VERSION_FILE, "r", encoding="utf-8") as f:
        return f.read()


def get_version(version_log):
    """
    func: 获取日志文件的最新版本号
    日志文件格式必须为 **x.x.x**
    """
    start_index = version_log.find("**") + 2
    end_index = version_log.find("**", start_index)
    return version_log[start_index:end_index]


def download_file(srcUrl):
    """
    func: 下载一个大文件
    """
    localFile = srcUrl.split("/")[-1]
    # info("开始下载 %s" % (srcUrl))
    # startTime = time.time()
    with requests.get(srcUrl, stream=True) as r:
        contentLength = int(r.headers["content-length"])
        line = "content-length: %dB/ %.2fKB/ %.2fMB"
        line = line % (contentLength, contentLength / 1024, contentLength / 1024 / 1024)
        # info(line)
        downSize = 0
        with open(localFile, "wb") as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
                downSize += len(chunk)
                # line = '%d KB/s - %.2f MB， 共 %.2f MB'
                # line = line % (downSize/1024/(time.time()-startTime),
                #                downSize/1024/1024, contentLength/1024/1024)
                # info(line)
                if downSize >= contentLength:
                    break
        # timeCost = time.time() - startTime
        # info(
        #     "下载成功, 共耗时: %.2f s, 平均速度: %.2f KB/s"
        #     % (timeCost, downSize / 1024 / timeCost)
        # )
    return True


def simple_check_is_need_update() -> bool:
    """
    func: 简单的返回是否需要更新
    """
    current_version = get_version(get_current_version_log())
    version_log = get_latest_version_log()
    if version_log == "":
        return False
    latest_version = get_version(version_log)
    if check_is_latest(current_version, latest_version) is True:
        return False
    return True


def check_update():
    """
    检查更新
    """
    current_log = get_current_version_log()
    current_version = get_version(current_log)

    version_log = get_latest_version_log()
    if version_log == "":
        return "connect error", current_version, current_log

    latest_version = get_version(version_log)
    if check_is_latest(current_version, latest_version) is True:
        return "already latest", current_version, current_log
    else:
        return latest_version, current_version, version_log


class CheckUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_CheckUpdate()
        self.ui.setupUi(self)
        self.autoupdate = config.get(config.checkUpdateAtStartUp)
        self.ui.autoupdate.setChecked(self.autoupdate)
        # self.ui.autoupdate.stateChanged.connect(self.set_autoupdate_param)
        self.ui.ok.clicked.connect(self.start_update)
        self.ui.cancel.clicked.connect(lambda: self.close())
        self.update_proc = UpdateProc(REMOTE_INSTALL_PACK, self)
        self.update_proc.doneCB.connect(self.update_proc_done)
        self.update_proc.processRateCB.connect(
            lambda rate: self.ui.progress.setValue(rate)
        )

        latest_version, current_version, latest_log = check_update()

        # 异常处理
        if latest_version == "connect error":
            self.ui.version_num.setText("!!!网络连接出错!!! 当前版本为 " + current_version)
            self.need_update = -1
        elif latest_version == "already latest":
            self.ui.version_num.setText("软件已经是最新啦！当前版本为 " + current_version)
            self.need_update = 0
        else:
            self.ui.version_num.setText(
                "有版本更新啦！当前版本为 " + current_version + "; 最新版本为 " + latest_version
            )
            self.need_update = 1

        self.ui.textBrowser.setMarkdown(latest_log)

    def start_update(self):
        if self.need_update == 1:
            if not exists(dirname(DOWNLOAD_INSTALL_PACK)):
                mkdir(dirname(DOWNLOAD_INSTALL_PACK))
            self.update_proc.start()
        elif self.need_update == 0:
            critical_win("软件已经是最新啦")
        elif self.need_update == -1:
            critical_win("网络连接出错")

    def update_proc_done(self, ret):
        if ret == 0:
            # info('下载成功')
            # Popen('start ' + REMOTE_INSTALL_PACK.split('/')
            #       [-1], shell=True, stdin=PIPE, stdout=PIPE)
            # os.system('start ChromeSetup.exe')
            if exists(DOWNLOAD_INSTALL_PACK) is True:
                startfile(DOWNLOAD_INSTALL_PACK)
                # info("正在启用最新升级包")
                exit()
            critical_win("下载的升级包不存在")
        else:
            # info("下载失败")
            print("下载失败")


class UpdateProc(QThread):
    doneCB = pyqtSignal(int)
    processRateCB = pyqtSignal(int)

    def __init__(self, url, parent=None) -> None:
        super(UpdateProc, self).__init__(parent=parent)
        self.url = url

    def run(self):
        self.processRateCB.emit(0)
        # info('开始下载更新...')
        with requests.get(self.url, stream=True, timeout=5) as r:
            contentLength = int(r.headers["content-length"])
            downSize = 0
            with open(DOWNLOAD_INSTALL_PACK, "wb") as f:
                for chunk in r.iter_content(8192):
                    if chunk:
                        f.write(chunk)
                    downSize += len(chunk)
                    self.processRateCB.emit(downSize / contentLength * 100)
                    # info('下载进度{}%'.format(downSize/contentLength * 100))
                    if downSize >= contentLength:
                        self.doneCB.emit(0)
                        return
        self.doneCB.emit(-1)
        return

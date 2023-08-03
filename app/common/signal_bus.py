# coding:utf-8
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtMultimedia import QMediaPlaylist

# from common.crawler import SongQuality, QueryServerType

# from .database.entity import AlbumInfo, SingerInfo, SongInfo
from .singleton import Singleton


class SignalBus(Singleton, QObject):
    """ Signal bus in Groove Music """
    appMessageSig = pyqtSignal(object)          # APP 发来消息
    appErrorSig = pyqtSignal(str)               # APP 发生异常
    appRestartSig = pyqtSignal()                # APP 需要重启

    randomPlayAllSig = pyqtSignal()             # 无序播放所有
    playCheckedSig = pyqtSignal(list)           # 播放选中的歌曲
    nextToPlaySig = pyqtSignal(list)            # 下一首播放
    playAlbumSig = pyqtSignal(str, str)         # 播放专辑
    playPlaylistSig = pyqtSignal(list, int)     # 播放歌曲列表

    addSongsToPlayingPlaylistSig = pyqtSignal(list)      # 添加到正在播放
    addSongsToNewCustomPlaylistSig = pyqtSignal(list)    # 添加到新建自定义播放列表
    addSongsToCustomPlaylistSig = pyqtSignal(str, list)  # 添加到自定义播放列表
    addFilesToCustomPlaylistSig = pyqtSignal(str, list)  # 添加本地文件到播放列表

    removeSongSig = pyqtSignal(list)            # 删除本地歌曲
    clearPlayingPlaylistSig = pyqtSignal()      # 清空正在播放列表
    deletePlaylistSig = pyqtSignal(str)         # 删除自定义播放列表
    renamePlaylistSig = pyqtSignal(str, str)    # 重命名自定义播放列表

    selectionModeStateChanged = pyqtSignal(bool)  # 进入/退出 选择模式

    showPlayingPlaylistSig = pyqtSignal()                        # 显示正在播放列表
    switchToPlayingInterfaceSig = pyqtSignal()                   # 显示正在播放界面信号
    switchToSettingInterfaceSig = pyqtSignal()                   # 切换到设置界面信号
    switchToSingerInterfaceSig = pyqtSignal(str)                 # 切换到歌手界面
    switchToAlbumInterfaceSig = pyqtSignal(str, str)             # 切换到专辑界面
    switchToMyMusicInterfaceSig = pyqtSignal()                   # 切换到我的音乐界面
    switchToRecentPlayInterfaceSig = pyqtSignal()                # 切换到最近播放界面
    switchToPlaylistInterfaceSig = pyqtSignal(str)               # 切换到播放列表界面信号
    switchToPlaylistCardInterfaceSig = pyqtSignal()              # 切换到播放列表卡界面
    switchToSmallestPlayInterfaceSig = pyqtSignal()              # 显示最小播放模式界面
    switchToVideoInterfaceSig = pyqtSignal(str, str)             # 切换到视频界面
    switchToLabelNavigationInterfaceSig = pyqtSignal(list, str)  # 显示标签导航界面

    nextSongSig = pyqtSignal()             # 下一首
    lastSongSig = pyqtSignal()             # 上一首
    togglePlayStateSig = pyqtSignal()      # 播放/暂停
    progressSliderMoved = pyqtSignal(int)  # 播放进度条滑动

    muteStateChanged = pyqtSignal(bool)   # 静音
    volumeChanged = pyqtSignal(int)       # 调整音量

    randomPlayChanged = pyqtSignal(bool)                        # 随机播放
    loopModeChanged = pyqtSignal(QMediaPlaylist.PlaybackMode)   # 循环模式

    playSpeedUpSig = pyqtSignal()       # 加速播放
    playSpeedDownSig = pyqtSignal()     # 减速播放
    playSpeedResetSig = pyqtSignal()    # 恢复播放速度

    writePlayingSongStarted = pyqtSignal()     # 开始向正在播放的歌曲写入数据
    writePlayingSongFinished = pyqtSignal()    # 完成向正在播放的歌曲写入数据

    showMainWindowSig = pyqtSignal()      # 显示主界面
    fullScreenChanged = pyqtSignal(bool)  # 全屏/退出全屏

    downloadAvatarFinished = pyqtSignal(str, str)  # 下载了一个头像

    totalOnlineSongsChanged = pyqtSignal(int)      # 搜索到的在线音乐总数发生变化

    lyricFontChanged = pyqtSignal(QFont)                       # 正在播放界面歌词字体改变
    albumBlurRadiusChanged = pyqtSignal(int)                   # 正在播放界面背景磨砂半径改变

    desktopLyricStyleChanged = pyqtSignal()              # 桌面歌词样式改变


signalBus = SignalBus()

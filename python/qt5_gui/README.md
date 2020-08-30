# PyQt5 的入门使用

## 文档

[中文手册](https://maicss.gitbooks.io/pyqt5/content/)

## 打包成exe

### pyInstaller

#### 工具安装

```shell
$ pip install Pyinstaller
```

#### 使用

打包单个文件

```shell
$ pyinstaller -F -w -i dancer.ico main.py
```

-F 打包为单文件
-w windows程序
-i 程序图标

打包PyQt5的问题整理
[加载失败](https://stackoverflow.com/questions/56949297/how-to-fix-importerror-unable-to-find-qt5core-dll-on-path-after-pyinstaller-b)
[github_issus](https://github.com/pyinstaller/pyinstaller/issues/4293)

## 打包成msi

## 问题点

### QWidget, QDialog 及 QMainWindow 的区别
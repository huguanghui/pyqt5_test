
## 打包

```
$ pyinstaller.exe --onefile --icon=.\resource\images\logo\logo.ico --name=PTool -Fw .\PTool.py
$ pyinstaller.exe PTool.spec --noconfirm
```

pylupdate5 .\View\main_window\ui_main.py .\View\page01\ui_page01.py -ts .\resource\i18n\ptool.zh_CN.ts
lrelease.exe .\resource\i18n\ptool.zh_CN.ts


## 安装包制作

```
# Inno Setup Compiler安装包需要安装5.6.0以上的版本
$ Start-Process -FilePath "compil32" -ArgumentList "/cc ./PTool.iss" -Wait

```

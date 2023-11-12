Write-Host "Pyqt5 build..." -ForegroundColor green

# $env:PATH += ";E:\ProgramData\miniconda3\envs\pysider6\Lib\site-packages\PySide6"

# pyrccc
pyside6-rcc.exe ./resource/resource.qrc -o resource_rc.py

# designer
# pyside6-designer.exe .\View\main_window\main.ui

# compile
pyside6-uic.exe ./View/main_window/main.ui -o ./View/main_window/ui_main.py
pyside6-uic.exe ./View/help_widget/help.ui -o ./View/help_widget/ui_help.py
pyside6-uic.exe ./View/update/check_update.ui -o ./View/update/ui_check_update.py
pyside6-uic.exe ./View/tool/demo.ui -o ./View/tool/ui_demo.py
pyside6-uic.exe ./View/demo/main.ui -o ./View/demo/ui_main.py
# uic.exe ./View/page01/page01.ui -o ./View/page01/ui_page01.py
# uic.exe ./View/page02/page02.ui -o ./View/page02/ui_page02.py

# language
pyside6-lupdate.exe .\View\main_window\ui_main.py ./View/help_widget/ui_help.py ./View/update/ui_check_update.py ./View/tool/ui_demo.py -ts .\resource\i18n\ptool.zh_CN.ts
# linguist.exe .\resource\i18n\ptool.zh_CN.ts 
pyside6-lrelease.exe .\resource\i18n\ptool.zh_CN.ts

python PTool.py


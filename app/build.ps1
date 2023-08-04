Write-Host "Pyqt5 build..." -ForegroundColor green

# pyrccc
# pyrcc5.exe ./resource/resource.qrc -o ./common/resource.py

# designer
# python ../tools/designer.py .\View\main_window\main.ui

# compile
pyuic5.exe ./View/main_window/main.ui -o ./View/main_window/ui_main.py -x

python PTool.py

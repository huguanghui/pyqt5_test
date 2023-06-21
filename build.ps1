Write-Host "Pyqt5 build..." -ForegroundColor green

# pyrccc
# C:\Users\LENOVO\AppData\Roaming\Python\Python39\Scripts\pyrcc5.exe ./01_BurnTest/resource.qrc -o ./01_BurnTest/resource_rc.py
# C:\ProgramData\Miniconda3\Scripts\pyrcc5.exe ./01_BurnTest/resource.qrc -o ./01_BurnTest/resource_rc.py

# designer
# C:\ProgramData\Miniconda3\Lib\site-packages\qt5_applications\Qt\bin\designer.exe .\01_BurnTest\GUI\Main.ui
# C:\ProgramData\Miniconda3\Lib\site-packages\qt5_applications\Qt\bin\designer.exe .\01_BurnTest\GUI\Login.ui
# designer.exe .\01_QThread\GUI\Main.ui

# compile
C:\Users\LENOVO\AppData\Roaming\Python\Python39\Scripts\pyuic5.exe ./01_QThread/GUI/Main.ui -o ./01_QThread/GUI/Ui_Main.py -x
# C:\Users\LENOVO\AppData\Roaming\Python\Python39\Scripts\pyuic5.exe ./01_BurnTest/GUI/Login.ui -o ./01_BurnTest/GUI/Ui_Login.py -x

# C:\ProgramData\Miniconda3\Scripts\pyuic5.exe ./01_BurnTest/GUI/Main.ui -o ./01_BurnTest/GUI/Ui_Main.py -x

python ./01_QThread/main.py


@echo off
setlocal enabledelayedexpansion

set ROOT_DIR=%~dp0
call :GetFullPath "%ROOT_DIR%\.." ROOT

pip --default-timeout=100 install Pyinstaller
if ERRORLEVEL 1 GOTO errorHandling

REM 工程目录
set "DEMO_TEST01_CODE_DIR=%ROOT%\python\qt5_gui\test01"

REM 打包
cd "%DEMO_TEST01_CODE_DIR%" && pyinstaller -F -w test.py

exit /B 0

:GetFullPath
SET %2=%~f1

GOTO :EOF

:errorHandling
echo Error
cd "%ROOT_DIR%"
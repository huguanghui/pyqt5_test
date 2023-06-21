@echo off
setlocal enabledelayedexpansion

set ROOT_DIR=%~dp0
call :GetFullPath "%ROOT_DIR%\.." ROOT

pip --default-timeout=100 install --user pyautogui
if ERRORLEVEL 1 GOTO errorHandling

REM 执行 pyautogui 的 demo 程序
set "DEMO_PYTHON_DIR=%ROOT%\python"

echo python "%DEMO_PYTHON_DIR%\autogui_use\test.py"
python "%DEMO_PYTHON_DIR%\autogui_use\test.py"

exit /B 0

:GetFullPath
SET %2=%~f1

GOTO :EOF

:errorHandling
echo Error
cd "%ROOT_DIR%"

Remove-Item -Path .\build\* -Force -Recurse
Remove-Item -Path .\dist\* -Force -Recurse
Remove-Item -Path .\build -Force -Recurse
Remove-Item -Path .\dist -Force -Recurse
# pip install pyinstaller
Start-Process -FilePath "pyinstaller" -ArgumentList "-w ./PTool.py --noconfirm" -Wait
# Copy-Item -Path .\Readme.html -Destination .\dist\ImageTools\
Copy-Item -Path .\version.md -Destination .\dist\PTool\
Start-Process -FilePath "compil32" -ArgumentList "/cc ./PTool.iss" -Wait

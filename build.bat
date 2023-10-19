python -m pip install PyInstaller

@echo off
setlocal enabledelayedexpansion

set "package_name=site-packages"

for %%I in (python.exe) do (
    for /f "delims=" %%A in ('where "%%I"') do (
        set "python_path=%%~dpA"
        set "package_path=!python_path!Lib\!package_name!"
    )
)

python -m PyInstaller -F --paths=!package_path! main.py

endlocal
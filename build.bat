@echo off
setlocal enabledelayedexpansion

set "package_name=site-packages"

for %%I in (python.exe) do (
    for /f "delims=" %%A in ('where "%%I"') do (
        set "python_path=%%~dpA"
        set "package_path=!python_path!Lib\!package_name!"
    )
)

rem Define external modules that PyInstaller should include
set "external_modules=progress, progress.bar"

rem Create a list of --hidden-import options for PyInstaller
set "hidden_imports="
for %%M in (%external_modules%) do (
    set "hidden_imports=!hidden_imports! --hidden-import %%M"
)

rem Use PyInstaller with the hidden imports
py -m pip install progress
python -m PyInstaller --onefile -F --paths=!package_path! %hidden_imports% main.py -n pip-migrate.exe

endlocal

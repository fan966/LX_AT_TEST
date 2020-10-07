@echo off
cd /d "%~dp0"
cd /d "%cd%\"
pip install -r requirements.txt
::pip install --no-index --find-links=packages -r requirements.txt

echo ---------------------------------------------------------------------------------------
pause
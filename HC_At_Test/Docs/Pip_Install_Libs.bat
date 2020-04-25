@echo off
cd /d "%~dp0"
cd /d "%cd%\"
pip install -r requirements.txt

echo ---------------------------------------------------------------------------------------
pause
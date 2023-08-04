@echo off
echo [40;32mInstalling Requirements For You....[40;37m
echo.
pip install --upgrade -r add.txt
echo.
echo [40;32mLaunching InstaCheck..[40;37m
timeout 2 >nul
python InstaCheck.py
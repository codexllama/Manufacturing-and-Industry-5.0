@echo off
title AutoPlant-OS Launcher

echo ========================================
echo       AutoPlant-OS Starting...
echo ========================================
echo.

cd /d E:\AutoPlant-OS\backend

echo Backend folder:
cd
echo.

echo Checking Python environment...
if not exist "venv\Scripts\python.exe" (
    echo ERROR: Python virtual environment not found.
    pause
    exit /b 1
)

echo Python environment found.
echo.

echo Starting FastAPI...
echo ========================================
echo.

venv\Scripts\python.exe -m uvicorn main:app --reload

echo.
echo ========================================
echo FastAPI has stopped.
echo ========================================
pause
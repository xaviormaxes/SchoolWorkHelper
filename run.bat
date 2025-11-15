@echo off
REM School Work Helper Launcher for Windows

echo Starting School Work Helper...
python school_helper.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to start the application.
    echo Make sure Python is installed and you've run 'pip install -r requirements.txt'
    echo.
    pause
)

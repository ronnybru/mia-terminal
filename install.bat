@echo off
:: Installation script for mia-terminal on Windows

echo Installing MIA Terminal...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is required but not installed.
    echo Please install Python and try again.
    exit /b 1
)

:: Check Python version
for /f "tokens=2" %%I in ('python --version 2^>^&1') do set PYTHON_VERSION=%%I
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

if %MAJOR% LSS 3 (
    echo Error: Python 3.6 or higher is required.
    echo Current version: %PYTHON_VERSION%
    exit /b 1
)

if %MAJOR% EQU 3 (
    if %MINOR% LSS 6 (
        echo Error: Python 3.6 or higher is required.
        echo Current version: %PYTHON_VERSION%
        exit /b 1
    )
)

:: Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pip is required but not installed.
    echo Please install pip and try again.
    exit /b 1
)

:: Get the directory of the script
set SCRIPT_DIR=%~dp0

echo Installing from directory: %SCRIPT_DIR%

:: Install the package
echo Installing package...
pip install -e "%SCRIPT_DIR%"

:: Check if installation was successful
if %errorlevel% equ 0 (
    echo.
    echo ✅ Installation successful!
    echo.
    echo You can now use mia by running:
    echo   mia ^<your natural language prompt^>
    echo.
    echo Example:
    echo   mia list all files in the current directory sorted by size
    echo.
    echo On first use, you'll be prompted to enter your OpenAI API key.
) else (
    echo ❌ Installation failed.
    exit /b 1
)

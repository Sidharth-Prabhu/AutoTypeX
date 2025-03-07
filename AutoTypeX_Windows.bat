@echo off
setlocal

:: Set environment and script names
set VENV_DIR=venv
set REQUIREMENTS=requirements.txt
set PYTHON_SCRIPT=typexgui.py

:: Check if venv exists, if not, create it
if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

:: Activate virtual environment
call %VENV_DIR%\Scripts\activate

:: Check if requirements.txt exists and install dependencies
if exist %REQUIREMENTS% (
    echo Installing dependencies...
    pip install -r %REQUIREMENTS%
) else (
    echo No requirements.txt found. Skipping dependency installation.
)

:: Run the Python script
python %PYTHON_SCRIPT%

:: Deactivate and remove virtual environment after execution
echo Cleaning up...
call %VENV_DIR%\Scripts\deactivate
rd /s /q %VENV_DIR%

:: Exit the batch script
exit /b

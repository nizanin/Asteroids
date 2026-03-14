@echo off
REM Sprawdzenie Pythona
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python nie jest zainstalowany. Pobierz i zainstaluj Python 3.12+ z: https://www.python.org/downloads/
    pause
    exit /b
)

REM Tworzenie venv jeśli nie istnieje
if not exist ".venv\Scripts\python.exe" (
    python -m venv .venv
)

REM Aktywacja venv
call .venv\Scripts\activate.bat

REM Instalacja zależności
pip install --upgrade pip
python -m pip install -r requirements.txt

REM Uruchomienie gry
python main.py
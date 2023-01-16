@echo off


chcp 65001

echo Vérification de l'installation de Python 3 et de pip...
python -V
if %errorlevel% NEQ 0 (
    echo Python 3 n'est pas installé. Veuillez l'installer avant de continuer.
    pause
    exit /b
)
python -m pip -V
if %errorlevel% NEQ 0 (
    echo pip n'est pas installé. Veuillez l'installer avant de continuer.
    pause
    exit /b
)

echo Vérification de l'installation des modules ctypes, mouse, keyboard et pyperclip...
python -c "import ctypes"
if %errorlevel% NEQ 0 (
    echo Le module ctypes n'est pas installé. Installation en cours...
    python -m pip install ctypes
)
python -c "import pyautogui"
if %errorlevel% NEQ 0 (
    echo Le module pyautogui n'est pas installé. Installation en cours...
    python -m pip install pyautogui
)
python -c "import keyboard"
if %errorlevel% NEQ 0 (
    echo Le module keyboard n'est pas installé. Installation en cours...
    python -m pip install keyboard
)
python -c "import pyperclip"
if %errorlevel% NEQ 0 (
    echo Le module pyperclip n'est pas installé. Installation en cours...
    python -m pip install pyperclip
)

echo Tous les modules sont installés!
pause

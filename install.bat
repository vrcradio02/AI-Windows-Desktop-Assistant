@echo off
REM Script d'installation pour Windows
REM Assistant IA Windows Desktop

echo.
echo ============================================================
echo  INSTALLATION - Assistant IA Windows Desktop
echo ============================================================
echo.

REM Verifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python n'est pas installe ou pas dans PATH
    echo Installez Python 3.8+ depuis https://www.python.org
    pause
    exit /b 1
)

echo [1/5] Verification Python... OK

REM Creer venv
if not exist venv (
    echo [2/5] Creation environnement virtuel...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Impossible de creer l'environnement virtuel
        pause
        exit /b 1
    )
) else (
    echo [2/5] Environnement virtuel existe deja... OK
)

REM Activer venv
echo [3/5] Activation environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dependances
echo [4/5] Installation des dependances...
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Erreur lors de l'installation des dependances
    echo Essayez: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Creer fichier .env
echo [5/5] Configuration...
if not exist .env (
    copy .env.example .env
    echo.
    echo ============================================================
    echo  CONFIGURATION REQUISE
    echo ============================================================
    echo.
    echo Editez le fichier: .env
    echo Remplacez: OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE
    echo Par votre vraie cle API d'OpenRouter
    echo.
    echo https://openrouter.io/keys
    echo.
    echo ============================================================
    echo.
) else (
    echo .env existe deja... OK
)

echo.
echo ============================================================
echo  INSTALLATION COMPLETE!
echo ============================================================
echo.
echo Prochaines etapes:
echo 1. Editez .env avec votre cle API OpenRouter
echo 2. Executez: python main.py
echo.
echo ============================================================
echo.
pause

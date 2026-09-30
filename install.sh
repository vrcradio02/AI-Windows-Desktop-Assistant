#!/bin/bash
# Script d'installation pour Linux/Mac
# Assistant IA Windows Desktop

echo ""
echo "============================================================"
echo "  INSTALLATION - Assistant IA Windows Desktop"
echo "============================================================"
echo ""

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 n'est pas installé"
    echo "Installez Python 3.8+ depuis https://www.python.org"
    exit 1
fi

echo "[1/5] Vérification Python... OK"
python3 --version

# Créer venv
if [ ! -d "venv" ]; then
    echo "[2/5] Création environnement virtuel..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Impossible de créer l'environnement virtuel"
        exit 1
    fi
else
    echo "[2/5] Environnement virtuel existe déjà... OK"
fi

# Activer venv
echo "[3/5] Activation environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "[4/5] Installation des dépendances..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Erreur lors de l'installation des dépendances"
    exit 1
fi

# Créer fichier .env
echo "[5/5] Configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo ""
    echo "============================================================"
    echo "  CONFIGURATION REQUISE"
    echo "============================================================"
    echo ""
    echo "Éditez le fichier: .env"
    echo "Remplacez: OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE"
    echo "Par votre vraie clé API d'OpenRouter"
    echo ""
    echo "https://openrouter.io/keys"
    echo ""
    echo "============================================================"
    echo ""
else
    echo ".env existe déjà... OK"
fi

echo ""
echo "============================================================"
echo "  INSTALLATION COMPLÈTE!"
echo "============================================================"
echo ""
echo "Prochaines étapes:"
echo "1. Éditez .env avec votre clé API OpenRouter"
echo "2. Exécutez: python main.py"
echo ""
echo "============================================================"
echo ""

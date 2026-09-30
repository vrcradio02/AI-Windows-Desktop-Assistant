# 📚 Guide d'Installation Détaillé

## 🖥️ Système d'exploitation

Ce projet fonctionne sur:
- ✅ **Windows 10/11** (Recommandé - toutes les features)
- ✅ **Linux** (Ubuntu 20.04+, Fedora, etc.)
- ✅ **macOS** (Intel et Apple Silicon)

---

## 📥 **Installation Automatisée (Recommandé)**

### Sur Windows:
```bash
# Double-cliquez sur install.bat
# OU depuis le terminal:
install.bat
```

### Sur Linux/Mac:
```bash
chmod +x install.sh
./install.sh
```

---

## 🔧 **Installation Manuelle**

### Étape 1: Cloner le repository
```bash
git clone https://github.com/vrcradio02/AI-Windows-Desktop-Assistant.git
cd AI-Windows-Desktop-Assistant
```

### Étape 2: Créer un environnement virtuel

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Étape 3: Installer les dépendances

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

> **Note**: Si vous avez une erreur avec PyAudio, ce n'est pas grave. Le mode vocal fonctionnera partiellement mais le reste fonctionne parfaitement.

### Étape 4: Configurer l'API OpenRouter

```bash
# Copier le fichier d'exemple
cp .env.example .env  # Linux/Mac
copy .env.example .env  # Windows
```

Ouvrez `.env` et remplacez:
```dotenv
OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE
```

Par votre vraie clé (obtenue sur https://openrouter.io/keys)

### Étape 5: Lancer l'application

```bash
python main.py
```

---

## 🐛 **Dépannage**

### ❌ "No module named 'X'"

Installez manuellement:
```bash
pip install pyperclip pyautogui psutil requests python-dotenv pydantic pillow gtts pyttsx3 speechrecognition
```

### ❌ "OPENROUTER_API_KEY not found"

1. Vérifiez que `.env` existe dans le dossier principal
2. Vérifiez que la clé est bien remplie
3. Redémarrez le terminal après édition de `.env`

### ❌ "ModuleNotFoundError: No module named 'pyaudio'"

PyAudio n'est pas disponible facilement sur Windows. C'est OK! 
- Le mode texte et GUI fonctionneront parfaitement
- Le mode vocal aura une reconnaissance limitée
- Vous pouvez toujours utiliser `pyttsx3` pour la synthèse vocale

### ❌ "No audio input detected"

- Vérifiez que votre microphone est branché
- Allez dans Paramètres → Son et vérifiez les permissions
- Testez votre microphone dans une autre application d'abord

### ❌ "Permission denied" (Linux/Mac)

```bash
chmod +x install.sh
./install.sh
```

### ❌ Erreur avec PyGetWindow

Installez la bonne version:
```bash
pip install --upgrade pygetwindow>=0.0.9
```

---

## ✅ **Vérifier l'installation**

Testez avec une commande simple:
```bash
python main.py
# Choisir mode 1 (texte)
# Tapez: help
# Puis: exit
```

---

## 📁 **Fichiers créés après première utilisation**

```
AI-Windows-Desktop-Assistant/
├── venv/                      # Environnement virtuel
├── .env                       # Configuration (SECRET - pas en git)
├── permissions.json           # Permissions accordées
├── permission_audit.log       # Historique des permissions
├── assistant_logs.txt         # Logs de l'application
└── screenshots/               # Captures d'écran prises
    ├── screenshot_20260930_140523.png
    └── ...
```

---

## 🚀 **Prochaines étapes**

1. ✅ Éditer `.env` avec votre clé API
2. ✅ Lancer `python main.py`
3. ✅ Choisir le mode (texte recommandé pour débuter)
4. ✅ Accorder les permissions demandées
5. ✅ Essayer quelques commandes:
   - `Dis-moi l'heure`
   - `Quel est le jour?`
   - `Quel est l'usage CPU?`
   - `Prends une capture d'écran`

---

## 💡 **Conseils**

- Gardez votre clé API secrète (elle est dans `.env` qui est ignoré par git)
- Les permissions sont sauvegardées dans `permissions.json`
- Les logs sont sauvegardés dans `assistant_logs.txt`
- Vous pouvez annuler une action avec `Ctrl+C`
- Le failsafe PyAutoGUI: déplacer la souris au coin haut-gauche arrête les actions

---

## 📞 **Besoin d'aide?**

- 📖 Consultez le README.md
- 🐛 Ouvrez une issue sur GitHub
- 💬 Vérifiez les logs dans `assistant_logs.txt`


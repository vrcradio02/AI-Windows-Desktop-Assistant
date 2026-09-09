# 🤖 Assistant IA Windows Desktop

Un assistant IA complet pour contrôler votre ordinateur Windows en direct avec OpenRouter API.

## ✨ Fonctionnalités

### 🎮 Contrôle Système
- **Contrôle souris**: Mouvement, clic, double-clic
- **Contrôle clavier**: Saisie de texte, raccourcis clavier
- **Lancement d'applications**: Ouvrir n'importe quel programme
- **Exécution de commandes**: Shell, PowerShell, etc.
- **Captures d'écran**: Analyse et sauvegarde
- **Presse-papiers**: Lecture/écriture
- **Infos système**: CPU, RAM, disque, processus

### 🔐 Gestion des Permissions
- Système de permissions granulaire
- Demande de confirmation pour chaque action sensible
- Audit log des permissions
- Révocation facile des permissions

### 🎤 Modes de Contrôle
- **Mode texte**: Interface en ligne de commande
- **Mode vocal**: Reconnaissance et synthèse vocale
- **Mode GUI**: Interface graphique complète

### 🧠 IA Intégrée
- Basée sur OpenRouter (GPT-4 par défaut)
- Historique de conversation
- Parsing automatique des actions
- Réponses en français naturel

### 🎁 Options Supplémentaires
- Mode sombre par défaut
- Enregistrement macro de commandes
- Surveillance du système en temps réel
- Tâches planifiées
- Apprentissage des patterns

## 🚀 Installation

### Prérequis
- Python 3.8+
- Windows 10/11
- Clé API OpenRouter

### Étapes

1. **Cloner le repo**
   ```bash
   git clone https://github.com/vrcradio02/AI-Windows-Desktop-Assistant.git
   cd AI-Windows-Desktop-Assistant
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer l'API**
   ```bash
   cp .env.example .env
   # Éditer .env avec votre clé OpenRouter
   ```

5. **Lancer l'assistant**
   ```bash
   python main.py
   ```

## 📖 Utilisation

### Mode Texte
```bash
python main.py
# Choisir option 1
```

Exemples de commandes:
```
> Ouvre Firefox
> Prends une capture d'écran
> Quel est l'usage CPU?
> Clique à 500, 300
> Tape Hello World
```

### Mode Vocal
```bash
python main.py
# Choisir option 2
# Parlez en français
```

### Mode GUI
```bash
python main.py
# Choisir option 3
```

## 🔑 Clés API

Obtenir une clé OpenRouter:
1. Aller sur https://openrouter.io
2. S'inscrire/Se connecter
3. Copier la clé API
4. La mettre dans `.env`

## 📋 Architecture

```
├── main.py                 # Point d'entrée principal
├── ai_assistant.py         # Logique IA avec OpenRouter
├── system_controller.py    # Contrôle système Windows
├── permissions.py          # Gestion des permissions
├── voice_controller.py     # Reconnaissance/synthèse vocale
├── ui.py                   # Interface graphique Tkinter
├── config.py              # Configuration globale
├── requirements.txt       # Dépendances
└── README.md             # Documentation
```

## 🔐 Système de Permissions

L'assistant demande la permission avant chaque action sensible:

```
=========================================================
🔐 DEMANDE DE PERMISSION
=========================================================
Permission: control_mouse
Raison: Cliquer à (500, 300)

Voulez-vous autoriser cette action? (oui/non):
```

Les permissions sont stockées dans `permissions.json`:
```json
{
  "control_mouse": true,
  "control_keyboard": true,
  "launch_apps": false
}
```

## 🎯 Cas d'Usage

- **Automatisation**: Tâches répétitives
- **Accessibilité**: Contrôle par voix
- **Développement**: Tester l'UI automatiquement
- **Productivité**: Assistant personnel
- **Apprentissage**: Comprendre l'IA et l'automatisation

## ⚠️ Sécurité

- Toutes les permissions sont audit-loggées
- Aucune action sans confirmation
- Clé API en `.env` (pas en git)
- Failsafe PyAutoGUI activé (coin supérieur gauche = arrêt)

## 🆘 Troubleshooting

### Erreur: "No audio input detected"
```bash
# Installer PyAudio pour Windows
pip install pipwin
pipwin install pyaudio
```

### Erreur API OpenRouter
- Vérifier la clé API dans `.env`
- Vérifier la connexion internet
- Vérifier le quota API

### PyAutoGUI lent
- Augmenter `pyautogui_speed` dans `system_controller.py`
- Réduire les animations Windows

## 📄 Licence

MIT - Libre d'utilisation

## 🙏 Contributions

Les contributions sont bienvenues! Créez une PR.

## 📧 Support

Pour les problèmes, ouvrir une issue sur GitHub.

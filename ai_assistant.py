import requests
import json
from datetime import datetime
from typing import List, Dict, Any
from config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

class AIAssistant:
    def __init__(self, system_controller):
        self.sc = system_controller
        self.conversation_history = []
        self.api_key = OPENROUTER_API_KEY
        self.model = OPENROUTER_MODEL
        self.base_url = OPENROUTER_BASE_URL
        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self) -> str:
        """Construire le prompt système"""
        return """Tu es un assistant IA pour Windows Desktop. Tu peux:
- Contrôler la souris et le clavier
- Lancer des applications
- Prendre des captures d'écran
- Exécuter des commandes
- Lire/écrire le presse-papiers
- Obtenir les infos système

Sois toujours prudent et demande confirmation avant d'actions sensibles.
Tu dois respecter les permissions accordées par l'utilisateur.
Réponds de manière claire et concise en français.

Lorsque tu dois effectuer des actions, utilise le format suivant:
ACTION: [nom_action]
PARAMETRES: [paramètres]
RAISON: [pourquoi tu fais cela]
"""

    def send_message(self, user_message: str) -> str:
        """Envoyer un message à l'IA et obtenir une réponse"""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/vrcradio02/AI-Windows-Desktop-Assistant",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                *self.conversation_history
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            assistant_message = result['choices'][0]['message']['content']
            
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        except requests.exceptions.RequestException as e:
            return f"Erreur API: {str(e)}"

    def parse_action(self, response: str) -> Dict[str, Any]:
        """Parser la réponse pour extraire les actions"""
        action_dict = {
            'action': None,
            'parameters': {},
            'reason': '',
            'message': response
        }

        lines = response.split('\n')
        for line in lines:
            if line.startswith('ACTION:'):
                action_dict['action'] = line.replace('ACTION:', '').strip()
            elif line.startswith('PARAMÈTRES:'):
                try:
                    params_str = line.replace('PARAMÈTRES:', '').strip()
                    action_dict['parameters'] = json.loads(params_str)
                except:
                    action_dict['parameters'] = params_str
            elif line.startswith('RAISON:'):
                action_dict['reason'] = line.replace('RAISON:', '').strip()

        return action_dict

    def save_conversation(self, filename: str = None):
        """Sauvegarder la conversation"""
        if filename is None:
            filename = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)

    def clear_history(self):
        """Effacer l'historique"""
        self.conversation_history = []

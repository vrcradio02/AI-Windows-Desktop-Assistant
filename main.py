#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from permissions import PermissionManager
from system_controller import SystemController
from ai_assistant import AIAssistant
from voice_controller import VoiceController
from ui import DesktopAssistantUI
from config import REQUIRED_PERMISSIONS

class DesktopAssistant:
    def __init__(self):
        print("\n" + "="*60)
        print("🤖 ASSISTANT IA WINDOWS DESKTOP")
        print("="*60)
        
        # Initialiser les composants
        self.pm = PermissionManager()
        self.sc = SystemController(self.pm)
        self.ai = AIAssistant(self.sc)
        self.vc = VoiceController(use_gtts=False)
        self.ui = DesktopAssistantUI(self)
        
        # Demander les permissions initiales
        self._request_initial_permissions()

    def _request_initial_permissions(self):
        """Demander les permissions initiales"""
        print("\n📋 PERMISSIONS INITIALES")
        print("-" * 60)
        
        permissions_to_request = {
            'read_screen': 'Capturer l\'écran pour l\'analyse',
            'control_mouse': 'Contrôler la souris',
            'control_keyboard': 'Contrôler le clavier',
            'launch_apps': 'Lancer des applications',
            'execute_command': 'Exécuter des commandes',
            'system_info': 'Accéder aux infos système',
        }
        
        for permission, description in permissions_to_request.items():
            self.pm.request_permission(permission, description)

    def handle_user_input(self, user_input: str):
        """Traiter l'entrée utilisateur"""
        if not user_input.strip():
            return
        
        print(f"\n👤 Vous: {user_input}")
        
        # Obtenir la réponse de l'IA
        response = self.ai.send_message(user_input)
        print(f"\n🤖 Assistant: {response}")
        
        # Parser et exécuter les actions si nécessaire
        action = self.ai.parse_action(response)
        if action['action']:
            self._execute_action(action)
        
        # Feedback vocal optionnel
        if self.ui.voice_enabled:
            self.vc.speak(response)

    def _execute_action(self, action: dict):
        """Exécuter une action système"""
        action_name = action['action'].lower()
        params = action['parameters']
        
        print(f"\n⚙️ Exécution: {action_name}")
        print(f"📋 Raison: {action['reason']}")
        
        try:
            if action_name == 'move_mouse':
                self.sc.move_mouse(params.get('x'), params.get('y'))
            elif action_name == 'click':
                self.sc.click(params.get('x'), params.get('y'))
            elif action_name == 'type_text':
                self.sc.type_text(params.get('text'))
            elif action_name == 'press_key':
                self.sc.press_key(params.get('key'))
            elif action_name == 'launch_app':
                self.sc.launch_app(params.get('app'))
            elif action_name == 'screenshot':
                path = self.sc.take_screenshot(f"screenshot_{self._get_timestamp()}.png")
                print(f"✅ Capture sauvegardée: {path}")
            elif action_name == 'get_info':
                info = self.sc.get_system_info()
                print(f"ℹ️ Infos: {info}")
            elif action_name == 'execute_command':
                success, output = self.sc.execute_command(params.get('command'))
                print(f"📤 Résultat: {output}")
            else:
                print(f"⚠️ Action inconnue: {action_name}")
        except Exception as e:
            print(f"❌ Erreur: {e}")

    @staticmethod
    def _get_timestamp():
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')

    def run_text_mode(self):
        """Mode texte interactif"""
        print("\n💬 MODE TEXTE")
        print("Tapez 'exit' pour quitter, 'voice' pour mode vocal, 'help' pour l'aide\n")
        
        while True:
            try:
                user_input = input("\n> ").strip()
                
                if user_input.lower() == 'exit':
                    print("👋 Au revoir!")
                    break
                elif user_input.lower() == 'voice':
                    self.run_voice_mode()
                elif user_input.lower() == 'help':
                    self._show_help()
                elif user_input.lower() == 'permissions':
                    self._show_permissions()
                else:
                    self.handle_user_input(user_input)
            except KeyboardInterrupt:
                print("\n👋 Interruption...")
                break

    def run_voice_mode(self):
        """Mode vocal interactif"""
        print("\n🎤 MODE VOCAL")
        print("Dites 'stop' pour revenir au mode texte\n")
        
        self.vc.speak("Mode vocal activé")
        
        while True:
            user_input = self.vc.process_voice_command()
            if user_input is None:
                continue
            
            if user_input.lower() in ['stop', 'exit', 'quitter']:
                self.vc.speak("Retour au mode texte")
                break
            
            self.handle_user_input(user_input)

    def _show_help(self):
        """Afficher l'aide"""
        print("\n" + "="*60)
        print("📚 AIDE")
        print("="*60)
        print("""
Commandes disponibles:
  voice      - Basculer en mode vocal
  exit       - Quitter
  permissions - Gérer les permissions
  help       - Afficher cette aide

Exemples de commandes:
  "Ouvre Firefox"
  "Prends une capture d'écran"
  "Quel est l'usage CPU?"
  "Clique à 500, 300"
  "Tape Hello World"
  "Dis-moi l'heure"
        """)

    def _show_permissions(self):
        """Afficher les permissions"""
        print("\n" + "="*60)
        print("🔐 PERMISSIONS ACTUELLES")
        print("="*60)
        perms = self.pm.list_permissions()
        for perm, granted in perms.items():
            status = "✅ Accordée" if granted else "❌ Refusée"
            print(f"{perm:20} {status}")

def main():
    assistant = DesktopAssistant()
    
    print("\n🚀 Sélectionnez le mode:")
    print("1. Mode texte")
    print("2. Mode vocal")
    print("3. Interface GUI")
    
    choice = input("\nChoix (1-3): ").strip()
    
    if choice == '1':
        assistant.run_text_mode()
    elif choice == '2':
        assistant.run_voice_mode()
    elif choice == '3':
        assistant.ui.run()
    else:
        assistant.run_text_mode()

if __name__ == "__main__":
    main()

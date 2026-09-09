import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import threading

class DesktopAssistantUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.root = None
        self.voice_enabled = True
        self.dark_mode = True

    def run(self):
        """Lancer l'interface GUI"""
        self.root = tk.Tk()
        self.root.title("Assistant IA Windows Desktop")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e" if self.dark_mode else "#ffffff")
        
        self._create_widgets()
        self.root.mainloop()

    def _create_widgets(self):
        """Créer les widgets de l'interface"""
        # Style
        bg_color = "#1e1e1e" if self.dark_mode else "#ffffff"
        fg_color = "#00ff00" if self.dark_mode else "#000000"
        
        # En-tête
        header = tk.Frame(self.root, bg="#0d47a1" if self.dark_mode else "#1976d2", height=60)
        header.pack(fill=tk.X)
        
        title = tk.Label(header, text="🤖 Assistant IA Windows", font=("Arial", 16, "bold"),
                        bg="#0d47a1" if self.dark_mode else "#1976d2", fg="white")
        title.pack(pady=10)
        
        # Zone de conversation
        conv_frame = tk.LabelFrame(self.root, text="💬 Conversation", font=("Arial", 10, "bold"),
                                   bg=bg_color, fg=fg_color)
        conv_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.conversation_text = scrolledtext.ScrolledText(conv_frame, height=15, font=("Courier", 9),
                                                            bg="#0d0d0d" if self.dark_mode else "#f5f5f5",
                                                            fg=fg_color)
        self.conversation_text.pack(fill=tk.BOTH, expand=True)
        
        # Zone d'entrée
        input_frame = tk.Frame(self.root, bg=bg_color)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(input_frame, text="Votre message:", bg=bg_color, fg=fg_color).pack()
        
        self.input_text = tk.Entry(input_frame, font=("Arial", 10), width=80)
        self.input_text.pack(fill=tk.X, pady=5)
        self.input_text.bind("<Return>", lambda e: self._send_message())
        
        # Boutons de contrôle
        button_frame = tk.Frame(self.root, bg=bg_color)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="📤 Envoyer", command=self._send_message,
                 bg="#4CAF50", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="🎤 Vocal", command=self._toggle_voice,
                 bg="#2196F3", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="🔐 Permissions", command=self._show_permissions,
                 bg="#FF9800", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="ℹ️ Infos Système", command=self._show_system_info,
                 bg="#9C27B0", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="❌ Quitter", command=self.root.quit,
                 bg="#F44336", fg="white", font=("Arial", 10)).pack(side=tk.RIGHT, padx=5)
        
        # Afficher un message de bienvenue
        self._add_to_conversation("🤖 Assistant", "Bonjour! Je suis votre assistant IA. Comment puis-je vous aider?")

    def _send_message(self):
        """Envoyer un message"""
        message = self.input_text.get().strip()
        if not message:
            return
        
        self._add_to_conversation("👤 Vous", message)
        self.input_text.delete(0, tk.END)
        
        # Traiter en arrière-plan
        thread = threading.Thread(target=self._process_message, args=(message,))
        thread.daemon = True
        thread.start()

    def _process_message(self, message):
        """Traiter le message (en arrière-plan)"""
        try:
            response = self.assistant.ai.send_message(message)
            self._add_to_conversation("🤖 Assistant", response)
            
            # Exécuter les actions si nécessaire
            action = self.assistant.ai.parse_action(response)
            if action['action']:
                self.assistant._execute_action(action)
        except Exception as e:
            self._add_to_conversation("❌ Erreur", str(e))

    def _add_to_conversation(self, sender: str, message: str):
        """Ajouter un message à la conversation"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.conversation_text.insert(tk.END, f"[{timestamp}] {sender}: {message}\n\n")
        self.conversation_text.see(tk.END)

    def _toggle_voice(self):
        """Basculer le mode vocal"""
        self.voice_enabled = not self.voice_enabled
        status = "✅ Activé" if self.voice_enabled else "❌ Désactivé"
        messagebox.showinfo("Mode vocal", f"Synthèse vocale: {status}")

    def _show_permissions(self):
        """Afficher les permissions"""
        perms = self.assistant.pm.list_permissions()
        text = "🔐 PERMISSIONS ACTUELLES\n" + "="*40 + "\n"
        for perm, granted in perms.items():
            status = "✅" if granted else "❌"
            text += f"{status} {perm}\n"
        
        messagebox.showinfo("Permissions", text)

    def _show_system_info(self):
        """Afficher les infos système"""
        info = self.assistant.sc.get_system_info()
        text = "ℹ️ INFORMATIONS SYSTÈME\n" + "="*40 + "\n"
        for key, value in info.items():
            text += f"{key}: {value}\n"
        
        messagebox.showinfo("Infos Système", text)

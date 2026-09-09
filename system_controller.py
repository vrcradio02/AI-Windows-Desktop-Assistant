import pyautogui
import subprocess
import os
import time
import psutil
import platform
from typing import Tuple, Dict, Any
from PIL import ImageGrab
import pyperclip

class SystemController:
    def __init__(self, permission_manager):
        self.pm = permission_manager
        self.pyautogui_speed = 0.1
        pyautogui.FAILSAFE = True

    def move_mouse(self, x: int, y: int, duration: float = 1.0) -> bool:
        """Déplacer la souris"""
        if not self.pm.has_permission('control_mouse'):
            if not self.pm.request_permission('control_mouse', f'Déplacer la souris vers ({x}, {y})'):
                return False
        
        try:
            pyautogui.moveTo(x, y, duration=duration)
            return True
        except Exception as e:
            print(f"Erreur déplacement souris: {e}")
            return False

    def click(self, x: int = None, y: int = None, button: str = 'left', clicks: int = 1) -> bool:
        """Cliquer à une position"""
        if not self.pm.has_permission('control_mouse'):
            if not self.pm.request_permission('control_mouse', f'Cliquer à ({x}, {y})'):
                return False
        
        try:
            if x and y:
                pyautogui.moveTo(x, y)
            pyautogui.click(button=button, clicks=clicks)
            return True
        except Exception as e:
            print(f"Erreur clic: {e}")
            return False

    def type_text(self, text: str, interval: float = 0.1) -> bool:
        """Taper du texte"""
        if not self.pm.has_permission('control_keyboard'):
            if not self.pm.request_permission('control_keyboard', f'Taper: {text[:50]}...'):
                return False
        
        try:
            pyautogui.typewrite(text, interval=interval)
            return True
        except Exception as e:
            print(f"Erreur saisie: {e}")
            return False

    def press_key(self, key: str) -> bool:
        """Appuyer sur une touche"""
        if not self.pm.has_permission('control_keyboard'):
            if not self.pm.request_permission('control_keyboard', f'Appuyer sur {key}'):
                return False
        
        try:
            pyautogui.press(key)
            return True
        except Exception as e:
            print(f"Erreur touche: {e}")
            return False

    def hotkey(self, *keys) -> bool:
        """Appuyer sur plusieurs touches simultanément"""
        if not self.pm.has_permission('control_keyboard'):
            if not self.pm.request_permission('control_keyboard', f'Raccourci: {+"-".join(keys)}'):
                return False
        
        try:
            pyautogui.hotkey(*keys)
            return True
        except Exception as e:
            print(f"Erreur raccourci: {e}")
            return False

    def take_screenshot(self, save_path: str = None) -> Any:
        """Prendre une capture d'écran"""
        if not self.pm.has_permission('read_screen'):
            if not self.pm.request_permission('read_screen', 'Capturer l\'écran'):
                return None
        
        try:
            screenshot = ImageGrab.grab()
            if save_path:
                screenshot.save(save_path)
            return screenshot
        except Exception as e:
            print(f"Erreur capture: {e}")
            return None

    def get_clipboard(self) -> str:
        """Lire le presse-papiers"""
        if not self.pm.has_permission('read_clipboard'):
            if not self.pm.request_permission('read_clipboard', 'Lire le presse-papiers'):
                return ""
        
        try:
            return pyperclip.paste()
        except Exception as e:
            print(f"Erreur lecture presse-papiers: {e}")
            return ""

    def set_clipboard(self, text: str) -> bool:
        """Copier dans le presse-papiers"""
        if not self.pm.has_permission('write_clipboard'):
            if not self.pm.request_permission('write_clipboard', f'Copier: {text[:50]}...'):
                return False
        
        try:
            pyperclip.copy(text)
            return True
        except Exception as e:
            print(f"Erreur écriture presse-papiers: {e}")
            return False

    def launch_app(self, app_name: str, args: str = "") -> bool:
        """Lancer une application"""
        if not self.pm.has_permission('launch_apps'):
            if not self.pm.request_permission('launch_apps', f'Lancer: {app_name}'):
                return False
        
        try:
            if platform.system() == 'Windows':
                os.startfile(app_name)
            else:
                subprocess.Popen([app_name] + args.split())
            return True
        except Exception as e:
            print(f"Erreur lancement: {e}")
            return False

    def execute_command(self, command: str) -> Tuple[bool, str]:
        """Exécuter une commande shell"""
        if not self.pm.has_permission('execute_command'):
            if not self.pm.request_permission('execute_command', f'Exécuter: {command}'):
                return False, "Permission refusée"
        
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
            return True, result.stdout
        except Exception as e:
            return False, str(e)

    def get_system_info(self) -> Dict:
        """Obtenir les informations système"""
        if not self.pm.has_permission('system_info'):
            if not self.pm.request_permission('system_info', 'Accéder aux infos système'):
                return {}
        
        try:
            return {
                'os': platform.system(),
                'version': platform.version(),
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory': psutil.virtual_memory()._asdict(),
                'disk': psutil.disk_usage('/')._asdict(),
                'processes': len(psutil.pids())
            }
        except Exception as e:
            print(f"Erreur infos système: {e}")
            return {}

    def get_running_processes(self) -> list:
        """Lister les processus en cours"""
        if not self.pm.has_permission('system_info'):
            if not self.pm.request_permission('system_info', 'Lister les processus'):
                return []
        
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'status']):
                processes.append(proc.info)
            return processes
        except Exception as e:
            print(f"Erreur processus: {e}")
            return []

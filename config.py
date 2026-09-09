import os
from dotenv import load_dotenv

load_dotenv()

# Configuration OpenRouter
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_MODEL = "openai/gpt-4-turbo-preview"  # Ou gpt-3.5-turbo pour plus rapide
OPENROUTER_BASE_URL = "https://openrouter.io/api/v1"

# Configuration système
MAX_RETRIES = 3
TIMEOUT = 30
LOG_FILE = "assistant_logs.txt"

# Permissions par défaut (demander confirmation pour chacune)
REQUIRED_PERMISSIONS = {
    'execute_command': False,
    'control_mouse': False,
    'control_keyboard': False,
    'read_screen': False,
    'read_clipboard': False,
    'write_clipboard': False,
    'launch_apps': False,
    'system_info': False,
    'file_operations': False,
    'browser_control': False,
}

# Options supplémentaires
FEATURES = {
    'voice_control': True,
    'voice_feedback': True,
    'dark_mode_ui': True,
    'auto_save_logs': True,
    'learning_mode': True,
    'schedule_tasks': True,
    'macro_recording': True,
    'system_monitor': True,
    'screenshot_analysis': True,
}
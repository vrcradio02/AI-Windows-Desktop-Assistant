import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
from typing import Optional

class VoiceController:
    def __init__(self, use_gtts: bool = False):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.use_gtts = use_gtts
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)

    def listen(self) -> Optional[str]:
        """Écouter l'entrée vocale"""
        try:
            with sr.Microphone() as source:
                print("🎤 Écoute en cours...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=10)
                
            text = self.recognizer.recognize_google(audio, language='fr-FR')
            print(f"Vous avez dit: {text}")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Erreur de connexion au service de reconnaissance")
            return None

    def speak(self, text: str):
        """Parler un texte"""
        try:
            if self.use_gtts:
                tts = gTTS(text=text, lang='fr', slow=False)
                tts.save("temp_speech.mp3")
                os.system("start temp_speech.mp3" if os.name == 'nt' else "open temp_speech.mp3")
            else:
                self.engine.say(text)
                self.engine.runAndWait()
        except Exception as e:
            print(f"Erreur synthèse vocale: {e}")

    def process_voice_command(self) -> Optional[str]:
        """Traiter une commande vocale complète"""
        text = self.listen()
        if text:
            self.speak(f"J'ai entendu: {text}")
        return text

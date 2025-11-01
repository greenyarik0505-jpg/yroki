import os
import subprocess
import webbrowser
import pyttsx3
import speech_recognition as sr
import logging
import time
import sys

logging.basicConfig(
    filename=os.path.join(os.path.expanduser("~"), "assistant_log.txt"),
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# --------------------------
# Голосовой движок
# --------------------------
class VoiceEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.configure_russian_voice()
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 1.0)

    def configure_russian_voice(self):
        voices = self.engine.getProperty('voices')
        ru_voice = None
        for voice in voices:
            if "russian" in voice.name.lower() or "рус" in voice.name.lower():
                ru_voice = voice.id
                break
        if ru_voice:
            self.engine.setProperty('voice', ru_voice)

    def speak(self, text):
        print(f"💬 {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Ошибка TTS: {e}")

# --------------------------
# Распознавание речи
# --------------------------
class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self, prompt="Говорите..."):
        with sr.Microphone() as source:
            print(f"🎤 {prompt}")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=12)
                return self._process_audio(audio)
            except:
                return ""

    def _process_audio(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language="ru-RU")
        except:
            return ""
        replacements = {"точка": ".", "слеш": "/", "две точки": ":", "тире": "-", "подчеркивание": "_", "пробел": " "}
        words = text.lower().split()
        return " ".join([replacements.get(w, w) for w in words])

# --------------------------
# Работа с файлами
# --------------------------
class FileManager:
    def __init__(self, voice_engine):
        self.voice = voice_engine
        self.desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        self.documents = os.path.join(os.path.expanduser("~"), "Documents")
        self.current = os.getcwd()

    def create_file(self, filename=None, content=None):
        if not filename:
            self.voice.speak("Как назвать файл?")
            filename = input("Введите имя файла: ").strip() or VoiceRecognizer().listen()
        if not filename:
            self.voice.speak("Команда отменена")
            return
        file_path = os.path.join(self.desktop, f"{filename}.txt")
        if not content:
            self.voice.speak("Что записать в файл?")
            content = input("Введите текст: ").strip() or VoiceRecognizer().listen()
        if not content:
            self.voice.speak("Команда отменена")
            return
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.voice.speak(f"Файл {filename}.txt создан на рабочем столе.")
        except Exception as e:
            self.voice.speak(f"Ошибка при создании файла: {e}")

    def read_file(self, filename=None):
        if not filename:
            self.voice.speak("Скажите или введите имя файла.")
            filename = input("Введите имя файла: ").strip() or VoiceRecognizer().listen()
        if not filename:
            self.voice.speak("Команда отменена")
            return
        search_places = [
            os.path.join(self.desktop, f"{filename}.txt"),
            os.path.join(self.documents, f"{filename}.txt"),
            os.path.join(self.current, f"{filename}.txt")
        ]
        for file_path in search_places:
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    self.voice.speak(f"Содержимое файла: {content}")
                    return
                except:
                    self.voice.speak("Ошибка при чтении файла")
                    return
        self.voice.speak("Файл не найден.")

# --------------------------
# Работа с вебом
# --------------------------
class WebManager:
    def __init__(self, voice_engine):
        self.voice = voice_engine
        self.recognizer = VoiceRecognizer()

    def open_website(self, url=None):
        if not url:
            self.voice.speak("Какой сайт открыть?")
            url = input("Введите адрес сайта: ").strip() or self.recognizer.listen()
        if not url:
            self.voice.speak("Команда отменена")
            return
        if not url.startswith("http"):
            if "." in url:
                url = "https://" + url
            else:
                query = url.replace(" ", "+")
                url = f"https://www.google.com/search?q={query}"
        try:
            webbrowser.open(url)
            self.voice.speak(f"Открываю {url}")
        except:
            self.voice.speak("Не удалось открыть сайт")

    def open_youtube_channel(self, channel_name=None):
        if not channel_name:
            self.voice.speak("Скажите название канала")
            channel_name = self.recognizer.listen()
        if not channel_name:
            self.voice.speak("Команда отменена")
            return
        query = channel_name.replace(" ", "+")
        url = f"https://www.youtube.com/results?search_query={query}"
        try:
            webbrowser.open(url)
            self.voice.speak(f"Открываю канал {channel_name}")
        except:
            self.voice.speak("Не удалось открыть YouTube")

# --------------------------
# Поиск и запуск приложений с расчетом времени
# --------------------------
class AppManager:
    def __init__(self, voice_engine):
        self.voice = voice_engine
        self.desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        self.standard_folders = [
            os.environ.get("ProgramFiles", r"C:\Program Files"),
            os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"),
            os.path.join(os.path.expanduser("~"), "AppData\\Local"),
            os.path.join(os.path.expanduser("~"), "AppData\\Roaming")
        ]

    def find_and_run_app(self, app_name):
        app_name_clean = (app_name or "").strip().lower()
        if not app_name_clean:
            self.voice.speak("Скажите название приложения.")
            return False
        # Пропускаем если YouTube или сайт
        if any(word in app_name_clean for word in ["ютуб", "youtube", "http", ".", "сайт"]):
            return False

        start_time = time.time()
        self.voice.speak(f"Ищу {app_name_clean} на рабочем столе...")
        total_files = sum(len(files) for _, _, files in os.walk(self.desktop))
        checked_files = 0

        try:
            for root, dirs, files in os.walk(self.desktop):
                for f in files:
                    checked_files += 1
                    elapsed = time.time() - start_time
                    remaining = (elapsed / checked_files) * (total_files - checked_files) if checked_files else 0
                    print(f"Ищу... {checked_files}/{total_files}, прошло {int(elapsed)} с, осталось ~{int(remaining)} с", end="\r")
                    if app_name_clean in f.lower() and f.lower().endswith(".exe"):
                        full = os.path.join(root, f)
                        subprocess.Popen(full)
                        self.voice.speak(f"Открываю {f}")
                        return True

            self.voice.speak(f"Ищу {app_name_clean} в стандартных папках...")
            for folder in self.standard_folders:
                if not folder or not os.path.exists(folder):
                    continue
                for root, dirs, files in os.walk(folder):
                    for f in files:
                        if app_name_clean in f.lower() and f.lower().endswith(".exe"):
                            full = os.path.join(root, f)
                            subprocess.Popen(full)
                            self.voice.speak(f"Открываю {f}")
                            return True

            self.voice.speak(f"{app_name_clean} не найдено в стандартных местах. Начинаю поиск по дискам...")
            for drive_letter in "CDEFGHIJKLMNOPQRSTUVWXYZ":
                drive = f"{drive_letter}:/"
                if os.path.exists(drive):
                    for root, dirs, files in os.walk(drive):
                        for f in files:
                            if app_name_clean in f.lower() and f.lower().endswith(".exe"):
                                full = os.path.join(root, f)
                                subprocess.Popen(full)
                                self.voice.speak(f"Открываю {f}")
                                return True

            self.voice.speak(f"{app_name_clean} не найдено.")
            return False
        except KeyboardInterrupt:
            self.voice.speak("Поиск приложения прерван пользователем.")
            return False

# --------------------------
# Главный ассистент
# --------------------------
class Assistant:
    def __init__(self):
        self.voice = VoiceEngine()
        self.recognizer = VoiceRecognizer()
        self.file_manager = FileManager(self.voice)
        self.web_manager = WebManager(self.voice)
        self.app_manager = AppManager(self.voice)

    def run(self):
        self.voice.speak("Привет! Я современный голосовой ассистент.")
        last_active = time.time()

        try:
            while True:
                print("\n⌨️ Введите команду (или оставьте пустым для голоса): ")
                cmd = input().strip().lower()
                if not cmd:
                    cmd = self.recognizer.listen()
                if not cmd:
                    if time.time() - last_active > 180:
                        self.voice.speak("Три минуты тишины. Выключаюсь.")
                        break
                    continue
                last_active = time.time()

                if any(word in cmd for word in ["стоп", "выход", "отключись"]):
                    self.voice.speak("Отключаюсь. До свидания!")
                    break

                if "ютуб" in cmd and "канал" in cmd:
                    channel = cmd.replace("открой ютуб канал", "").strip()
                    self.web_manager.open_youtube_channel(channel)
                    continue

                if "создай файл" in cmd:
                    filename = cmd.replace("создай файл", "").strip() or None
                    self.file_manager.create_file(filename=filename)
                    continue
                if "прочитай файл" in cmd:
                    filename = cmd.replace("прочитай файл", "").strip() or None
                    self.file_manager.read_file(filename=filename)
                    continue

                if "открой сайт" in cmd or ("http" in cmd or "." in cmd):
                    site = cmd.replace("открой сайт", "").strip() or cmd
                    self.web_manager.open_website(site)
                    continue

                self.app_manager.find_and_run_app(cmd)
        except KeyboardInterrupt:
            self.voice.speak("Ассистент остановлен пользователем.")
            sys.exit(0)

if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()

import speech_recognition as sr
import pyttsx3
import os
import subprocess
import difflib
import time
import webbrowser

# Голос
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    ru_voice = None
    for voice in voices:
        if "russian" in voice.name.lower() or "рус" in voice.name.lower():
            ru_voice = voice.id
            break
    if ru_voice:
        engine.setProperty('voice', ru_voice)
    print(f"💬 {text}")
    engine.say(text)
    engine.runAndWait()

# Слушаем
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Скажите команду (или введите текст ниже)...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            query = recognizer.recognize_google(audio, language="ru-RU")
            print("Вы сказали:", query)
            return query.lower()
        except sr.WaitTimeoutError:
            return ""
        except:
            print("Не распознал")
            return ""

# Проверка путей и поиск exe
def try_paths(paths, app_name):
    tried = []
    for path in paths:
        real_path = os.path.expandvars(path)
        tried.append(real_path)
        if os.path.exists(real_path):
            subprocess.Popen(real_path)
            speak(f"Открываю {app_name}")
            return True

    # Автопоиск exe
    standard_dirs = [
        r"C:\Program Files",
        r"C:\Program Files (x86)",
        os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Local"),
        os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Roaming")
    ]
    for folder in standard_dirs:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if app_name.lower().replace(" ", "") in file.lower().replace(" ", "") and file.endswith(".exe"):
                    exe_path = os.path.join(root, file)
                    subprocess.Popen(exe_path)
                    speak(f"Открываю {app_name} (найдено автоматически)")
                    return True

    speak(f"Не удалось открыть {app_name}")
    return False

# Открытие YouTube по имени канала
def open_youtube_channel():
    speak("Кого YouTube-канал вы хотите открыть?")
    channel_name = input("Введите имя канала или скажите: ").strip()
    if not channel_name:
        channel_name = listen()
    if not channel_name:
        speak("Я не понял. Команда отменена")
        return
    search_query = channel_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)
    speak(f"Открываю результаты поиска для {channel_name} на YouTube")

# Основной запуск программ
def run_program_exact(command):
    command = command.lower()
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe"
    ]
    telegram_paths = [
        r"C:\Users\%USERNAME%\AppData\Roaming\Telegram Desktop\Telegram.exe",
        r"C:\Program Files\Telegram Desktop\Telegram.exe",
        r"D:\Telegram Desktop\Telegram.exe"
    ]
    roblox_paths = [
        r"C:\Users\%USERNAME%\AppData\Local\Roblox\Versions\RobloxPlayerLauncher.exe",
        r"C:\Users\%USERNAME%\AppData\Local\Roblox\Versions\version-d34359a5577645e2\RobloxPlayerBeta.exe"
    ]
    explorer_paths = [
        r"C:\Windows\explorer.exe"
    ]

    if "калькулятор" in command:
        os.system("start calc")
        speak("Открываю калькулятор")
        return True
    if "блокнот" in command:
        os.system("start notepad")
        speak("Открываю блокнот")
        return True
    if "гугл" in command or "chrome" in command or "браузер" in command:
        return try_paths(chrome_paths, "Google Chrome")
    if "чат гпт" in command or "chat gpt" in command:
        webbrowser.open("https://chat.openai.com")
        speak("Открываю ChatGPT")
        return True
    if "телеграм" in command or "telegram" in command:
        return try_paths(telegram_paths, "Telegram")
    if "роблокс" in command or "roblox" in command:
        return try_paths(roblox_paths, "Roblox")
    if "проводник" in command or "файлы" in command:
        return try_paths(explorer_paths, "Проводник")
    if "ютуб" in command or "youtube" in command:
        open_youtube_channel()
        return True
    return False

# Работа с файлами
def file_action(command):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    documents = os.path.join(os.path.expanduser("~"), "Documents")
    current = os.getcwd()

    if "создай файл" in command:
        speak("Как назвать файл?")
        filename = input("Введите имя файла: ").strip()
        if not filename:
            filename = listen()
        if not filename:
            speak("Я не понял. Команда отменена")
            return
        file_path = os.path.join(desktop, f"{filename}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            speak("Что записать в файл?")
            content = input("Введите текст: ").strip()
            if not content:
                content = listen()
            if not content:
                speak("Я не понял. Команда отменена")
                return
            f.write(content)
        speak(f"Файл {filename}.txt создан на рабочем столе.")
    elif "прочитай файл" in command:
        speak("Скажи или введи имя файла.")
        filename = input("Введите имя файла: ").strip()
        if not filename:
            filename = listen()
        if not filename:
            speak("Я не понял. Команда отменена")
            return
        search_places = [
            os.path.join(desktop, f"{filename}.txt"),
            os.path.join(documents, f"{filename}.txt"),
            os.path.join(current, f"{filename}.txt")
        ]
        found = False
        for file_path in search_places:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                speak(f"Содержимое файла: {content}")
                found = True
                break
        if not found:
            speak("Файл не найден. Команда отменена")

# Подтверждение команды
def confirm_and_run(suggestion):
    speak(f"Ты это имел в виду: {suggestion}?")
    answer = input("Ответ (да/нет) или скажите голосом: ").strip().lower()
    if not answer:
        answer = listen()
    yes_words = ["да", "ага", "именно", "конечно", "правильно", "точно"]
    no_words = ["нет", "не"]
    if any(word in answer for word in yes_words):
        if "создай файл" in suggestion or "прочитай файл" in suggestion:
            file_action(suggestion)
        elif "что ты можешь" in suggestion or "что умеешь" in suggestion:
            list_capabilities()
        else:
            run_program_exact(suggestion.lower())
    elif any(word in answer for word in no_words):
        speak("Команда отменена")
    else:
        speak("Я не понял. Команда отменена")

# Что умеет ассистент
def list_capabilities():
    capabilities = [
        "Я могу открывать Chrome, Telegram, Roblox, проводник, YouTube, калькулятор и блокнот.",
        "Я могу создавать и читать текстовые файлы.",
        "Я могу открыть сайт ChatGPT.",
        "Я могу искать YouTube-каналы.",
        "Если приложение не найдено, я попробую найти его автоматически.",
        "Если ты молчишь три минуты, я выключаюсь.",
        "Я спрашиваю подтверждение, если не уверен, что ты имел в виду.",
        "Теперь ты можешь не только говорить, но и писать команды вручную."
    ]
    speak("Вот что я умею:")
    for line in capabilities:
        speak(line)

# Основной цикл
def assistant_loop():
    speak("Привет! Я твой голосовой помощник.")
    known_commands = [
        "открой калькулятор", "открой гугл", "открой телеграм", "открой роблокс",
        "открой блокнот", "создай файл", "прочитай файл", "привет",
        "открой ютуб", "открой чат гпт", "открой проводник",
        "что ты можешь", "что умеешь"
    ]

    last_active = time.time()
    while True:
        print("\n⌨️ Введите команду (или оставьте пустым, чтобы говорить): ")
        text_input = input().strip().lower()
        if text_input:
            command = text_input
        else:
            command = listen()

        if command:
            last_active = time.time()
        else:
            if time.time() - last_active > 180:
                speak("Три минуты тишины. Выключаюсь.")
                break
            continue

        if any(word in command for word in ["стоп", "отключись"]):
            speak("Отключаюсь. До свидания!")
            break
        if "что ты можешь" in command or "что умеешь" in command:
            list_capabilities()
            continue
        if run_program_exact(command):
            continue
        elif "создай файл" in command or "прочитай файл" in command:
            file_action(command)
        elif "привет" in command:
            speak("Привет, чем помочь?")
        else:
            suggestion = difflib.get_close_matches(command, known_commands, n=1, cutoff=0.6)
            if suggestion:
                confirm_and_run(suggestion[0])
            else:
                speak("Я не понял. Команда отменена")

if __name__ == "__main__":
    assistant_loop()

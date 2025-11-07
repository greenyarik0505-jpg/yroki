# """Перше це ми встановлюємо бібліотеку
# pip install SpeechRecognition"""
# # ЩЕ ОДНА БІБЛІОТЕКА це pyaudio - бібліотека для роботи з мікрофоном
# """pip install pyaudio"""
# import speech_recognition as sr
# recognizer = sr.Recognizer() # Ініціалізація розпізнавача , підключення класу Recognizer
# print("Бібліотека встановлена")
# for index,name in enumerate(sr.Microphone.list_microphone_names()): # Отримати список мікрофонів
#     print(f"Мікрофон номер {index} - {name}") # Вивести список мікрофонів
# #Налаштування мікрофону "ДУЖЕ ВАЖЛИВО!!!!!!!!!!!!!!!!!!!!!"
# recognizer.energy_threshold = 4000 # Поріг шуму для визначення мови
# recognizer.dynamic_energy_threshold = True # Динамічне налаштування порогу шум
# recognizer.pause_threshold = 2 # Пауза між словами
# with sr.Microphone(device_index=1) as source: # Вказуєте індекс мікрофона який в вас робочий 
#     print("Можеш починати говорити ")
#     recognizer.adjust_for_ambient_noise(source,duration=0.5) # підключити ШУМОДАВ
#     audio = recognizer.listen(source) # підключаємо звук і записуємо його
# try:
#     text = recognizer.recognize_google(audio,language="uk-UA") #Розпізнаємо звук за допомогою гугла 
#     print(f"Ви сказали {text}")
# except sr.UnknownValueError: # 
#     print("Я вас не чую! ")

import pyautogui
import time
import speech_recognition as sr
recognizer = sr.Recognizer()
print("Ласкаво просимо в нашу розумну програму Tun tun Programun")
while True:
    print("=======================ОБЕРІТЬ ДІЮ============================= \n 1. Відкрити YouTube \n 2. Відкрити браузер \n 3. Відкрити Блокнот \n 4. Відкрити калькулятор \n 5. Відкрити Telegram \n 6. Відкрити Visual Studio Code \n 7. Відкрити Roblox \n 8. Відкрити Viber \n 9. Відкрити Microsoft Store \n 10. Відкрити Захист Windows \n 11. Дізнатися погоду \n 12. Відкрити Провідник \n 13. Відкрити Диспетчер завдань \n 14. Відкрити Paint \n 15. Відкрити Корзину\n 16. Відкрити сайт \n 17. Зробити знімок екрану \n 18. Відкрити Календар\n 19. Відкрити Командний рядок\n 20. Відкрити Налаштування Windows")
    recognizer.energy_threshold = 4000
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 2
    with sr.Microphone(device_index=1) as source:
        print("Можеш починати говорити ")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio,language="uk-UA")
        print(f"Ви сказали {text}")
    except sr.UnknownValueError: # 
        print("Я вас не чую! ")
        continue
    
    text_lower = text.lower() 

    pyautogui.alert("Увага зараз програма почне працювати йдіть попийте чай ")
    
    # 1. Відкрити YouTube
    if text_lower == "1" or text_lower == "один" or text_lower == "раз" or text_lower == "відкрити ютуб":
        with sr.Microphone(device_index=1) as source:
            print("Можеш починати говорити (ім'я ютубера)")
            recognizer.adjust_for_ambient_noise(source,duration=0.5)
            audio_inner = recognizer.listen(source)
        try:
            text_inner = recognizer.recognize_google(audio_inner,language="uk-UA") 
            print(f"Ви сказали {text_inner}")
        except sr.UnknownValueError: # 
            print("Я вас не чую! ")
            text_inner = None
            
        if text_inner:
            print(f"Шукаю ютубера {text_inner}...")
            time.sleep(2)
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge", interval=0.10)
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write(f"https://www.youtube.com/@{text_inner}", interval=0.10) 
            pyautogui.press("enter")
        else:
            pyautogui.alert("Ви не ввели ютубера! відкривається просто ютуб або що у тебе в пошуку")
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge", interval=0.10)
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write("https://www.youtube.com", interval=0.10)
            pyautogui.press("enter")
            
    # 2. Відкрити браузер
    elif text_lower == "2" or text_lower == "два" or text_lower == "двое" or text_lower == "відкрити браузер":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"msedge", interval=0.10)
        pyautogui.press("enter")

    # 3. Відкрити Блокнот
    elif text_lower == "3" or text_lower == "три" or text_lower == "трійка" or text_lower == "відкрити блокнот":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"notepad", interval=0.10)
        pyautogui.press("enter")

    # 4. Відкрити калькулятор
    elif text_lower == "4" or text_lower == "чотири" or text_lower == "четыре" or text_lower == "відкрити калькулятор":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"calc", interval=0.10)
        pyautogui.press("enter")

    # 5. Відкрити Telegram
    elif text_lower == "5" or text_lower == "п'ять" or text_lower == "пять" or text_lower == "відкрити telegram":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"D:\Telegram Desktop\Telegram.exe", interval=0.10) 
        pyautogui.press("enter")

    # 6. Відкрити Visual Studio Code
    elif text_lower == "6" or text_lower == "шість" or text_lower == "шесть" or text_lower == "відкрити visual studio code":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"D:\Microsoft VS Code\Code.exe", interval=0.10) 
        pyautogui.press("enter")

    # 7. Відкрити Roblox
    elif text_lower == "7" or text_lower == "сім" or text_lower == "семь" or text_lower == "відкрити roblox":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"roblox-player:1", interval=0.10)
        pyautogui.press("enter")

    # 8. Відкрити Viber
    elif text_lower == "8" or text_lower == "вісім" or text_lower == "восемь" or text_lower == "відкрити viber":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"C:\Users\%USERNAME%\AppData\Local\Viber\Viber.exe", interval=0.10) 
        pyautogui.press("enter")

    # 9. Відкрити Microsoft Store
    elif text_lower == "9" or text_lower == "дев'ять" or text_lower == "девять" or text_lower == "відкрити microsoft store":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"ms-windows-store:", interval=0.10)
        pyautogui.press("enter")

    # 10. Відкрити Захист Windows
    elif text_lower == "10" or text_lower == "десять" or text_lower == "відкрити захист windows":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"ms-settings:windowsdefender", interval=0.10)
        pyautogui.press("enter")

    # 11. Дізнатися погоду
    elif text_lower == "11" or text_lower == "одинадцять" or text_lower == "одиннадцать" or text_lower == "дізнатися погоду":
        with sr.Microphone(device_index=1) as source:
            print("Можеш починати говорити (назва міста)")
            recognizer.adjust_for_ambient_noise(source,duration=0.5)
            audio_inner = recognizer.listen(source)
        try:
            text_inner = recognizer.recognize_google(audio_inner,language="uk-UA") 
            print(f"Ви сказали {text_inner}")
        except sr.UnknownValueError: # 
            print("Я вас не чую! ")
            
        if text_inner:
            print(f"Шукаю погоду в місті {text_inner}...")
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge")
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write(f"Weather in {text_inner}", interval=0.10)
            pyautogui.press("enter")
        else:
            pyautogui.alert("Ви не ввели назву міста! Шукаю погоду у вашому місті")
            pyautogui.hotkey("win", "r")
            pyautogui.write("msedge")
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write("Weather" , interval=0.10)
            pyautogui.press("enter")

    # 12. Відкрити Провідник
    elif text_lower == "12" or text_lower == "дванадцять" or text_lower == "двенадцать" or text_lower == "відкрити провідник":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"explore", interval=0.10)
        pyautogui.press("enter")

    # 13. Відкрити Диспетчер завдань
    elif text_lower == "13" or text_lower == "тринадцять" or text_lower == "тринадцать" or text_lower == "відкрити диспетчер завдань":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"taskmgr", interval=0.10)
        pyautogui.press("enter")

    # 14. Відкрити Paint
    elif text_lower == "14" or text_lower == "чотирнадцять" or text_lower == "четырнадцать" or text_lower == "відкрити paint":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"mspaint", interval=0.10)
        pyautogui.press("enter")

    # 15. Відкрити Корзину
    elif text_lower == "15" or text_lower == "п'ятнадцять" or text_lower == "пятнадцать" or text_lower == "відкрити корзину":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"explorer.exe shell:RecycleBinFolder", interval=0.10)
        pyautogui.press("enter")

    # 16. Відкрити сайт
    elif text_lower == "16" or text_lower == "шістнадцять" or text_lower == "шестнадцать" or text_lower == "відкрити сайт":
        with sr.Microphone(device_index=1) as source:
            print("Можеш починати говорити (назва сайту)")
            recognizer.adjust_for_ambient_noise(source,duration=0.5)
            audio_inner = recognizer.listen(source)
        try:
            text_inner = recognizer.recognize_google(audio_inner,language="uk-UA") 
            print(f"Ви сказали {text_inner}")
        except sr.UnknownValueError: # 
            print("Я вас не чую! ")
            text_inner = None
            
        if text_inner:
            print(f"Шукаю сайт {text_inner}...")
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge")
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write(f"https://www.{text_inner}", interval=0.10) 
            pyautogui.press("enter")
        else:
            pyautogui.alert("Ви не ввели сайт команда отменена!")

    # 17. Зробити знімок екрану
    elif text_lower == "17" or text_lower == "сімнадцять" or text_lower == "семнадцать" or text_lower == "зробити знімок екрану":
        time.sleep(2)
        pyautogui.screenshot("screen.png")

    # 18. Відкрити Календар
    elif text_lower == "18" or text_lower == "вісімнадцять" or text_lower == "восемнадцать" or text_lower == "відкрити календар":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"outlookcal:", interval=0.10)
        pyautogui.press("enter")

    # 19. Відкрити Командний рядок
    elif text_lower == "19" or text_lower == "дев'ятнадцять" or text_lower == "девятнадцать" or text_lower == "відкрити командний рядок":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"cmd", interval=0.10)
        pyautogui.press("enter")

    # 20. Відкрити Налаштування Windows
    elif text_lower == "20" or text_lower == "двадцять" or text_lower == "двадцать" or text_lower == "відкрити налаштування windows":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"ms-settings:", interval=0.10)
        pyautogui.press("enter")
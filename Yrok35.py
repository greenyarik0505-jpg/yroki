# Завдання 1: Твоя перша програма
# Створи програму, яка представиться твоїм іменем та розкаже три цікаві факти про тебе. Наприклад:
# Твоє ім'я та вік
# Твоє хобі
# Твій улюблений предмет у школі

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Привіт, мене звати Робот Убийца 3000!")
# engine.say("Привіт, моє улюблене хоби красть брейнритов!")
# engine.say("Привіт, мой улюблений предмет інформатика")
# engine.runAndWait()

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Я говорю")
# volume = engine.getProperty("volume") # Отримати поточний рівень гучності
# print(f"Поточний рівень гучності: {volume}")
# engine.setProperty("volume", 0.5) # Встановити рівень гучності (0.0 до 1.0) 0.5 - 50% 
# engine.say("Я тепер говорю тихіше")
# print(f"Поточний рівень гучності: {volume}")
# engine.runAndWait()

# import pyttsx3
# engine = pyttsx3.init()
# volume = engine.getProperty("volume") # Отримати поточний рівень гучності
# print(f"Поточний рівень гучності: {volume}")
# engine.setProperty("volume", 0.5) # Встановити рівень гучності (0.0 до 1.0) 0.5 - 50% 
# engine.say("Я тепер говорю тихіше")
# print(f"Поточний рівень гучності: {volume}") # Змінили гучність
# rate = engine.getProperty("rate")
# print(f"Поточна швидкість {rate}")
# engine.setProperty("rate",120)
# engine.say("Я говорю повільно")
# engine.setProperty("rate",300)
# engine.say("Я говорю швидко")
# engine.runAndWait()

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty("voices") # Виводимо інформацію про кожен голос
# for index,voice in enumerate(voices):
#     print(f"Голос {index}")
#     print(f" - ID {voice.id}")
#     print(f" - Ім'я {voice.name}")
#     print(f" - Мови {voice.languages}")
#     print()
# engine.setProperty("voice",voices[0].id)
# engine.say("Це мій голос ")
# engine.runAndWait()

#Для кожного голосу використовує різну швидкість (повільно, нормально, швидко)
# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty("rate",120)
# engine.say("Я говорю повільно")
# engine.setProperty("rate",170)
# engine.say("Я говорю нормально")
# engine.setProperty("rate",300)
# engine.say("Я говорю швидко")
# engine.runAndWait()

#--------Домашка

# Створи програму, яка вітається голосом, запитує ім'я та настрій користувача.
# Що повинна робити програма:
# Привітати користувача
# Запитати ім'я
# Запитати настрій (добрий/поганий)
# Відповісти залежно від настрою

import pyttsx3
engine = pyttsx3.init()
engine.say("Привіт")
engine.say("Як до тебе звертатися ")
name = input("Введіть як до тебе звертатися: ")
engine.say("Якій у тебе настрій (добрий/поганий)").lower()
nastrui = input("Введіть якій у тебе настрій (добрий/поганий): ")
if nastrui == "добрий":
    engine.say("Добре ")
if nastrui == "поганий":
    engine.say("Погано")
engine.runAndWait()

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty("voices") # Виводимо інформацію про кожен голос
# for index,voice in enumerate(voices):
#     print(f"Голос {index}")
#     print(f" - ID {voice.id}")
#     print(f" - Ім'я {voice.name}")
#     print(f" - Мови {voice.languages}")
# engine.runAndWait()
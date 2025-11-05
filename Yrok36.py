# TKINTER GUI для голосового помічника
# import tkinter as tk
# import pyttsx3
# """Обов'язково=============="""
# window = tk.Tk() # Створення вікна
# window.geometry("800x600") # Розмір вікна
# window.title("Tutorial") # Назва вікна

# engine = pyttsx3.init()
# voices = engine.getProperty("voices") # Виводимо інформацію про кожен голос
# for index,voice in enumerate(voices):
#     print(f"Голос {index}")
#     print(f" - ID {voice.id}")
#     print(f" - Ім'я {voice.name}")
#     print(f" - Мови {voice.languages}")
#     print()
# engine.setProperty("voice",voices[1].id)
# rate = engine.getProperty("rate")
# engine.setProperty("rate",120) # Змінити швидкість мовлення 
# engine.setProperty("voice",voices[1].id)
# """"======================="""


# """"Label - це текст на екрані, який можна розмістити наприклад над кнопкою або залишити просто як назва програми """

# label1 = tk.Label(window,text = "Текст для прикладу ",bg="#FCE300",font=("Times New Roman",14),fg="#361974") # Створення надпису (вікно до якого належить, текст, опції)
# label1.pack(pady=5) #Розмістити на екрані (відступ від попереднього елементу )

# """"==============================================================================================================="""



# """Button - це кнопка з якою ми можемо взаємодіяти  і вона виконує функцію яку ми вкажемо"""
# """Створюємо деф перед кнопкою """
# def hello():
#     engine.say("Привіт")
# button1 = tk.Button(window, text="текст на кнопці",command=hello)# Створення надпису (вікно до якого належить, текст, команда = функція яка має виконуватись)
# button1.pack()


# """"==============================================================================================================="""

# """Entry - це поле вводу , який можна назвати графічний інпут"""
# def прочитати():
#     a = entry1.get() # Отримати написане значення 
#     """Увага"""
#     print(type(a)) # Було STR
#     a = int(entry1.get()) # Отримати написане число або цифру 
#     print(type(a)) # стало інт, можна обчислювати
#     """====="""
#     engine.say(f"{a}") # змінні в say потрібно вставляти через f-рядок 
# entry1 = tk.Entry(window,width=20) # width - це ширина де ми вказуємо в пікселях
# entry1.pack()
# button2 = tk.Button(window, text="текст на кнопці",command=прочитати)# Створення надпису (вікно до якого належить, текст, команда = функція яка має виконуватись)
# button2.pack()
# engine.runAndWait() # ОБОВ'язково в кінці
# window.mainloop() # ОБОВ'язково в кінці

import tkinter as tk
import pyttsx3
window = tk.Tk()
window.geometry("800x600")
window.title("Calculator tun tun sahura")
engine = pyttsx3.init()
def mnozuni():
    a = int(entry1.get())
    d = int(entry2.get())
    dorivnue = a * d
    engine.say(f"{dorivnue}")
def nodeluti():
    a = int(entry1.get())
    d = int(entry2.get())
    if d == 0:
        engine.say("Нельзя делить на нуль")
    else:
        dorivnue = a // d
        engine.say(f"{dorivnue}")
def plys():
    a = int(entry1.get())
    d = int(entry2.get())
    dorivnue = a + d
    engine.say(f"{dorivnue}")
def minus():
    a = int(entry1.get())
    d = int(entry2.get())
    dorivnue = a - d
    engine.say(f"{dorivnue}")
label1 = tk.Label(window,text = "Введіть перше число")
label1.pack(pady=5)
entry1 = tk.Entry(window,width=20)
entry1.pack()
label2 = tk.Label(window,text = "Введіть перше число")
label2.pack(pady=5)
entry2 = tk.Entry(window,width=20)
entry2.pack()
button1 = tk.Button(window, text="Плюс",command=plys)
button1.pack()
button2 = tk.Button(window, text="Минус",command=minus)
button2.pack()
button3 = tk.Button(window, text="Множення",command=mnozuni)
button3.pack()
button4 = tk.Button(window, text="Поделить",command=nodeluti)
button4.pack()
engine.runAndWait()
window.mainloop()

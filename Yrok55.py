# # Приклад програмки з нашими елементами
# import tkinter as tk # імпорт бібліотеки tkinter
# window = tk.Tk()   # створення вікна
# window.title("Шаблон") # назва вікна
# window.geometry("400x300") # розмір вікна
# window.config(bg="lightblue") # колір вікна

# # створення напису
# text = tk.Label(window,text="Hello World",bg="lightgreen") # напис на вікні
# text.pack(pady=10,padx=10) # розміщення напису на вікні

# # створення поля вводу
# entry = tk.Entry(window) # поле вводу
# entry.pack(pady=10)

# # кнопка яка змінює напис на вікні і вставляє його з ентрі
# def changetext():
#     textentry = entry.get() # отримання тексту з поля вводу
#     text.config(text=textentry) # зміна напису на вікні

# button = tk.Button(window,text="Змінити напис",command=changetext,bg="lightgreen") # кнопка
# button.pack(pady=10,padx=10) # розміщення кнопки на вікні

# window.mainloop() # запуск головного циклу вікна





# Задачка 3: 🔒 Секретний сейф
# Завдання: Створи програму, яка перевіряє секретний пароль.
# Як це має працювати: На екрані є напис "Введи пароль:".
# Ти вводиш цифри у поле. Якщо ти ввів правильний пароль (наприклад, 1234), напис змінюється на "СЕЙФ ВІДКРИТО!", а фон напису стає зеленим.
# Якщо пароль неправильний — напис змінюється на "ПОМИЛКА!", а його фон стає червоним.
# (Тут знадобиться конструкція if ... else)

# import tkinter as tk
# window = tk.Tk()
# window.title("Секретний сейф")
# window.geometry("400x300")

# paroli = "1234"

# label = tk.Label(window,text="Ожидаем пароль",bg="black",fg="white")
# label.pack(pady=10,padx=10)

# entry = tk.Entry(window)
# entry.pack(pady=10)

# def proverka():
#     paroli1 = entry.get()
#     if paroli == paroli1:
#         label.config(text="СЕЙФ ВІДКРИТО!")
#         label.config(fg="green")
#     else:
#         label.config(text="ПОМИЛКА!")
#         label.config(fg="red")

# button = tk.Button(window,text="Проверка",command=proverka,bg="lightgreen")
# button.pack(pady=10,padx=10)

# window.mainloop()






# Задачка 7: 🤖 Робот-лічильник (Рентген для слів)
# Завдання: Створи програму, яка вміє рахувати, скільки букв у слові, яке ти їй даєш.
# Як це має працювати: На екрані є напис "Яке слово перевірити?". Ти вводиш у поле якесь довге слово (наприклад, Програмування). Натискаєш кнопку "Просканувати", і напис змінюється на: "У цьому слові 13 літер!".
# Якщо введеш Кіт, напис покаже "У цьому слові 3 літер!".
# Секретна підказка: У Python є спеціальна команда-лінійка, яка вміє вимірювати довжину чого завгодно. Вона називається len() (від англійського слова length — довжина).
# Працює вона так: kilkist_liter = len(entry.get())

import tkinter as tk
window = tk.Tk()
window.title("🤖 Робот-лічильник")
window.geometry("400x300")

label = tk.Label(window,text="Ожидаем",bg= "white",fg="black")
label.pack(pady=10,padx=10)

entry = tk.Entry(window)
entry.pack(pady=10)

def proverka():
    entry1 = entry.get()
    if "" != entry1:
        liter = entry.get()
        kilkist_liter = len(liter)
        label.config(fg="black")
        label.config(text=f"Кількість слів {kilkist_liter}")
    else:
        label.config(fg="red")
        label.config(text="ПОМИЛКА!")

button = tk.Button(window,text="Проверка",command=proverka,bg="lightgreen")
button.pack(pady=10,padx=10)

window.mainloop()

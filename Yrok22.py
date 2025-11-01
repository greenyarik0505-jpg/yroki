# import tkinter as tk
# import random
# from tkinter import ttk #ткінтер стильовий )
# word = ["Яблуко","Груша","Книга","Кружка","Шкаф"]
# secret=random.choice(word)
# def check():
#     user = entry.get()
#     if user == secret:
#         label2.config(text="Правильно!!!!!",foreground="green")
#         button1.config(state="disabled")
#         entry.config(state="disabled")
#     else:
#         label2.config(text="Неправильно!!!!!",foreground="red")
#         entry.delete(0,"end")
    
# window = tk.Tk()
# window.title("Вгадай слово")
# window.geometry("500x300")
# label1= ttk.Label(window,text="Я загадав слово, спробуй його відгадати",font=("Arial",12)).pack(pady=20)
# entry = ttk.Entry(window,font=("Arial",14),justify="center") #розмістити по горизонталі в центрі
# entry.pack(pady=10)
# button1=ttk.Button(window,text="Перевірити",command = check)
# button1.pack(pady=10)
# label2 = ttk.Label(window,text="",font=("Arial",14,"bold")) # bold - жирний шрифт
# label2.pack(pady=10)
# window.mainloop()

#Вгадай слово 

# import ttkbootstrap as ttk
# import random
# from ttkbootstrap.constants import *

# word = ["Яблуко","Груша","Книга","Кружка","Шкаф"]
# secret=random.choice(word)
# def check():
#     user = entry.get()
#     if user == secret:
#         label2.config(text="Правильно!!!!!",foreground="green")
#         button1.config(state="disabled")
#         entry.config(state="disabled")
#     else:
#         label2.config(text="НеПравильно!!!!!",foreground="red")
#         entry.delete(0,"end")
    
# window = ttk.Window(themename="minty") 
# # cyborg , journal , flatly , litera , darkly
# window.title("Вгадай слово")
# window.geometry("500x300")

# # Створити об'єкт стилю
# # style = ttk.Style()
# # style.theme_use("clam")

# # style.configure("TLabel",font=("Helvtica",12))
# # style.configure("TButton",font=("Helvetica",12,"bold"),padding=5)
# # style.configure("TEntry",font=("Helvetica",14),padding = 5)
# # window.configure(bg="#f0f0f0")


# label1= ttk.Label(window,text="Я загадав слово, спробуй його відгадати",font=("Arial",12)).pack(pady=20)
# entry = ttk.Entry(window,font=("Arial",14),justify="center") #розмістити по горизонталі в центрі
# entry.pack(pady=10)
# button1=ttk.Button(window,text="Перевірити",command = check)
# button1.pack(pady=10)

# label2 = ttk.Label(window,text="",font=("Arial",14,"bold")) # bold - жирний шрифт
# label2.pack(pady=10)

# window.mainloop()

#Задача, створити програму яка при нажиманні на кнопку перевертає текст, який був введений в entry

# import ttkbootstrap as tk
# from ttkbootstrap.constants import *
# def reverse():
#     text = entry.get()
#     textreverse = text[::-1]
#     label2.config(text=f"Результат {textreverse}")


# window = tk.Window(themename="solar")
# window.title("Перевертач тексту")
# window.geometry("400x250")

# label1=tk.Label(window,text="Введіть текст для перевертання")
# label1.pack(pady = 10)

# entry = tk.Entry(window)
# entry.pack(pady=5)

# button= tk.Button(window,text="Перевернути",command=reverse)
# button.pack(pady=10)

# label2 = tk.Label(window,text="Результат: ")
# label2.pack()

# window.mainloop()

# import ttkbootstrap as tk
# from ttkbootstrap.constants import *

# def reverse():
#     text = entry.get()
#     textreverse = text[::-1]
#     label2.config(text=f"Результат {textreverse}")


# window = tk.Window(themename="cyborg")
# window.title("Перевертач тексту")
# window.geometry("400x250")

# label1=tk.Label(window,text="Введіть текст для перевертання")
# label1.pack(pady = 10)

# entry = tk.Entry(window)
# entry.pack(pady=5)

# button= tk.Button(window,text="Перевернути",command=reverse)
# button.pack(pady=10)

# label2 = tk.Label(window,text="Результат: ")
# label2.pack()

# window.mainloop()

# домашка

import ttkbootstrap as tk

def convert():
    try:
        km = float(entry.get())
        miles = km * 0.62137
        label.config(text=f"Це дорівнює {miles:.2f} миль")
    except ValueError:
        label.config(text="Введіть коректне число!")

window = tk.Window(themename="minty")
window.title("Конвертер км в милі")
window.geometry("400x200")

label1 = tk.Label(window, text="Введіть кілометри:", font=("Arial", 12))
label1.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(window, text="Конвертувати", command=convert)
button.pack(pady=10)

label = tk.Label(window, text="", font=("Arial", 12, "bold"))
label.pack(pady=10)

window.mainloop()
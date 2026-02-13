# 🔴 Ярік — “Анкета учня


# Створи програму “Анкета”.


# 🔹 Додай


# Поле вводу: “Введи ім’я учня”


# Кнопку "Зберегти анкету"


# 🔹 Чекбокси


# “Люблю математику”


# “Люблю програмування”


# 🔹 Радіокнопки (улюблений предмет — тільки один)


# “Математика”


# “Англійська”


# “Інформатика”


# 🔹 Після натискання кнопки


# Напис змінюється на "Анкета: <ім’я>"


# Показати які чекбокси вибрані


# Показати який предмет обраний



import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()

window.title("Анкета")

window.geometry("500x500")


def anketa():

    yroku = yroku.get()


    names = name.get()


    anketa = ( f"ім'я {names} \n Любимий урок {yroku}" )


    messagebox.showinfo("Анкета", anketa)



name_label = tk.Label(window, text="Введи ім'я")

name_label.pack()



name_entry = tk.Entry(window)

name_entry.pack()

yroku = tk.StringVar(value="Ненавиджу школу")

tk.Radiobutton(window, text="Математика", variable=yroku, value="Математика").pack()

tk.Radiobutton(window, text="Англіська", variable=yroku, value="Англіська").pack()

tk.Radiobutton(window, text="Інформатика", variable=yroku, value="Інформатика").pack()

tk.Radiobutton(window, text="Ненавиджу школу", variable=yroku, value="Ненавиджу школу").pack()

ttk.Separator(window, orient='horizontal').pack(fill='x', pady=10)

button1 = tk.Button(window, text="Зберегти анкету" , command=anketa)


button1.pack()


window.mainloop()
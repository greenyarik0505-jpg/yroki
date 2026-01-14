# Клікер з магазином апгрейдів 
# tkinter 
# має бути сила кліку і має бути авто-клікер
# Посилення кліку і автоклікер повинен мати ціну

import tkinter as tk 
from tkinter import messagebox 
window = tk.Tk() # створення вікна
window.title("Super Clicker") # назва
window.geometry("300x400") # розміри екрану
#Змінні
score = 0
clickpower = 1
autoclickpower = 0

upgradeclick = 10
upgradeauto = 50

#Функції
def updateui():
    """Оновлює весь текст на екрані"""
    labelscore.config(text=f"Рахунок {score}")
    labelstats.config(text=f"Сила кліку {clickpower} | Авто: {autoclickpower}/сек")
    btnupgradeclick.config(text=f"Посилити клік (+1)\n Ціна: {upgradeclick}")
    btnupgradeauto.config(text=f"Посилити клік (+1)\n Ціна: {upgradeauto}")
def onclick():
    """Функція для головної кнопки""" # коментарі в функціях можна робити за допомогою потрійних лапок
    global score # глобальна змінна може використовуватись і в зовнішньому коді і в середині функцій
    score+= clickpower
    updateui()
def buyclickupgrade():
    """Купівля посилення кліку"""
    global score,clickpower,upgradeclick
    if score >= upgradeclick:
        score -= upgradeclick
        clickpower +=1
        upgradeclick = int(upgradeclick*1.5)
        updateui()
    else:
        messagebox.showwarning("Помилка","Не вистачає очок")
def buyautoupgrade():
    """Купівля посилення кліку"""
    global score,autoclickpower,upgradeauto
    if score >= upgradeauto:
        score -= upgradeauto
        autoclickpower +=1
        upgradeauto = int(upgradeauto*1.5)
        updateui()
    else:
        messagebox.showwarning("Помилка","Не вистачає очок")
def autoclickloop():
    global score 
    if autoclickpower >0:
        score+=autoclickpower
        updateui()
    window.after(1000,autoclickloop) # запускаємо функцію раз в 1000 мс
# Текст рахунку 
labelscore = tk.Label(window,text=f"Рахунок: {score}") # Створення тексту рахунку
labelscore.pack(pady=15) #Розміщення рахунку (pady = 15 - відступ від верху 15 пікселів)
# Статистика 
labelstats = tk.Label(window,text="Статистика ...")
labelstats.pack()

# Головна кнопка
btnclick = tk.Button(window,text="CLICK!",command=onclick) # створення кнопки кліку
btnclick.pack(pady=20)

# Магазин 
# якщо ми не плануємо змінювати label тоді можна не давати йому змінну
tk.Label(window,text="---Магазин---").pack(pady=5) # Дозволена форма запису для label

btnupgradeclick = tk.Button(window,text="Посилити клік",command=buyclickupgrade)
btnupgradeclick.pack(fill=tk.X,padx=20,pady=2)
# fill - заповнити по tk.X - х це ширина
btnupgradeauto = tk.Button(window,text="Авто-клікер",command=buyautoupgrade)
btnupgradeauto.pack(fill=tk.X,padx=20,pady=2)

updateui()
autoclickloop()
window.mainloop()

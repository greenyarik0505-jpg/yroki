# #Tkinter повторення 
# # У нас є основні елементи entry - поле вводу , label - текст на екрані , button - кнопка яка виконувала якусь функцію 
# # Додаткові які ми рідко використовували але пора вже навчитись 
# # модуль message box який видавав повідомлення помилки або інформативні 
# # TEXT - текстове поле для різних нотаток коментарів або відображення великих текстів (тіпа блокнот)
# # Checkbutton (Прапорець або галочка) це квадратик де можна поставити галочку і ми отримуємо параметри так або ні , наприклад запам'ятати мене або додати цукор 
# # Radiobutton (перемикач) Це круглі кнопочки де можна вибрати ЛИИИИШЕЕЕЕ один варіант з групи інших варіантів
# #Scale (slider) це смуга прокрутки для вибору числового значення в діапазоні наприклад гучність звуку, яскравість екрану 


# import tkinter as tk # Підключення бібліотеки tkinter
# from tkinter import messagebox # Підключення модуля messagebox з бібліотеки tkinter
# from tkinter import ttk # Підключення модуля ttk з бібліотеки tkinter
# # ttk - це розширення для tkinter, яке надає сучасні стилізовані віджети

# window = tk.Tk() # Створення головного вікна
# window.title("Конструктор піци") # Встановлення заголовка вікна
# window.geometry("800x800") # Встановлення розмірів вікна
# # Відповідь на питання яріка чи можемо ми перемістити вікно не по центру
# #window.geometry("400x400+100+200") # Встановлення розмірів вікна та його позиції на екрані
# window.resizable(False, False) # Вимкнення можливості зміни розмірів вікна
# window.config(bg="#CAB28F") # Встановлення кольору фону вікна (hex-код кольору)
# def order():
#     name = nameentry.get() # Отримання тексту з поля вводу імені
#     size = sizevar.get() # Отримання вибраного розміру піци
#     cheese = cheesevar.get() # Отримання стану прапорця додаткового сиру (True/False)
#     spicylevel = scalespicy.get() # Отримання значення з повзунка гострого соусу
#     sause = sausecombo.get() # Отримання вибраного соусу з комбобоксу
#     notes = notestext.get("1.0", tk.END).strip() # Отримання тексту з текстового поля для нотаток
#     # Формування повідомлення з деталями замовлення
#     order_details = f"Ім'я: {name}\nРозмір піци: {size}\nДодатковий сир: {'Так' if cheese else 'Ні'}\nРівень гострого соусу: {spicylevel}\nСоус: {sause}\nДодаткові побажання: {notes}"
#     # Відображення повідомлення з деталями замовлення
#     messagebox.showinfo("Деталі замовлення", order_details)

# # ГРУПУВАННЯ ВІДЖЕТІВ
# #Створюємо контейнер для осоновних налаштувань Frame - рамка
# mainframe = tk.Frame(window,padx=20,pady=20) # Створення фрейму (контейнера) з відступами
# mainframe.pack(fill=tk.BOTH, expand=True) # Розміщення фрейму в головному вікні , expand - розтягує фрейм по всьому вікну

# # ENTRY - поле вводу тексту
# tk.Label(mainframe,text="Введіть ваше ім'я:").pack() # Створення та розміщення мітки з текстом
# nameentry = tk.Entry(mainframe,width=30) # Створення поля вводу тексту , width - ширина поля
# nameentry.pack(pady=10) # Розміщення поля вводу з відступом по вертикалі 10 пікселів

# #RADIOBUTTON - перемикач
# tk.Label(mainframe,text="Оберіть розмір піци:").pack() # Створення та розміщення мітки з текстом
# # Створюємо змінну для збереження вибраного розміру елемента
# sizevar = tk.StringVar(value="Середня") # Ініціалізація змінної з початковим значенням "Середня"
# # Створення радіокнопок для вибору розміру піци
# tk.Radiobutton(mainframe,text="Мала",variable=sizevar,value="Мала").pack() # Мала піца
# tk.Radiobutton(mainframe,text="Середня",variable=sizevar,value="Середня").pack() # Середня піца
# tk.Radiobutton(mainframe,text="Велика",variable=sizevar,value="Велика").pack() # Велика піца

# # CHECKBUTTON - прапорець
# tk.Label(mainframe,text="Оберіть додаткові інгредієнти:").pack() # Створення та розміщення мітки з текстом
# cheesevar = tk.BooleanVar() # Змінна для збереження стану прапорця (True/False) Змінна де зберігається чи вибрано чи ні 
# cbcheese = tk.Checkbutton(mainframe,text="Додатковий сир", variable=cheesevar,onvalue=True, offvalue=False) # Прапорець для додаткового сиру
# cbcheese.pack()
# # def sfisdskd(): 
# #     if cheesevar.get():
# #         print("Додатковий сир обрано")
# #     else:
# #         print("Додатковий сир не обрано")
# # SCALE - повзунок (slider)
# tk.Label(mainframe,text="Оберіть кількість  гострого соусу:").pack() # Створення та розміщення мітки з текстом
# scalespicy = tk.Scale(mainframe, from_=0, to=10, orient=tk.HORIZONTAL) # Створення повзунка для вибору кількості соусу
# # from - початкове значення , to - кінцеве значення , orient - орієнтація (горизонтальна або вертикальна) tk.HORIZONTAL - горизонтальна орієнтація tk.VERTICAL - вертикальна орієнтація
# scalespicy.pack()
# # COMBOBOX - випадаючий список (вибір соусів з кількох варіантів)
# tk.Label(mainframe,text="Оберіть соус:").pack() # Створення та розміщення мітки з текстом
# sauses = ["Томатний","Сметанний","Барбекю","Сирний","Часниковий"] # Список варіантів соусів
# sausecombo = ttk.Combobox(mainframe, values=sauses) # Створення комбобоксу з варіантами соусів
# sausecombo.current(0) # Встановлення початкового вибраного значення (перший елемент списку)
# sausecombo.pack(pady=10) # Розміщення комбобоксу

# # TEXT - текстове поле для нотаток
# tk.Label(mainframe,text="Додаткові побажання:").pack() # Створення та розміщення мітки з текстом
# notestext = tk.Text(mainframe, width=40, height=5) # Створення текстового поля для нотаток
# # width - ширина поля в символах , height - висота поля в рядках
# notestext.pack(pady=10) # Розміщення текстового поля
# # BUTTON - кнопка для оформлення замовлення
# btn_order = tk.Button(mainframe, text="Оформити замовлення",command =order) # Створення кнопки з текстом
# btn_order.pack(pady=20) # Розміщення кнопки з відступом по вертикалі 20 пікселів

# window.mainloop() # Запуск головного циклу обробки подій

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title("Конструктор бургера")
window.geometry("500x850")
window.resizable(False, False)

def order():
    name = nameentry.get()
    telefon = telefonentry.get()
    adres = adresentry.get()
    size = sizevar.get()
    drink = drinkvar.get()
    spicylevel = scalespicy.get()
    sause = sausecombo.get()
    notes = notestext.get("1.0", tk.END).strip()
    
    order_details = (
        f"Ім'я: {name}\n"
        f"Телефон: {telefon}\n"
        f"Адреса: {adres}\n"
        f"Розмір бургера: {size}\n"
        f"Напій: {drink}\n"
        f"Рівень гостроти: {spicylevel}\n"
        f"Соус: {sause}\n"
        f"Побажання: {notes}"
    )
    messagebox.showinfo("Деталі замовлення", order_details)

mainframe = tk.Frame(window, padx=20, pady=10)
mainframe.pack(fill=tk.BOTH, expand=True)

tk.Label(mainframe, text="Введіть ваше ім'я:").pack()
nameentry = tk.Entry(mainframe, width=30)
nameentry.pack(pady=5)

tk.Label(mainframe, text="Введіть ваш номер телефона:").pack()
telefonentry = tk.Entry(mainframe, width=30)
telefonentry.pack(pady=5)

tk.Label(mainframe, text="Введіть адресу:").pack()
adresentry = tk.Entry(mainframe, width=30)
adresentry.pack(pady=5)

ttk.Separator(mainframe, orient='horizontal').pack(fill='x', pady=10)

tk.Label(mainframe, text="Оберіть розмір бургера:", font=('Arial', 10, 'bold')).pack()
sizevar = tk.StringVar(value="Середня")
tk.Radiobutton(mainframe, text="Мала", variable=sizevar, value="Мала").pack()
tk.Radiobutton(mainframe, text="Середня", variable=sizevar, value="Середня").pack()
tk.Radiobutton(mainframe, text="Велика", variable=sizevar, value="Велика").pack()

ttk.Separator(mainframe, orient='horizontal').pack(fill='x', pady=10)

tk.Label(mainframe, text="Оберіть додатковий напій:", font=('Arial', 10, 'bold')).pack()
drinkvar = tk.StringVar(value="Без напою")
tk.Radiobutton(mainframe, text="Кока Кола", variable=drinkvar, value="Кока Кола").pack()
tk.Radiobutton(mainframe, text="Фанта", variable=drinkvar, value="Фанта").pack()
tk.Radiobutton(mainframe, text="Спрайт", variable=drinkvar, value="Спрайт").pack()
tk.Radiobutton(mainframe, text="Не потрібно", variable=drinkvar, value="Без напою").pack()

ttk.Separator(mainframe, orient='horizontal').pack(fill='x', pady=10)

tk.Label(mainframe, text="Рівень гострого соусу:").pack()
scalespicy = tk.Scale(mainframe, from_=0, to=10, orient=tk.HORIZONTAL)
scalespicy.pack()

tk.Label(mainframe, text="Оберіть соус:").pack(pady=(10, 0))
sauses = ["Майонез", "Гірчиця", "Кетчуп", "Сирний", "Соус-хрін"]
sausecombo = ttk.Combobox(mainframe, values=sauses, state="readonly")
sausecombo.current(0)
sausecombo.pack(pady=5)

tk.Label(mainframe, text="Додаткові побажання:").pack()
notestext = tk.Text(mainframe, width=40, height=4)
notestext.pack(pady=5)

btn_order = tk.Button(mainframe, text="Оформити замовлення", bg="#4CAF50", fg="white", font=('Arial', 11, 'bold'), command=order)
btn_order.pack(pady=20)

window.mainloop()

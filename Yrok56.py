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
#     # Доповнення з чекбоксом
#     zminna = checkbox_var.get() # отримання значення з чекбоксу
#     zminna2 = checkbox_var2.get() # отримання значення з чекбоксу
#     # тут ми можемо робити перевірку на вибране чи не вибране
#     if zminna == 0:
#         zminna = "Не вибрано"
#     else:
#         zminna = "Вибрано"
#     if zminna2 == 0:
#         zminna2 = "Не вибрано"
#     else:
#         zminna2 = "Вибрано"
#     a=tk.Label(window,text=f"Вибране значення чекбоксу: {zminna}, {zminna2}",bg="lightyellow")
#     a.pack(pady=5)
# def radiocheck():
#     radiovalue = radio_var.get() # отримання значення з радіобатонів
#     if radiovalue == 1:
#         radiovalue = "Халід кашмірі"
#     elif radiovalue == 2:
#         radiovalue = "Амір Хосров Дехлаві"
#     elif radiovalue == 3:
#         radiovalue = "Фірдоусі"
#     b=tk.Label(window,text=f"Вибране значення радіобатону: {radiovalue}",bg="lightyellow")
#     b.pack(pady=5)
# button = tk.Button(window,text="Змінити напис",command=changetext,bg="lightgreen") # кнопка
# button.pack(pady=10,padx=10) # розміщення кнопки на вікні
# button2 = tk.Button(window,text="Радіобатон перевірка",command=radiocheck,bg="lightgreen") # кнопка
# button2.pack(pady=10,padx=10) # розміщення кнопки на вікні

# # Чекбокси - Checkbutton()
# # створення чекбоксу
# checkbox_var = tk.IntVar(value=1) # створення змінної для збереження стану чекбоксу
# checkbox_var2 = tk.IntVar(value=1) # створення змінної для збереження стану чекбоксу
# # для чекбоксів значення 0 це не вибрано , а 1 це вибрано
# #Просто змінна яка може набувати якесь значення (зазвичай 1 або 0)
# checkbox1 = tk.Checkbutton(window,text="Опція 1",variable=checkbox_var) # створення чекбоксу
# # variable - яке значення змінної буде змінюватись при натисканні на чекбокс
# # value - яке значення буде присвоєно цій змінній коли чекбокс буде обраний
# checkbox1.pack(pady=10) # розміщення чекбоксу на вікні
# chebox2 = tk.Checkbutton(window,text="Опція 2",variable=checkbox_var2) # створення чекбоксу
# chebox2.pack(pady=10) # розміщення чекбоксу на вікні

# #В чекбоксах значення лише 0 або 1 , а в радіобатонах може бути будь яке число
# # Радіобатони - Radiobutton() 
# # створення радіобатонів
# radio_var = tk.IntVar(value=1) # створення змінної для збереження стану радіобатонів
# radio1 = tk.Radiobutton(window,text="Варіант 1",variable=radio_var,value=1) # створення радіобатону
# radio1.pack(pady=5) # розміщення радіобатону на вікні
# radio2 = tk.Radiobutton(window,text="Варіант 2",variable=radio_var,value=2) # створення радіобатону
# radio2.pack(pady=5) # розміщення радіобатону на вікні
# radio3 = tk.Radiobutton(window,text="Варіант 3",variable=radio_var,value=3) # створення радіобатону
# radio3.pack(pady=5) # розміщення радіобатону на вікні

# window.mainloop() # запуск головного циклу вікна






# Задача 3: Тест з історії або математики (Radiobutton)
# Умова: Напишіть міні-тест. У вікні має бути запитання (наприклад: "Скільки буде 2+2?") та три радіобатони з варіантами відповідей (наприклад: "3", "4", "5"). Додайте кнопку "Перевірити". Якщо відповідь правильна, напис під кнопкою має стати зеленим і написати "Правильно!", якщо помилкова — червоним і написати "Спробуй ще!".
# Підказка:
# Визначте, яке value відповідає правильній відповіді.
# У функції перевірки порівняйте значення змінної радіобатонів із правильним числом.

import tkinter as tk

window = tk.Tk()
window.title("Тест з історії")
window.geometry("500x350")

text = "Яку назву мав німецький план наступу через Арденни,\nщоб відрізати союзників від решти Франції?"
vopros = tk.Label(window, text=text, font=("Arial", 11, "bold"), justify="center")
vopros.pack(pady=15)

radio_var = tk.IntVar()
radio_var.set(0)

radio1 = tk.Radiobutton(window, text="План Шліффена", variable=radio_var, value=1)
radio1.pack(pady=5, anchor="w", padx=100)

radio2 = tk.Radiobutton(window, text="План «Гельб» (Fall Gelb)", variable=radio_var, value=2)
radio2.pack(pady=5, anchor="w", padx=100)

radio3 = tk.Radiobutton(window, text="План «Барбаросса»", variable=radio_var, value=3)
radio3.pack(pady=5, anchor="w", padx=100)

result = tk.Label(window, text="", font=("Arial", 10, "bold"), width=30)
result.pack(pady=20)

def check_answer():
    vubor = radio_var.get()
    
    if vubor == 2:
        result.config(text="Правильно!", fg="green")
        result.config(bg="lightgreen")
    elif vubor == 0:
        result.config(text="Спочатку обери варіант!", fg="black", bg="white")
    else:
        result.config(text="Спробуй ще!", fg="red")
        result.config(bg="#ffcccb")

check_button = tk.Button(window, text="Перевірити відповідь", command=check_answer, font=("Arial", 10))
check_button.pack(pady=10)

window.mainloop()
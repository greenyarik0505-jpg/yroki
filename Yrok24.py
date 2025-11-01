# Умовний оператор
# if умова:
#     блок коду
#     будь який код
#     будь якої величини
#     будь якої довжини
#     і поки він з відступом 
#     він належить до ось цього if

# elif умова:
#     блок коду
#     будь який код
#     будь якої величини
#     будь якої довжини
#     і поки він з відступом 
#     він належить до ось цього elif
# else: # без умови бо це будь яка інша або непердбачувана або зазвичай неправильна 
#     #коли не задовільнинилсь всі інші умови переходим до крайньої
#     помилка
#     або якась дія яку ми зробимо в будь якому випадку

# a = int(input("Напишіть будь яке число "))
# if a>0:
#     print("Додатнє число")
# elif a<0:
#     print("Від'ємне число")
# #Ця умова
# elif a==0:
#     print("Нуль")
# #І ця умова
# # else:
# #     print("Нуль")
# while True:
#     a = int(input("Напишіть будь яке число "))
#     if a>=0:
#         print("Додатнє число")
#     else:
#         print("Від'ємне")

# Функції
# print()
# input()
# import random
# random.randint()
# random.choice()

#Створення фукції 
# def назва функції (список аргументів):
#     блок коду, який буде виконуватись при виклику функції

# def sayhelloprivetandpaka():
#     print("Hello privet paka ")

# def spk():
#     print("Hello privet paka ")
# spk()

#Позиційні аргументи і функції з аргументами 

# def peremnozhnasebe(x):
#     print(x*x)
# peremnozhnasebe(100)
# peremnozhnasebe(2)
# peremnozhnasebe(4)
# peremnozhnasebe(8)
# peremnozhnasebe(10)
# peremnozhnasebe(50)

# Створити функцію яка перемножує A B C 
# def kruto(a,b,c):
#     print(a*b*c)
#     print(f"a= {a} ")
#     print(f"b= {b} ")
#     print(f"c= {c} ")

# kruto(4,10,20)


# def opus(name,city,age):
#     print(f"Мене звати {name},я живу в {city} і мені {age} років")
# opus("Sasha","Kyiv","22")
# opus("Nikopole","11","Dima")
# opus(city="Nikopole",age="11",name="Dima")
# opus("Dima",age="11",city="Nikopole") # ось так робити можна
# opus(age="11","Dima",city="Nikopole") #SyntaxError: positional argument follows keyword argument
# #Якщо використовуєте змішаний то тоді позиційні аргументи завжди мають бути на першому місці 
# def opus(name,city,age,country="Ukraine"):
#     print(f"Мене звати {name},я живу в {city} {country} і мені {age} років")
# opus("Sasha","Kyiv","22")
# opus("Kirill","Paris","12","France")


# def calculate(a,b):
#     resultat = a+b
#     return resultat
# print(calculate(10,20))
# def calculate2(a,b):
#     print(a+b+calculate(a,b))
# calculate2(10,20)

# x = 10
# def plusx():
#     global x
#     x+=5
#     print(x)
# plusx()
# print(x)

# 12. Вводяться два цілих числа. Визначити, чи діляться вони націло одне на одне.
# Якщо діляться, то вивести результат їхнього ділення
# b = int(input("Введіть число 1: " ))
# a = int(input("Введіть число 2: " ))
# f = a // b
# if a % b == 0:
#     print(f"Ділится націло {f} результат")
# else:
#     print(f"Не ділится націло {f} результат")

# Домашка 

# 5. Перевірка діапазону
# Завдання: Визначити, чи знаходиться число в діапазоні від -4 до 10 включно.

# import tkinter as tk
# from tkinter import ttk

# def check():
#     user = int(entry.get())

#     if user >= -4 and user <= 10:
#         label2.config(text="Не лимит!!!!!", foreground="green")
#         button1.config(state="disabled")
#         entry.config(state="disabled")
#     else:
#         label2.config(text="Лимит!!!!!", foreground="red")
#         entry.delete(0, "end")

# window = tk.Tk()
# window.title("Проверка числа")
# window.geometry("500x300")

# label1 = ttk.Label(window, text="Напиши число от -4 до 10", font=("Arial",12))
# label1.pack(pady=20)

# entry = ttk.Entry(window,font=("Arial",14),justify="center")
# entry.pack(pady=10)

# button1 = ttk.Button(window, text="Перевірити", command=check)
# button1.pack(pady=10)

# label2 = ttk.Label(window, text="", font=("Arial",14,"bold"))
# label2.pack(pady=10)

# window.mainloop()

# 6. Порівняння з нулем
# Завдання: Визначити, чи є число додатним або від'ємним.
# Опис: Програма порівнює введене число з нулем.
# Якщо воно менше нуля, вона повідомляє, що число від'ємне.
# В іншому випадку вона повідомляє, що воно позитивне.

# a = int(input("Введіть число: "))
# if 0 <= a:
#     print(f"{a} це число додатне")
# else:
#     print(f"{a} це число від'ємне")

# 7. Визначення високосного року
# Завдання: Перевірити, чи є рік високосним.
# Опис: Програма використовує правила григоріанського календаря: рік є високосним,
# якщо він ділиться на 4, але не на 100, або якщо він ділиться на 400.

# a = int(input("Введи число: " ))
# if a % 4 == 0 or a % 400 == 0:
#     print(f"{a} це рік є високим")
# else:
#     print(f"{a} це рік не є високим")

# 8. Визначення дня тижня
# Завдання: Вивести назву дня тижня, що відповідає числу від 1 до 7.
# Опис: Програма перевіряє, яке число ви ввели, і виводить відповідну назву дня тижня.
# Наприклад, якщо ви вводите 1, виводиться "Понеділок".
# Якщо число не в діапазоні від 1 до 7, виводиться повідомлення про помилку.

# a = int(input("Введіть число: " ))
# if a == 1:
#     print("Понеділок")
# elif a == 2:
#     print("Вівторок")
# elif a == 3:
#     print("Середа")
# elif a == 4:
#     print("Четверг")
# elif a == 5:
#     print("П'ятниця")
# elif a == 6:
#     print("Субота")
# elif a == 7:
#     print("Неділя")
# else:
#     print("Помилка")

# 2. Повідомлення: напишіть функцію display_message() для виведення повідомлення
# за темою, розглянутою в цьому розділі. Викличте функцію і переконайтеся в тому,
# що повідомлення виводиться правильно.

# def display_message(message):
#     print(message)
# display_message("Tung tung sahur")

# 3. Улюблена книга: напишіть функцію favorite_book(), яка отримує один параметр title.
# Функція має виводити повідомлення виду "One of my favorite books is Alice in
# Wonderland". Викличте функцію і переконайтеся в тому, що назву книги правильно
# передають як аргумент під час виклику функції.

# def favorite_book(books):
#     print(f"One of my favorite books is {books}")
# favorite_book("Alice in Wonderland")
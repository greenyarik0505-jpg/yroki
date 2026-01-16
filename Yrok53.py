# # Робота з файлами 
# f = open("clicks.txt","r") # Відкриття файлу з назвою clicks.txt в режимі..
# #Існуючі режими
# # r - відкриття на читання
# # коли пишемо r - використовуємо функцію read()
# # для того щоб вивести контент нашого файлу в змінну в пайтоні
# # наприклад
# # content = f.read()
# # print(content)
# # print(type(content))
# # content=int(content)
# # print(type(content))
# # content+=1
# # print(content)
# #=====================================
# #наступний режим 
# # w - відкриття на запис 
# # Увааажно
# # коли ми вмикаємо цей режим вміст файлу стирається ПОВНІСТЮ
# # а якщо такого файлу не існує то створюється цей файл
# # З цим режимом ми можемо використовувати
# # функцію write()
# # import random
# # f = open(f"clicks{random.randint(0,1000)}.txt","w")
# # f.write("Text text text AБО ЗМІННА")
# # коли при записі ми отримуємо не наш текст а �̲���
# # ми повинні відкривати файл з ще одним параметром
# # encoding = "UTF-8"
# # наприклад
# # f = open(f"clicks{random.randint(0,1000)}.txt","w",encoding="UTF-8")
# # f.write("Text text text AБО ЗМІННА")
# # ===============- режим дозапису
# режим а
# він дозапису==========================
# Останній режим є інформацію через функцію write()
# в кінці файлу 
# якщо файлу немає свариться
# читати файл не вміє
# f = open("clicks.txt","a",encoding="UTF-8")
# f.write("GuguGaga")
# # Нагадування
# #якщо хочемо кожен рядок дозаписувати в новому рядочку
# # Використовуємо \n
# f.write("\n67")

# import tkinter as tk
# window = tk.Tk()
# window.geometry("600x400")
# clicks=0
# def save():
#     global clicks
#     f = open("clicks.txt","w")
#     f.write(str(clicks))
#     f.close()
# def load():
#     global clicks
#     f=open("clicks.txt","r")
#     clicks = f.read()
#     clicks= int(clicks)
# def click():
#     global clicks
#     clicks+=1
#     label.config(text=f"Кліків:{clicks}")
#     save()

# label = tk.Label(window,text="Clicks")
# label.pack()
# button = tk.Button(window,text="Clickme",command=click)
# button.pack()
# load()





# 🟢 Задача 3. Лічильник натискань кнопок (так / ні)

# Ідея:
# Є дві кнопки: «Так» і «Ні», програма рахує натискання кожної.

# Потрібно:

# Два лічильники: yes_count, no_count

# Зберігати обидва числа в answers.txt

# При запуску — завантажувати значення

# Виводити статистику в Label

# Tkinter елементи:

# 2 кнопки

# 1 або 2 Label

# Файл:
# answers.txt
# (наприклад: 5 3)

import tkinter as tk
window = tk.Tk()
window.geometry("600x400")

yes_count = 0
no_count = 0

def save():
    global yes_count, no_count
    f = open("answers.txt", "w")
    f.write(f"{yes_count} {no_count}")
    f.close()

def load():
    global yes_count, no_count
    f = open("answers.txt", "r")
    data = f.read().split()
    f.close()
    yes_count = int(data[0])
    no_count = int(data[1])

def yes_cout():
    global yes_count
    yes_count += 1
    save()

def no_cout():
    global no_count
    no_count += 1
    save()

label = tk.Label(window, text="Считалка")
label.pack()

button1 = tk.Button(window, text="Да", command=yes_cout)
button1.pack()

button2 = tk.Button(window, text="Нет", command=no_cout)
button2.pack()

load()

window.mainloop()

# import tkinter as tk
# window = tk.Tk() # створити вікно програми
# window.title("Перша програма ") # назва програми
# window.geometry("600x500") # розмір вікна  (ширинаxвисота)
# window.resizable(True,True) # дозволити чи заборонити змінювати розмір вікна 

# def onclick():
#     label1.config(text="Кнопка була натиснута") # .config(text) дозволя редагувати і писати новий текст
# #Створюємо напис
# label1 = tk.Label(window,text="Привіт це моя супер програма ",font=("Arial",20)) #створення надпису (вікно,текст,шрифт(шрифт не обов'язково))
# label1.pack(pady=50) # pady - відступ в даному випадку 50 пікселів, можна його не писати

# #Кнопка
# button1 = tk.Button(window,text="Кляцни мене",command = onclick , bg="lightblue",font=("Arial",20)) # (вікно,текст,функція яка активовується при нажатті кнопки,задній фон bg (не обов'язково),шрифт(шрифт не обов'язково))
# button1.pack(pady=100)
# window.mainloop()

# import tkinter as tk

# count = 0

# def plus():
#     global count
#     count+=1
#     label1.config(text=f"Рахунок {count}")
# def minus():
#     global count
#     count-=1
#     label1.config(text=f"Рахунок {count}")
# def reset():
#     global count
#     count=0
#     label1.config(text=f"Рахунок {count}")

# window = tk.Tk()
# window.title("Лічильник")
# window.geometry("300x200")

# label1 = tk.Label(window,text="Рахунок: 0",font=("Arial",30))
# label1.pack(pady=20)

# buttonplus=tk.Button(window,text="+1",command=plus,bg="lightgreen",width=50,height=10,font=("Arial",20))
# buttonplus.pack(pady=5)

# buttonminus=tk.Button(window,text="-1",command=minus,bg="pink",width=50,height=10,font=("Arial",20))
# buttonminus.pack(pady=5)

# buttonreset=tk.Button(window,text="Скинути",command=reset,bg="yellow",width=50,height=10,font=("Arial",20))
# buttonreset.pack(pady=5)

# buttonexit=tk.Button(window,text="Вийти",command=window.quit,bg="red",width=50,height=10,font=("Arial",20)) #window.quit - вихід
# buttonexit.pack(pady=5)
# window.mainloop()

#Домашнє завдання: спробуйте зробити клікер який додає рандомне число при кожному клікові з бібліотекою tkinter

import tkinter as tk
import random

count = 0
error = 0

def plus():
    global  count , error
    count=random.randint(1,1000)
    error += count
    label1.config(text=f"Рахунок {error}")
window = tk.Tk()
window.title("Лічильник")
window.geometry("300x200")
label1 = tk.Label(window,text="Рахунок: 0",font=("Arial",30))
label1.pack(pady=20)
buttonplus=tk.Button(window,text="+1",command=plus,bg="lightgreen",width=50,height=10,font=("Arial",20))
buttonplus.pack(pady=5)

window.mainloop()
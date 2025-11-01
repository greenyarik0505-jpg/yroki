# import turtle
# import random 

# d = turtle.Screen()
# d.setup(width=300,height=300)
# d.bgcolor("white")
# d.title("Гра у кубики")
# d.tracer(1) # Вмикає анімацію, щоб ми бачили всі дії черепашок
# dots = [[(0,0,"red"), (-100,100,"white"),(-100,0,"white"),(-100,-100,"white"),(100,100,"white"),(100,0,"white"),(100,-100,"white") ],
#         [(0,0,"white"), (-100,100,"red"),(-100,0,"white"),(-100,-100,"white"),(100,100,"white"),(100,0,"white"),(100,-100,"red") ],
#         [(0,0,"red"), (-100,100,"red"),(-100,0,"white"),(-100,-100,"white"),(100,100,"white"),(100,0,"white"),(100,-100,"red") ],
#         [(0,0,"white"), (-100,100,"red"),(-100,0,"white"),(-100,-100,"red"),(100,100,"red"),(100,0,"white"),(100,-100,"red") ],
#         [(0,0,"red"), (-100,100,"red"),(-100,0,"white"),(-100,-100,"red"),(100,100,"red"),(100,0,"white"),(100,-100,"red") ],
#         [(0,0,"white"), (-100,100,"red"),(-100,0,"red"),(-100,-100,"red"),(100,100,"red"),(100,0,"red"),(100,-100,"red") ]]
# dot = [turtle.Turtle() for _ in range(7)]

# def click():
#     num = random.randint(1,6)
#     print(f"Випало число {num}\n") 
#     for i in range(7):
#         dot[i].shape("circle")
#         dot[i].color(dots[num-1][i][2])
#         dot[i].penup()
#         dot[i].goto(dots[num-1][i][0],dots[num-1][i][1])
#         dot[i].dot()
# d.listen()
# d.onkeypress(click,"space")
# d.mainloop()

# import tkinter as tk
# import random
# f = 0
# def b(event):
#     d.delete("all")
#     f = random.randint(1, 6)
#     g = c[f]
#     for (x, y) in g:
#         d.create_oval(x-15, y-15, x+15, y+15, fill="black")
#     user = int(entry.get())
#     if user == f:
#         label2.config(text="Правильно!!!!!",foreground="green")
#     else:
#         label2.config(text="Неправильно!!!!!",foreground="red")
#         entry.delete(0,"end")

# a = tk.Tk()
# a.title("Кубик")
# a.geometry("250x300")

# c = [
#     [],
#     [(100, 100)],
#     [(50, 50), (150, 150)],
#     [(50, 50), (100, 100), (150, 150)],
#     [(50, 50), (50, 150), (150, 50), (150, 150)],
#     [(50, 50), (50, 150), (100, 100), (150, 50), (150, 150)],
#     [(50, 50), (50, 150), (150, 50), (150, 150), (50, 100), (150, 100)]
# ]

# d = tk.Canvas(a, width=200, height=200, bg="white")
# e = tk.Label(a, text="Натисни 'Пробіл', щоб кинути кубик")

# a.bind("<space>", b)

# d.pack(pady=10)
# e.pack(pady=5)

# a.geometry("500x300")
# label1= tk.Label(a,text="Угадай число",font=("Arial",12)).pack(pady=20)
# entry = tk.Entry(a,font=("Arial",14),justify="center") #розмістити по горизонталі в центрі
# entry.pack(pady=10)
# label2 = tk.Label(a,text="",font=("Arial",14,"bold")) # bold - жирний шрифт
# label2.pack(pady=10)

# a.mainloop()

# Домашка

import tkinter as tk
import random
from tkinter import ttk

word = ["Ліво","Право","Верх","Низ"]
secret = 0
label3 = None

def check():
    global secret, label3
    secret = random.choice(word)
    user = entry.get()
    label3 = ttk.Label(window, text=secret, font=("Arial",14,"bold"))
    label3.pack(pady=10)

    if user == secret:
        label2.config(text="Правильно!!!!!", foreground="green")
        button1.config(state="disabled")
        entry.config(state="disabled")
    else:
        label2.config(text="Неправильно!!!!!", foreground="red")
        entry.delete(0, "end")

def ozucka():
    global label3
    for w in window.winfo_children():
        try:
            t = w.cget("text")
        except Exception:
            continue
        if t in word:
            w.destroy()
    label3 = None

def restart():
    global label3
    for w in window.winfo_children():
        try:
            t = w.cget("text")
        except Exception:
            continue
        if t in word:
            w.destroy()
    label3 = None
    label2.config(text="", foreground="black")
    entry.config(state="normal")
    entry.delete(0,"end")
    button1.config(state="normal")

window = tk.Tk()
window.title("Вгадай направление")
window.geometry("500x300")

label1 = ttk.Label(window, text="Я загадав Право или Ліво или Верх или Низ, спробуй його відгадати", font=("Arial",12))
label1.pack(pady=20)

entry = ttk.Entry(window,font=("Arial",14),justify="center")
entry.pack(pady=10)

button1 = ttk.Button(window, text="Перевірити", command=check)
button1.pack(pady=10)

button2 = ttk.Button(window, text="Очистка відповидей", command=ozucka)
button2.pack(pady=10)

button3 = ttk.Button(window, text="Рестарт", command=restart)
button3.pack(pady=10)

label2 = ttk.Label(window, text="", font=("Arial",14,"bold"))
label2.pack(pady=10)

window.mainloop()


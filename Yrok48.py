import tkinter as tk
from tkinter import messagebox
def avtorizacia():
    with open("users.txt","r",encoding="utf-8") as file:
        for line in file:
            # print(line)
            login = line.strip().split(",")[0]
            parol = line.strip().split(",")[1]
            print(f"Користувач: {login}")
            print(f"Пароль: {parol}")
            if login == entrylogin.get() and parol == entryparol.get():
                messagebox.showinfo("Вхід","Вхід успішний")
            else:
                messagebox.showwarning("Невірние дание входа","Ви ввели неправильний пароль або логин")
window = tk.Tk()
window.title("Authorisation Form")
labelparol=tk.Label(window, text="Введіть ваш пароль:")
labellogin = tk.Label(window, text="Введіть ваш логін:")
entrylogin = tk.Entry(window, width=30)

entryparol= tk.Entry(window, width=30)

Button= tk.Button(window,text="увійти",command=avtorizacia) 

labellogin.pack()
entrylogin.pack(pady=10)
labelparol.pack()
entryparol.pack(pady=10)
Button.pack(pady=10)

window.mainloop()

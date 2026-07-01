import tkinter as tk
import secrets
import string

window = tk.Tk()
window.title("Academy Clicker")
window.geometry("500x300")

def generate_password(length=12):
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def obnova():
    new_password = generate_password(16)
    parol_label.config(text=new_password)

def copy_password():
    password = parol_label.cget("text")
    if password and password != "Пароль еще не сгенерирований":
        window.clipboard_clear()
        window.clipboard_append(password)

parol_label = tk.Label(window, text="Пароль еще не сгенерирований", font=("Arial", 18, "bold"))
parol_label.pack(pady=12)

parol = tk.Button(window, text="Сгенерировать пароль", font=("Arial", 14), command=obnova)
parol.pack(pady=16)

copy_btn = tk.Button(window, text="Скопировать пароль", font=("Arial", 14), command=copy_password)
copy_btn.pack(pady=10)

window.mainloop()

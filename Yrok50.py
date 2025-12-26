#----------------------------KILZONE----------------------------------------
#------------------------SHADOW---FALL--------------------------------------
import tkinter as tk
import random
from tkinter import messagebox

window = tk.Tk()
window.title("KILZONE SHADOW FALL")
window.geometry("500x500")
window.resizable(False, False)

HP_ME = 100
HP_BOSS = 200

def ydaruti():
    global HP_ME
    global HP_BOSS
    orezue = vubor_oryzue.get()
    
    if orezue == 1:
        Ydar_ugroka = random.randint(1,10)
        Ydar_bossa = random.randint(35,45)
        HP_BOSS -= Ydar_ugroka
        HP_ME -= Ydar_bossa
    elif orezue == 2:
        Ydar_ugroka = random.randint(30,45)
        Ydar_bossa = random.randint(20,40)
        HP_BOSS -= Ydar_ugroka
        HP_ME -= Ydar_bossa
    elif orezue == 3:
        Ydar_ugroka = random.randint(35,45)
        Ydar_bossa = random.randint(1,15)
        HP_BOSS -= Ydar_ugroka
        HP_ME -= Ydar_bossa
    elif orezue == 4:
        Ydar_ugroka = random.randint(20,30)
        HP_BOSS -= Ydar_ugroka

    label1.config(text=f"Ваше hp {HP_ME}")
    label2.config(text=f"Босса hp {HP_BOSS}")

    if HP_ME <= 20:
        label1.config(fg="red")
    else:
        label1.config(fg="green")

    if HP_BOSS <= 20:
        label2.config(fg="red")
    else:
        label2.config(fg="green")
        
    if HP_ME <= 0:
        messagebox.showwarning("Меню пройграша","Ви проиграли")
        window.destroy()
    elif HP_BOSS <= 0:
        messagebox.showwarning("Меню виграша","Ви виграли")
        window.destroy()

label1 = tk.Label(window, text=f"Ваше hp {HP_ME}", font=("Arial", 15), fg="green")
label1.pack(pady=10)

label2 = tk.Label(window, text=f"Босса hp {HP_BOSS}", font=("Arial", 15), fg="green")
label2.pack(pady=10)

mainframe = tk.Frame(window, padx=20, pady=20)
mainframe.pack(fill=tk.BOTH, expand=True)

tk.Label(mainframe, text="Оберіть дію атаки:").pack()
vubor_oryzue = tk.IntVar(value=1)

r1 = tk.Radiobutton(window, text="Вдарити рукою", variable=vubor_oryzue, value=1)
r2 = tk.Radiobutton(window, text="Стрелять оружием", variable=vubor_oryzue, value=2)
r3 = tk.Radiobutton(window, text="Кинути гранату", variable=vubor_oryzue, value=3)
r4 = tk.Radiobutton(window, text="Визвать дрона", variable=vubor_oryzue, value=4)

r1.pack()
r2.pack()
r3.pack()
r4.pack()

Ydar = tk.Button(mainframe, text="Вдарити", bg="#FF0000", fg="white", font=('Arial', 11, 'bold'), command=ydaruti)
Ydar.pack(pady=20)

window.mainloop()

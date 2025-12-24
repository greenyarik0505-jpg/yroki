#----------------------------KILZONE----------------------------------------
#------------------------SHADOW---FALL--------------------------------------
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


window = tk.Tk()
window.title("KILZONE" \
"         SHADOW   FALL")
window.geometry("500x500")
window.resizable(False, False)

HP_ME = 100
HP_BOSS = 200

def ydaruti():
    global HP_ME
    global HP_BOSS
    orezue = vubor_oryzue.get()
    if orezue == 1:
                HP_BOSS -= 10
                HP_ME -= 45
                label1.config(text=f"Ваше hp {HP_ME}")
                label2.config(text=f"Босса hp {HP_BOSS}")
                if 0 > HP_ME:
                    messagebox.showwarning("Меню пройграша","Ви проиграли")
                    window.destroy()
                if 0 > HP_BOSS:
                    messagebox.showwarning("Меню виграша","Ви виграли")
                    window.destroy()
    elif orezue == 2:
                HP_BOSS -= 50
                HP_ME -= 20
                label1.config(text=f"Ваше hp {HP_ME}")
                label2.config(text=f"Босса hp {HP_BOSS}")
                if 0 > HP_ME:
                    messagebox.showwarning("Меню пройграша","Ви проиграли")
                    window.destroy()
                if 0 > HP_BOSS:
                    messagebox.showwarning("Меню виграша","Ви виграли")
                    window.destroy()
    elif orezue == 3:
                HP_BOSS -= 45
                HP_ME -= 10
                label1.config(text=f"Ваше hp {HP_ME}")
                label2.config(text=f"Босса hp {HP_BOSS}")
                if 0 > HP_ME:
                    messagebox.showwarning("Меню пройграша","Ви проиграли")
                    window.destroy()
                if 0 > HP_BOSS:
                    messagebox.showwarning("Меню виграша","Ви виграли")
                    window.destroy()
    elif orezue == 4:
                HP_BOSS -= 30
                label1.config(text=f"Ваше hp {HP_ME}")
                label2.config(text=f"Босса hp {HP_BOSS}")
                if 0 > HP_ME:
                    messagebox.showwarning("Меню пройграша","Ви проиграли")
                    window.destroy()
                if 0 > HP_BOSS:
                    messagebox.showwarning("Меню виграша","Ви виграли")
                    window.destroy()

label1 = tk.Label(window,text="Ваше hp",font=("Arial",15))
label1.pack(pady=20)
label1.config(text=f"Ваше hp {HP_ME}")
label2 = tk.Label(window,text="Босса hp",font=("Arial",15))
label2.pack(pady=20)
label2.config(text=f"Босса hp {HP_BOSS}")

mainframe = tk.Frame(window,padx=20,pady=20)
mainframe.pack(fill=tk.BOTH, expand=True)

tk.Label(mainframe,text="Оберіть дію атаки:").pack()
vubor_oryzue = tk.IntVar(value=1)
r1 = tk.Radiobutton(window,text="Вдарити рукою",variable=vubor_oryzue,value=1)
r2 =tk.Radiobutton(window,text="Стрелять оружием",variable=vubor_oryzue,value=2)
r3 = tk.Radiobutton(window,text="Кинути гранату",variable=vubor_oryzue,value=3)
r4 = tk.Radiobutton(window,text="Визвать дрона",variable=vubor_oryzue,value=4)
r1.pack()
r2.pack()
r3.pack()
r4.pack()
Ydar = tk.Button(mainframe, text="Вдарити", bg="#FF0000", fg="white", font=('Arial', 11, 'bold'), command = ydaruti)
Ydar.pack(pady=20)

window.mainloop()

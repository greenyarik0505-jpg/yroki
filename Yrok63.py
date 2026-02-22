import tkinter as tk
import random
window = tk.Tk()
window.title("Cookie clicer")
window.geometry("400x300")

img = tk.PhotoImage(file="cookie.png")

score = 0

cula = 1
ctoumosti_culu = 10
avto_cluk = 0
ctoumosti_avto_cluk = 100
sans_mnozuni = 0
ctoumosti_sans_mnozuni = 1000

label_score = tk.Label(window, text="Очки: 0")
label_score.pack(pady=20)

label_status = tk.Label(window, text=f"Сила кліку {cula} | Авто: {avto_cluk}/сек | Сила множителя 10%")
label_status.pack(pady=20)

def updateui():
    label_score.config(text=f"Рахунок {score}")
    label_status.config(text=f"Сила кліку {cula} | Авто: {avto_cluk}/сек | Шанс на множителя 10%")
    btn_cula.config(text=f"Посилити клік (+1)\n Ціна: {ctoumosti_culu}")
    btn_avto_cluk.config(text=f"Посилити авто клік (+1)\n Ціна: {ctoumosti_avto_cluk}")

def click():
    global score , cula
    a = random.randint(0,10)
    if a == 5:
        score += cula
        score += cula
    else:
        score += cula
    updateui()

def upgade_cula():
    global cula , score , ctoumosti_culu

    if score >= ctoumosti_culu:
        score -= ctoumosti_culu
        cula *= 2
        ctoumosti_culu *= 4
        updateui()

    else:
        pass


def upgade_avto_cluk():
    global avto_cluk , score , ctoumosti_avto_cluk
    if score >= ctoumosti_avto_cluk:
        if 0 != avto_cluk:
            score -= ctoumosti_avto_cluk
            avto_cluk *= 2
            ctoumosti_avto_cluk *= 4
            updateui()
        else:
            score -= ctoumosti_avto_cluk
            avto_cluk += 1
            ctoumosti_avto_cluk *= 4
            updateui()
    else:
        pass

def avto_cluc():
    global avto_cluk , score
    if avto_cluk > 0:
        score+= avto_cluk
        updateui()
    window.after(1000,avto_cluc)

btn = tk.Button(window,image=img,command=click)
btn.image = img 
btn.pack()

btn_cula = tk.Button(window,command=upgade_cula,text=f"Посилити клік (+1)\n Ціна: {ctoumosti_culu}")
btn_cula.pack(pady=10)
btn_avto_cluk = tk.Button(window,command=upgade_avto_cluk,text=f"Посилити авто клік (+1)\n Ціна: {ctoumosti_avto_cluk}")
btn_avto_cluk.pack(pady=10)
updateui()
avto_cluc()
window.mainloop()

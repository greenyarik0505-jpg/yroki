# import tkinter as tk 
# window = tk.Tk()
# window.geometry("600x400")
# window.title("Картінки в ткінтері")
# def click():
#     print("Ви натиснули на кнопку")
# img = tk.PhotoImage(file="banana.gif")
# label = tk.Label(window,image=img)
# label.pack()

# btn = tk.Button(window,image=img,command=click)
# btn.image = img 
# btn.pack()
# # ТЕКСТ ТА КАРТИНКА РАЗОМ 
# btn = tk.Button(
#     window,
#     text="Натисни мене",
#     image=img,
#     compound="top" # top,bottom,left,right,center 
# )
# btn.pack()
# window.mainloop()






# import tkinter as tk 
# window = tk.Tk()
# window.geometry("600x400")
# window.title("Картінки в ткінтері")
# img1 = tk.PhotoImage(file="banana.gif")
# img2 = tk.PhotoImage(file="cat.png")
# label = tk.Label(window,image=img1)
# label.pack()
# def change():
#     label.config(image=img2)
#     label.image=img2
# # ТЕКСТ ТА КАРТИНКА РАЗОМ 
# btn = tk.Button(window,text="Змінити",command=change)
# btn.pack()
# window.mainloop()

# # Картинка як фон 
# import tkinter as tk
# window = tk.Tk()
# window.title("Ткінтер фон")
# window.geometry("400x300")
# window.resizable(False,False)#не дозволяє змінювати розмір вікна

# bg = tk.PhotoImage(file="banana.gif")
# canvas = tk.Canvas(window,width=400,height=300)
# canvas.pack(fill="both",expand=True)
# canvas.create_image(0,0,image=bg,anchor="nw")
# canvas.image=bg


# canvas.create_text(
#     200,50,
#     text="Привіт ткінтер",
#     font=("Arial",18,"bold"),
#     fill="black"
# )
# def click():
#     canvas.create_text(
#     200,200,
#     text="Кнопка натиснута!",
#     font=("Arial",14,"bold"),
#     fill="red"
# )

# btn = tk.Button(window,text="Натисни мене",command=click)
# canvas.create_window(200,130,window=btn)
# window.mainloop()


# АНІМАЦІЯ ГІФКИ 

# import tkinter as tk 
# window = tk.Tk()
# window.title("GIF animate")
# window.geometry("400x300")
# window.resizable(False,False)

# canvas = tk.Canvas(window,width=400,height=300,highlightthickness=0)
# canvas.pack(fill="both",expand=True)

# gif_frames = []
# frame_index = 0
# while True:
#     try:
#         frame = tk.PhotoImage(
#             file="banana.gif",
#             format=f"gif -index {len(gif_frames)}"
#         )
#         gif_frames.append(frame)
#     except:
#         break
# def animate():
#     global frame_index
#     canvas.delete("gif")
#     canvas.create_image(0,0,image=gif_frames[frame_index],anchor="nw",tags="gif")
#     frame_index = (frame_index + 1 ) % len(gif_frames)
#     window.after(80,animate)
# animate()
# window.mainloop()


# 🎒 Ярік — Задача «Рюкзак школяра»

# Користувач вводить число — скільки предметів у рюкзаку.

# Після натискання кнопки:

# • 0 → Рюкзак порожній + порожній рюкзак
# • 1–5 → Рюкзак нормальний + нормальний рюкзак
# • більше 5 → Рюкзак занадто важкий! + важкий рюкзак

# Підказка:
# Перетвори текст у число через int()

import tkinter as tk 
window = tk.Tk()
window.geometry("600x400")
window.title("Рюкзак школяра")
img1 = tk.PhotoImage(file="Gemini_Generated_Image_s01bj6s01bj6s01b.png")
img2 = tk.PhotoImage(file="Gemini_Generated_Image_cims7pcims7pcims.png")
img3 = tk.PhotoImage(file="Gemini_Generated_Image_yv4pi1yv4pi1yv4p.png")
label = tk.Label(window,text="Привет")
label.pack()

entry = tk.Entry(window)
entry.pack(pady=10)

def change():
    zufra = int(entry.get())
    if zufra == 0:
        label.config(image=img1)
        label.image=img1
    elif 1 <= zufra <= 5:
        label.config(image=img2)
        label.image=img2
    elif zufra > 5 :
        label.config(image=img3)
        label.image=img3

check_button = tk.Button(window, text="Перевірити", command=change, font=("Arial", 10))
check_button.pack(pady=10)

window.mainloop()

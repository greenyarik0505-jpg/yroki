import tkinter as tk

window = tk.Tk()
window.title("Кликер ")
window.geometry("400x300")

score = 0

label_score = tk.Label(window, text="Очки: 0")
label_score.pack(pady=20)

button = tk.Button(window, text="Нажми меня")
button.pack(pady=10)

def click():
    global score
    score += 1
    label_score.config(text=f"Очки: {score}")

button.config(command=click)

window.mainloop()

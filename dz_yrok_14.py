import tkinter as tk

window = tk.Tk()
window.title("Моя програма")
window.geometry("300x200")

def pokasat_tekst():
    tekst = pole_vvod.get()
    a.config(text=f"Ви ввели: {tekst}")

nadpis = tk.Label(window, text="Введіть щось цікаве:")
nadpis.pack(pady=5)

pole_vvod = tk.Entry(window)
pole_vvod.pack(pady=5)

knopka = tk.Button(window, text="Натисни мене", command=pokasat_tekst)
knopka.pack(pady=5)

a = tk.Label(window, text="")
a.pack(pady=10)

window.mainloop()

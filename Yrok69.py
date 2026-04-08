# Завдання 1: "Генератор Обзивалок" (Легко) 

# Створи вікно з Entry (куди гравець пише ім'я)'
# ' і кнопку "Згенерувати". При натисканні:'
# ' витягни ім'я з Entry, обери випадкову фразу через random.choice()
#  і виведи результат у Label!

import tkinter as tk,random

window = tk.Tk()
window.title("Entry Demo")
window.geometry("400x250")

# Заголовок
tk.Label(window, text="Як тебе звати?", font=("Arial", 14)).pack(pady=10)

# Поле введення
name_input = tk.Entry(
    window,
    font=("Arial", 14),      # Шрифт тексту
    width=25,                  # Ширина (у символах)
    fg="#2c3e50",              # Колір тексту
    bg="#ecf0f1",              # Колір фону поля
    insertbackground="black",  # Колір курсора
    relief="solid",            # Стиль рамки
    bd=2,                      # Товщина рамки
)
name_input.pack(pady=10)

# Функція для отримання тексту
def greet():
    name = name_input.get()  # .get() — витягує текст з Entry
    clovo = [f"Ку {name}",f"Привет {name}",f"Здарово {name}"]
    clovo_1 = random.choice(clovo)
    result_label.config(text=f"{clovo}", fg="#2ecc71")
    name_input.delete(0, tk.END)  # Очистити поле (від 0 до кінця)

tk.Button(window, text="Привітати", font=("Arial", 12),
          command=greet).pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

window.mainloop()

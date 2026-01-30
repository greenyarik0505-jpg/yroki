# Легенда: Компанія "OpenAI" пішла на перерву, і тебе попросили терміново написати замінник — "Aura". Він не дуже розумний, але має виглядати стильно, як справжній чат, і вміти підтримувати розмову (хоча б удавати).
# Технічне завдання: Створити вікно чат-бота в стилі "Dark Mode" (Темна тема), використовуючи такі елементи:
# Label (Заголовок): Напис зверху "Aura v0.1" (великий шрифт, білий колір).
# Text (Чат-історія): Велике поле, де з'являється листування.
# Важливо: Користувач не повинен могти стирати текст у цьому полі вручну (воно лише для читання).
# Entry (Поле вводу): Де ми пишемо повідомлення.
# Button (Кнопка "Надіслати"): Має бути стильною (наприклад, зеленого кольору).
# Логіка бота (Пародія): Бот має відповідати на повідомлення миттєво.
# Якщо написати "Привіт" -> Бот: "Привіт, шкіряний мішку!"
# Якщо написати "Як справи?" -> Бот: "Грію процесор, все супер."
# Якщо запитати щось інше -> Бот: "Я занадто лінивий, щоб думати про це."

import tkinter as tk 
window = tk.Tk()   
window.title("Aura") 
window.geometry("400x300") 
window.config(bg="black")

tk.Label(window,text="Aura v0.1",bg="orange").pack()


def otvet():
    text = entry.get
    user = entry.get
    d =+ 1000
    if user != "":
        d = tk.Label(d)(window,text=(user),bg="white").pack()
    a =+ 1
    if text != "":
        if text == "Привіт":
            a = tk.Label(a)(window,text="Привіт, шкіряний мішку!",bg="white").pack()
        elif text == "Як справи?":
            a = tk.Label(a)(window,text="Грію процесор, все супер.",bg="white").pack()
        else:
            a = tk.Label(a)(window,text="Я занадто лінивий, щоб думати про це.",bg="white").pack()

entry = tk.Entry(window)
entry.pack(pady=5)

otpravka_button = tk.Button(window, text="Отправити",command=otvet)
otpravka_button.pack(pady=20) 

window.mainloop()

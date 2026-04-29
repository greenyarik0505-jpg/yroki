from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        # 1. Створюємо об'єкт Кнопки
        btn = Button(
            text="Натисни мене!",         # Текст на кнопці
            font_size=40,                 # Розмір шрифту
            background_color=(0, 1, 0, 1),# Зелений колір КНОПКИ
            color=(0, 0, 0, 1),           # Чорний колір ТЕКСТУ
        )
        
        # 2. BIND - "Прив'язка" події. 
        # Ми кажемо кнопці: якщо стається подія 'on_press' (натиснення пальцем)
        # -> викликай ту функцію, яку я передаю (self.button_clicked).
        btn.bind(on_press=self.button_clicked)
        
        return btn # Повертаємо кнопку на екран

    # 3. Створюємо саму функцію-реакцію
    # Зверни увагу: Kivy АВТОМАТИЧНО передає аргумент `instance` (або `obj`, `button` - назвати можна як завгодно).
    # `instance` - це ПОСИЛАННЯ на саму кнопку, яку щойно натиснули!
    def button_clicked(self, instance):
        print("Бачу натиснення!")
        instance.text = "Мене натиснули! АУЧ!"        # Змінюємо текст
        instance.background_color = (1, 0, 0, 1)      # Робимо кнопку червоною!

if __name__ == '__main__':
    ButtonApp().run()

# yt-dlp - бібліотека для завантаження відео та аудіо з різних платформ, таких як YouTube. Вона підтримує широкий спектр форматів та якостей завантаження, а також дозволяє налаштовувати параметри збереження файлів.
# pip install yt-dlp - завантаження бібліотеки

# import yt_dlp 
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# options = {}
# print("Завантажуємо ")
# with yt_dlp.YoutubeDL(options) as ydl:
#     ydl.download([url])
# print("Завантажено ")



# import yt_dlp 
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# # Формати якості завантаження
# # best - найкраща якість відео та аудіо
# # bestvideo + bestaudio - качаємо все окремо і потім з'єднуємо
# # worst - найгірша якість відео та аудіо
# # bestaudio - найкраща якість аудіо
# # bestvideo[height<=720] - найкраще відео з роздільною здатністю до 720p
# writesubtitles - завантаження субтитрів, якщо вони доступні
# wrtiteautomaticsub - завантаження автоматичних субтитрів, якщо вони доступні

# # Зберегти в шлях 
# #"outtmpl": "C:/Users/Username/Downloads/%(title)s.%(ext)s"  # Зберегти в певну папку
# #'progress_hooks': [lambda d: print(f"Прогрес: {d.get('_percent_str', 'N/A')}")]  # Відстеження прогресу завантаження

# options = {
#     "format": "best", # якість завантаження
#     "outtmpl": "%(title)s.%(ext)s",  # Оригінальну назву в стандарнтому форматі
#     "progress_hooks": [lambda d: print(f"Прогрес: {d.get('_percent_str', 'N/A')}")]  # Відстеження прогресу завантаження
# }
# print("Завантажуємо ")
# with yt_dlp.YoutubeDL(options) as ydl:
#     ydl.download([url])
# print("Завантажено ")

# import yt_dlp
# import os

# def download_video(url, output_path="downloads", quality="best"):
#     """
#     Універсальна функція для завантаження відео.
    
#     Args:
#         url: Посилання на відео
#         output_path: Папка для збереження
#         quality: Якість відео (best, 720, 480, audio)
#     """
    
#     # Створюємо папку якщо не існує
#     os.makedirs(output_path, exist_ok=True)
    
#     # Вибір формату залежно від якості
#     format_options = {
#         'best': 'bestvideo+bestaudio/best',
#         '1080': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
#         '720': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
#         '480': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
#         'audio': 'bestaudio/best',
#     }
    
#     ydl_opts = {
#         'format': format_options.get(quality, 'best'),
#         'outtmpl': f'{output_path}/%(title)s.%(ext)s',
#         'ignoreerrors': True,  # Продовжувати при помилках
#         'no_warnings': False,
#         'quiet': False,
#     }
    
#     # Якщо тільки аудіо - додаємо конвертацію в MP3
#     if quality == 'audio':
#         ydl_opts['postprocessors'] = [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }]
    
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             print(f"🔄 Завантажую: {url}")
#             ydl.download([url])
#             print("✅ Успішно завантажено!")
#             return True
#     except yt_dlp.DownloadError as e:
#         print(f"❌ Помилка завантаження: {e}")
#         return False
#     except Exception as e:
#         print(f"❌ Невідома помилка: {e}")
#         return False

# # Приклад використання
# if __name__ == "__main__":
#     video_url = input("Введіть посилання на відео: ")
#     quality = input("Виберіть якість (best/1080/720/480/audio): ") or "best"
    
#     download_video(video_url, quality=quality)





# Бібліотека Pillow
# pip install pillow

from PIL import Image, ImageFilter,ImageEnhance


img=Image.open("image.jpg") # вказуємо яку картинку відкрити
print("Розмір",img.size) # розмір картинки
print("Формат",img.format) # формат картинки
# img.show() # показати картинку
# # збереження картинки різними способами
# img.save("copy.jpg") # зберегти копію картинки
# img.save("converted.png") # зберегти в іншому форматі
# img.save("comppressed.jpg",quality=50) # зберегти стиснену версію картинки (якість від 1 до 100
# де 100 - найкраща якість)

# Зміна розміру картинки 
# resized = img.resize((800,600)) # новий розмір (ширина, висота)
# resized.show() # показати змінену картинку
# Для збереження пропороцій можна використовувати метод thumbnail ЛИШЕ ДЛЯ ЗМЕНШЕННЯ 
# img.thumbnail((800,600))
# img.show()

# РОЗУМНИЙ RESIZE З АНТИАЛІАСИНГОМ Anti-aliasing 
# highquality = img.resize((800,600),Image.Resampling.LANCZOS) # Найкраща якість при зменшення 
# highquality.show()

# Поворот картинки
# rotated = img.rotate(270) # поворот на 90 градусів проти годинникової стрілки
# rotated.show()

# Відзеркалення картинки
# flip = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT) # горизонтальне відзеркалення
# flip2 = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM) # вертикальне відзеркалення
# flip.show()
# flip2.show()

# вбудовані фільтри

# blur = img.filter(ImageFilter.BLUR) # розмиття
# blur.show()

# Гаусове розмиття

# gaussian = img.filter(ImageFilter.GaussianBlur(radius=5)) # радіус розмиття
# gaussian.show()

# Прямокутне розмиття
# boxblur = img.filter(ImageFilter.BoxBlur(radius=5))
# boxblur.show()


# Різкість
# sharpen = img.filter(ImageFilter.SHARPEN)
# sharpen.show()

# Виявлення контурів 
# contour = img.filter(ImageFilter.CONTOUR)
# contour.show()

# Виявлення країв 
# edge = img.filter(ImageFilter.FIND_EDGES)
# edge.show()

# Деталізація
# detail = img.filter(ImageFilter.DETAIL)
# detail.show()

#Яскравість
#factor >1 - яскравіше <1 - темніше
# enchanc = ImageEnhance.Brightness(img)
# bright = enchanc.enhance(1.5) # 50% яскравіше
# dark = enchanc.enhance(0.5) # 50% темніше
# bright.show()
# dark.show()


# Режими кольорів 

# Чорнобіле
# bw = img.convert("L") # L - освітленість
# bw.show()
# rgb = img.convert("RGB") # RGB - кольоровий режим
# rgb.show()
# rgba = img.convert("RGBA") # RGBA - кольоровий режим з альфа каналом (прозорість)
# rgba.show()

# CMYK - для друку
# cmyk = img.convert("CMYK")
# cmyk.show()
# invert = img.convert("RGB")
# invert = Image.eval(invert, lambda x: 255 - x) # інверсія
# invert.show()


# Графіки це в нас бібліотека matplotlib
# pip install matplotlib

# import matplotlib.pyplot as plt

# plt.plot([1,2,3,4,5],[10,20,15,25,30],color="blue",marker="o") # лінійний графік
# plt.title("Приклад лінійного графіка") # заголовок
# plt.xlabel("X вісь") # підпис осі X
# plt.ylabel("Y вісь") # підпис осі Y
# plt.show() # показати графік


# qrcode - бібліотека для генерації QR-кодів
# pip install qrcode
# import qrcode
# url = input("Введіть посилання для генерації QR-коду: ")
# img = qrcode.make(url,box_size=10,border=5) # box_size - розмір одного квадратика, border - товщина рамки
# img.show() # показати QR-код

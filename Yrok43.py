#Встановити бібліотеки 
# # pip install requests beautifulsoup4 lxml
# import requests
# from bs4 import BeautifulSoup
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# url = "https://uakino.best/" # ссилка на сайт
# req = requests.get(url=url,headers=headers) # отримуємо код сторінки
# # print(req.text) # виводимо код сторінки
# # <> - теги в html
# # <div> - блок якийсь контейнер в якому знаходяться інші елементи 
# # class="movie-title" - клас елементу по якому його можна знайти 
# # тег <a> - містить в собі атрибут href в якому завжди посилання на іншу сторінку
# # тег <img> - містить в собі атрибут src в якому завжди посилання на зображення
# # <p> - параграф тексту , абзац 
# # <h1,h2,h3> заголовки 
# soup = BeautifulSoup(req.text,"lxml") # підключаємо наш об'єкт до коду і даємо доступ до нашого коду сторінки
# # p_info = soup.find("p")
# # print(p_info) # шукаємо перший тег <p> на сторінці
# # print(p_info.text) # виводимо текст з тегу <p>
# # allp_info = soup.find_all("p")
# # print(allp_info) # шукаємо перший тег <p> на сторінці

# # for p in allp_info:
# #     print(p.text) # виводимо текст з тегу <p>
# a_info = soup.find("a",class_="movie-title") # шукаємо перший тег <a> з класом movie-title
# print(a_info) # виводимо тег <a>
# # a_info = soup.find_all("a",class_="movie-title") # шукаємо перший тег <a> з класом movie-title
# # print(a_info) # виводимо тег <a>
# # for a in a_info:
# #     print(a.text) # виводимо текст з тегу <a>
# #     # print("https://uakino.best"+a.get("href")) # виводимо посилання з атрибуту href
# link = a_info.get("href") # get виводить значення атрибуту href 
# print(link)
# img_tag = soup.find("img") # шукаємо перший тег <img>
# img_url = img_tag.get("src") # отримуємо посилання на картинку з атрибуту src
# print(img_url) 
# if not "http" in img_url:
#     img_url="https://uakino.best"+img_url # додати url до картинки щоб ми могли її побачити та відвідати 
# print(img_url)
# img_response = requests.get(img_url,stream=True) # отримуємо картинку
# with open("image.jpg","wb") as file: # відкриваємо файл для запису картинки або ж створюємо його
#     file.write(img_response.content) # записуємо картинку в файл


import requests
from bs4 import BeautifulSoup

# --- ВХОДНЫЕ ДАННЫЕ ---
URL = "https://www.mcdonalds.com/ua/uk-ua.html"
LIMIT = 1 # 0 = все элементы
# ---------------------

# 1. Отправляем запрос и получаем HTML
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(URL, headers=headers, timeout=10)

# 2. Создаем объект BeautifulSoup
soup = BeautifulSoup(response.content, 'lxml')

# 3. Извлечение данных (по типу: prices)
# Поиск элементов по селекторам, содержащим слово "price"
items = soup.select('div[class*="price"], span[class*="price"], strong')
results = [item.get_text(strip=True) for item in items]
final_results = results[:1] # Применяем лимит

# 4. Вывод
print(f"URL: {URL}")
print(f"Извлечено {len(final_results)} элементов:")
for i, result in enumerate(final_results, 1):
    print(f"  {i}. {result}")

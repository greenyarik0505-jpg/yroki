# import requests # імпортуємо бібліотеку requests 

# def get_weather(city,apikey):
#     url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid":apikey,
#         "units":"metric",
#         "lang":"ua" 
#     }
#     try:
#         response = requests.get(url,params=params) # отримуємо данні з API
#         response.raise_for_status() # перевіряємо чи успішно отримали наші данні
#         data = response.json() # перетворюємо данні в json
#         temp = data["main"]["temp"]
#         feels_like = data["main"]["feels_like"]
#         description = data["weather"][0]["description"]
#         humidity = data["main"]["humidity"]
#         print(f"Температура в {city} ---- {temp}°C")
#         print(f"Відчувається як {feels_like}°C")
#         print(f"Опис погоди: {description}")
#         print(f"Вологість: {humidity}%")
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
# apikey = "ba1e7bd01c86b8bf05cf0d9e2bdb39a0"
# get_weather("Kyiv",apikey)



# import requests

# url = "https://api.chucknorris.io/jokes/random"

# response = requests.get(url)

# data = response.json()

# shytka = data["value"]

# print(f"Лучшая шутка ето: {shytka}")


import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

response = requests.get(url)

data = response.json()

print(data)
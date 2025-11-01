# 4. Напиши функцію, яка повертає найбільше число зі списку. Вона повинна мати один
# іменований аргумент: numbers (список чисел).  

# def findmax(numbers):
#     return max(numbers)
# a = [5,2,5,3,5,7,8,3,3,6,8,5]
# findmax([5,2,5,3,5,7,8,3,3,6,8,5])
# print(findmax([5,2,5,3,5,7,8,3,3,6,8,5]))
# print(findmax(numbers=a))
# [[1,2,3],[4,5,6],[7,8,9]]

# 5. Напиши функцію, яка перевіряє, чи є рядок паліндромом без урахування регістру
# (букви великі або малі). Вона повинна мати один іменований аргумент: string
# (рядок).


# def паліндром(string):
#     text = string.lower()
#     textreverse = text[::-1]
#     return text == textreverse
# textik = input("Введіть текст для перевірки паліндрому ")
# print(паліндром(string=textik))


# 9. Напиши функцію, яка повертає суму чисел зі списку, якщо він не порожній. Якщо
# список порожній, функція повертає нуль. Функція повинна мати один необов'язковий
# параметр: numbers (список чисел)

# def сумасписку(numbers=[]):
#     if numbers:
#         return sum(numbers)
#     else:
#         return 0
# print(сумасписку())
# print(сумасписку([1,2,3,4]))
# print(сумасписку([99,-99,1]))
# 1. Напиши функцію, яка приймає два аргументи: name і age. Вона повинна вивести
# повідомлення, що містить ім'я та вік, використовуючи іменовані аргументи.

# def zelovek (name,age):
#     print("Меня звяти", name ,"та мені",age,"лет")
# zelovek(name="Ярік",age=100)

# 3. Улюблена книга: напишіть функцію favorite_book(), яка отримує один параметр title.
# Функція має виводити повідомлення виду "One of my favorite books is Alice in
# Wonderland". Викличте функцію і переконайтеся в тому, що назву книги правильно
# передають як аргумент під час виклику функції.

# def roblox(roblox_prayer1,roblox_prayer2,roblox_prayer3):
#     print("Моя улюблена игра в роблоксі",roblox_prayer1,roblox_prayer2,"та",roblox_prayer3)
# roblox(roblox_prayer1="Steal Brainrot",roblox_prayer2="Plants vs Brainrot",roblox_prayer3="Counter Blox")

# 7. Назви міст: напишіть функцію city_country(), яка отримує назву міста та країну.
# Функція має повертати рядок у форматі "Santiago, Chile". Викличте свою функцію
# принаймні для трьох пар "місто - країна" і виведіть повернене значення

# def city_country(city,country):
#     print("Місто",city,"Країна",country)
#     return city,country
# city_country(city="Реал",country="Испанія")
# city_country(city="Київ",country="Україна")
# city_country(city="Париж",country="Франция")

# Домашка
# 1. Міста: напишіть функцію describe_city(), яка отримує назви міста та країни. 
# Функція має виводити просте повідомлення (наприклад, "Reykjavik is in Iceland"). 
# Задайте параметру країни значення за замовчуванням. 
# Викличте свою функцію для одного міста.

# def describe_city(c, k="Ukraine"):
#     print(f"{c} is in {k}.")

# describe_city("Kyiv")


# 2. Напишіть функцію під назвою calculate_rectangle_area, яка приймає два аргументи —
# довжину і ширину прямокутника, а повертає його площу. 
# Використайте цю функцію для обчислення площі прямокутника зі сторонами 4 і 5 
# і виведіть результат.

# def calculate_rectangle_area(l, w):
#     return l * w

# print("Площа прямокутника:", calculate_rectangle_area(4, 5))


#  3. Написати функцію пошуку максимального значення з переданого їй списку значень.

# def find_max_value(v):
#     return max(v)

# print("Максимальне значення:", find_max_value([3, 7, 1, 9, 4]))

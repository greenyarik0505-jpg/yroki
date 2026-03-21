# Умовний оператор if (якщо)
# a = int(input("Скільки вам років?"))
# if a >= 18: # Тут ми пишемо умову
#     print("Ви можете голосувати")
# else:
#     print("Ви не можете голосувати")



# ! УМОВИИИ 
# Умова повинна бути True або False
# для створення умови ми використовуємо оператори порівняння
# == - дорівнює
# != - не дорівнює
# > - більше
# < - менше
# >= - більше або дорівнює
# <= - менше або дорівнює
# not - не
# and - і
# or - або
# In - чи міститься в **** 
# not in - не міститься в ****
# Приклад з in 
# code = "1234567890"
# print("1" in code)
# if "1" in code:
#     print("Код містить 1")
# else:
#     print("Код не містить 1")

# code = "1234567890" # Це є строка
# print(type(code)) # Тип даних
# print(code.isdigit()) # Чи лише числа 
# print(isinstance(code, int)) # Чи це int?
# if code.isdigit():
#     print("Код є числом")
# else:
#     print("Код не є числом")
    
# if isinstance(code, int):
#     print("Код є числом")
# else:
#     code = int(code)
#     print(code)
# if isinstance(code, int):
#     print("Код став числом")


# ! Цикл WHILE ( доки виконується умова, виконується блок коду)
# while умова:
#     блок коду
#     break - вихід з циклу
#     continue - перехід до наступного циклу
#     pass - нічого не робити
#     return - повернення значення
#     yield - повернення значення і збереження стану функції
#     raise - викидання виключення
#     try - спроба виконати блок коду
#     except - обробка виключення
#     finally - виконання після блоку коду

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# #! Continue - перехід до наступного циклу з пропуском 
# login = "admin"
# while True:
#     login = input("Введіть логін: ")
    
#     if login != "admin":
#         print("Логін не вірний")
#         continue    
#     password = input("Введіть пароль: ")
#     if password == "123456":
#         print("Пароль вірний")
#         print("Вітаю, admin")
#         break
#     else:
#         print("Пароль не вірний")
#         continue

        
#! ЦИКЛ ФОР for (для кожного елемента в списку, кортежі, множині, словнику)
# for елемент in список, кортеж, множина, словник:
#     блок коду
#     break - вихід з циклу
# pass - нічого не робити
# return - повернення значення
# yield - повернення значення і збереження стану функції
# raise - викидання виключення
# try - спроба виконати блок коду
# except - обробка виключення
# finally - виконання після блоку коду

# for i in range(10):
#     print(i)
# for i in range(1, 10):
#     print(i)

#! Індекси починаються завжди з 0 , перший елемент завжди 0
#! Останній елемент завжди -1
#! range(10) - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#! range(1, 10) - 1, 2, 3, 4, 5, 6, 7, 8, 9
#! range(1, 10, 2) - 1, 3, 5, 7, 9
#! range(10, 1, -1) - 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
#! range(10, 1, -2) - 10, 8, 6, 4, 2
#! range(10, 1, -2) - 10, 8, 6, 4, 2

# a = "TikTok"
#! Розбиваємо на індекси
# [T=0, i=1, k=2, T=3, o=4, k=5] 
# for i in a: 
#     print(i) # prin(i) == print(a[i]) , i =0, 1, 2, 3, 4, 5

#! Задача змінити літери T на B 
# a = "TikTok"
# for i in a:
#     # print(i)
#     if i == "T": # if "T" == "T" , "i" == "T", "k" == "T", "T" == "T", "o" == "T", "k" == "T"
#         print("B",end="")
#     else:
#         print(i,end="")

#! Range() - це функція яка повертає послідовність чисел
#! Вона приймає 3 аргументи: start, stop, step 
#! start - початок послідовності (початкове значення)
#! stop - кінець послідовності (кінцеве значення)
#! step - крок послідовності (крок)
for i in range(1,10,2):
    print(i)

print("---------------------------------")
print("КАЛЬКУЛЯТОР 3000")
print("---------------------------------")

while True:
    print("МЕНЮ:")
    print("1 - Додати ")
    print("2 - Відняти ")
    print("3 - Помножити ")
    print("4 - Поділити ")
    print("5 - Вийти з програми")
    
    vubor = input("Оберіть номер (1-5): ")

    if vubor == "5":
        print("Програма завершує роботу.")
        break

    if vubor == "1" or vubor == "2" or vubor == "3" or vubor == "4":
        
        perhe_chuclo = int(input("Введіть перше число: "))
        dryge_chuclo = int(input("Введіть друге число: "))

        if vubor == "1":
            rezultat = perhe_chuclo + dryge_chuclo
            print("РЕЗУЛЬТАТ:", rezultat)

        if vubor == "2":
            rezultat = perhe_chuclo - dryge_chuclo
            print("РЕЗУЛЬТАТ:", rezultat)

        if vubor == "3":
            rezultat = perhe_chuclo * dryge_chuclo
            print("РЕЗУЛЬТАТ: ", rezultat)

        if vubor == "4":
            if dryge_chuclo != 0:
                rezultat = perhe_chuclo / dryge_chuclo
                print("РЕЗУЛЬТАТ:",  rezultat)
            else:
                print("ПОМИЛКА: На нуль ділити не можна!")

        print("--------------------")

    else:
        print("ПОМИЛКА: Введіть число від 1 до 5 ")

# 1
def privet(name1):
    print(f"Привіт, {name1}!")

# 2
def dodavanie(a, b):
    return a + b

# 3
def proverka_number(number1):
    return number1 % 2 == 0

# 4
def vvod_dannih():
    vveden_name = input("Введіть ім'я: ")
    vvedenoe_number = int(input("Введіть число для перевірки: "))
    return vveden_name, vvedenoe_number

def vaznoe():
    vopros, number2 = vvod_dannih()
    
    privet(vopros)
    
    rezultat_summi = dodavanie(15, 25)
    print(f"Сума 15 + 25 = {rezultat_summi}")
    
    proverka_result = proverka_number(number2)
    print(f"Чи є число {number2} парним? {proverka_result}")

vaznoe()

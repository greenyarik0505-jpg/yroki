# 1
price = int(input("Введіть ціну однієї книги: "))
kolichestvo = 2
while kolichestvo <= 10:
    print(kolichestvo, "шт. =", kolichestvo * price)
    kolichestvo += 1

# 2
line = 1
while line <= 5:
    print(line, ": 00000")
    line += 1

# 3
number = -10
while number <= 10:
    print(number)
    number += 1

# 4
parnux = 0
num = int(input("Введіть число (0 для виходу): "))
while num != 0:
    if num % 2 == 0:
        parnux += 1
    num = int(input("Наступне число: "))
print("Кількість парних:", parnux)

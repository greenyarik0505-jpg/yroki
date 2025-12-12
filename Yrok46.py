# import sys
# import time
# import random
# import os
# print("=========================================")
# print("  ЛАСКАВО ПРОСИМО У ПІДЗЕМЕЛЛЯ PYTHON ")
# print("=========================================")
# print("")
# class Colors:
#     HEADER = '\033[95m'
#     BLUE = '\033[94m'
#     CYAN = '\033[96m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = '\033[91m'
#     BOLD = '\033[1m'
#     END = '\033[0m'
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')
# def type_text(text, speed=0.04, color=Colors.END):
#     for char in text:
#         sys.stdout.write(color + char + Colors.END)
#         sys.stdout.flush()
#         time.sleep(speed)
#     print()
# def firework():
#     colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.HEADER]
#     x = random.randint(10, 50)
#     print(" " * x + f"{random.choice(colors)}    .    {Colors.END}")
#     time.sleep(0.1)
#     print(" " * x + f"{random.choice(colors)}  \ | /  {Colors.END}")
#     print(" " * x + f"{random.choice(colors)} -- * -- {Colors.END}")
#     print(" " * x + f"{random.choice(colors)}  / | \  {Colors.END}")
#     time.sleep(0.1)

#     sys.stdout.write(Colors.YELLOW + "     LOADING: [")
#     for i in range(20):
#         time.sleep(0.01)
#         sys.stdout.write("#")
#         sys.stdout.flush()
#     sys.stdout.write("] 100% DONE" + Colors.END + "\n")
#     time.sleep(0.3)
#     clear_screen()   
# print("\n" * 2)
# type_text("     СИСТЕМА: Завантаження фінального протоколу...", 0.05, Colors.CYAN)
# time.sleep(1)
# type_text("     СИСТЕМА: Обробка даних гравців...", 0.05, Colors.CYAN)
# time.sleep(1)
# time.sleep(1)
# clear_screen()


# print("Вступ до гри")
# print("Брама")
# nik = input("Введіть свій ник: ").upper()
# print(f"Привіт {nik}")
# zbroy =input("Що ти хочешь взяти меч, лук чи магія: ")
# print(f"Ти взяв {zbroy} і йдеш далі")

# print("╔══════════════════════════╗")
# print("║     ПЕРЕПУСТКА ГЕРОЯ     ║")
# print("╠══════════════════════════╣")

# print(" ╔══════════════════════════╗")
# print(f"║        Ник {nik}         ║")
# print(" ╠══════════════════════════╣")
# print(f"║        Оружие {zbroy}    ║")
# print(" ╠══════════════════════════╣")

# cula = int(input("Введіть свою силу: "))

# magia = int(input("Скільки у тебе магій: "))

# cuma = cula + magia

# print(f"Загальний результат {cuma}")



# zdorov = 110

# print("ЗАГАДКА")
# print("Скільки буде 5 * 5?")
# hp = 110
# a = int(input("Введи відповідь: "))
# if a == 25:
#      print("Шлях відкрито: ")
# else:
#      hp -= 35
#      print("Неправильно! Ти втратив здоров'я")
#      print(f"У тебе залишилось зров'я {hp}")

# print("ЗАГАДКА")
# print("Весит груша нельзя скушать")
# print("Підсказка:Відповідь на англійській")
# hp = 110
# a = (input("Введи відповідь: "))
# if a == "Lamp":
#      print("Шлях відкрито: ")
# else:
#      hp -= 35
#      print("Неправильно! Ти втратив здоров'я")
#      print(f"У тебе залишилось зров'я {hp}")

# print("ЗАГАДКА")
# print("Що можна зловити але не можна кинути")
# print("Підсказка:Відповідь на англійській")
# hp = 110
# a = (input("Введи відповідь: "))
# if a == "Cold":
#      print("Шлях відкрито: ")
# else:
#      hp -= 35
#      print("Неправильно! Ти втратив здоров'я")
#      print(f"У тебе залишилось зров'я {hp}")

# print(f"Твоє фінальне здоровʼя {zdorov}")
     



# print("Вхід до гри")
# print("СКАРБНИЦЯ")
# loot = ["Золото", "Меч", "Ключ", "Діамант"] 
# for item in loot: 
#     print(f"Ти знайшов: {item}") 
# print("Гру пройдено!") 












# type_text("\n     ВЕЛИКА ПЕРЕМОГА!", 0.1, Colors.GREEN)
# print("-" * 50)
# type_text("     Запускаємо святковий салют...", 0.05, Colors.HEADER)
# time.sleep(0.5)

# for _ in range(15): 
#     firework()



# type_text("     НАД ПРОЕКТОМ ПРАЦЮВАЛИ:", 0.05, Colors.YELLOW)
# time.sleep(0.5)
# print(f"     {Colors.CYAN}➤ [Вартовий Брами]{Colors.END} ..... Відповідав за Вхід")
# time.sleep(0.5)
# print(f"     {Colors.CYAN}➤ [Сфінкс]{Colors.END} ............. Відповідав за Логіку")
# time.sleep(0.5)
# print(f"     {Colors.CYAN}➤ [Воїн]{Colors.END} ............... Відповідав за Цикли While")
# time.sleep(0.5)
# print(f"     {Colors.CYAN}➤ [Скарбник]{Colors.END} ........... Відповідав за Списки")
    
# print("\n" + "-" * 50)
# time.sleep(1)

import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2,detectionCon=0.8)
while True:
     success,img = cap.read()
     hand,img = detector.findHands(img,draw=True) 
     # список руки --- [0,0,0,0,0]
     if hand:
        totalfingers = 0
        for hands in hand:
            fingers = detector.fingersUp(hands)
            totalfingers += fingers.count(1)
        cv2.putText(img,str(totalfingers),(50,150),cv2.FONT_HERSHEY_COMPLEX,10,(255,0,255),10)
        cv2.imshow("Finger counter",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

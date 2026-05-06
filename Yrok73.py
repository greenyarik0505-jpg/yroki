import random

hunger = 50
energy = 70
mood = 60
day = 1
sans_podia = 0

def clamp(value):
    if value < 0:
        return 0
    if value > 100:
        return 100
    return value

def show_status():
    print(f"\nДень {day}")
    print(f"Hunger: {hunger} | Energy: {energy} | Mood: {mood}")

print("PET SIMULATOR")
print("1 - Легко")
print("2 - Середне")
print("3 - Сложность")
cloznosti = int(input("Виберить сложность: "))

while True:
    show_status()
    print("1. Feed")
    print("2. Train")
    print("3. Sleep")
    print("4. Exit")

    choice = input("Дія: ").strip()

    if choice == "1":
        hunger -= 20
        mood += 5
        print("Улюбленець поїв.")
        sans_podia = 25

    elif choice == "2":
        energy -= 20
        hunger += 15
        mood += 10
        print("Тренування завершено.")
        sans_podia = 25

    elif choice == "3":
        energy += 30
        hunger += 10
        print("Сон відновив енергію.")
        sans_podia = 25

    elif choice == "4":
        print("Симулятор завершено.")
        break
    else:
        print("Невідома дія.")
        continue
    
    if sans_podia == 25:
        a = random.randint(1,25)
        if a == 6 or 9 or 12 or 15:
            podia = random.randint(1,4)

            if podia == 1:
                print("Трамп кинул ядерку на Иран. Настрой +")
                mood += 10
            if podia == 2:
                print("Зомбиапокалипс. Енергия -")
                energy -= 20
            if podia == 3:
                print("Тебе задали куче дз з матеше. Енергия -")
                energy -= 10
            if podia == 4:
                print("Уроки отменили. Настрой +")
                mood += 20

    hunger = clamp(hunger)
    energy = clamp(energy)
    mood = clamp(mood)
    day += 1

    if hunger == 100:
        print("Улюбленець тікає шукати їжу")

    if energy == 0:
        print("Енергія вичерпана тренування заблоковане")

    if mood == 0:
        print("Настрій дорівнює 0 гра завершується")
        break

    if cloznosti == 1:
        if day > 10 and mood >= 50:
            print("Ти завершив тренувальний сезон.")
            break
    if cloznosti == 2:
        if day > 30 and mood >= 65:
            print("Ти завершив тренувальний сезон.")
            break
    if cloznosti == 3:
        if day > 60 and mood >= 80:
            print("Ти завершив тренувальний сезон.")
            break

import random

attempts = 0
max_attempts = 7
print("===================")
print("NUMBER HUNTER")
print("===================")
print("1 - easy")
print("2 - normal")
print("3 - hard")
print("===================")
rehum = int(input("Вибери режим сложности: "))
print("===================")
print("NUMBER HUNTER")
print("===================")
print("Я загадав число від 1 до 50.")

while True:
    if rehun == 1:
            if attempts != 8:
                print("Я загадав число від 1 до 30.")
                secret = random.randint(1, 30)
                answer = input("Твоя версія: ").strip()

                if not answer.isdigit():
                    print("Введи саме число.")
                    continue

                guess = int(answer)
                attempts += 1

                if guess == secret:
                    print(f"Точно. Ти знайшов число за {attempts} спроб.")
                    break
                
                if 5 <= secret - answer
                    print("Гаряче")

                if 15 <= secret - answer
                    print("Тепло")

                else:
                    print("Холодно")
            else:
                print("Спроби закінчились")
                break

    if rehun == 2:
        if attempts != 7:
            print("Я загадав число від 1 до 50.")
            secret = random.randint(1, 50)
            answer = input("Твоя версія: ").strip()

            if not answer.isdigit():
                print("Введи саме число.")
                continue

            guess = int(answer)
            attempts += 1

            if guess == secret:
                print(f"Точно. Ти знайшов число за {attempts} спроб.")
                break
            
            if 5 <= secret - answer
                print("Гаряче")

            if 15 <= secret - answer
                print("Тепло")

            else:
                print("Холодно")
        else:
            print("Спроби закінчились")
            break

    if rehun == 3:
        if attempts != 7:
            print("Я загадав число від 1 до 100.")
            secret = random.randint(1, 100)
            answer = input("Твоя версія: ").strip()

            if not answer.isdigit():
                print("Введи саме число.")
                continue

            guess = int(answer)
            attempts += 1

            if guess == secret:
                print(f"Точно. Ти знайшов число за {attempts} спроб.")
                break
            
            if 5 <= secret - answer
                print("Гаряче")

            if 15 <= secret - answer
                print("Тепло")

            else:
                print("Холодно")
        else:
            print("Спроби закінчились")
            break

import random

rehum = 0
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
    if rehum == 1:
            secret = random.randint(1, 30)
            if attempts != 8:
                print("Я загадав число від 1 до 30.")
                answer = int(input("Твоя версія: "))


                guess = int(answer)
                attempts += 1

                if guess == secret:
                    print(f"Точно. Ти знайшов число за {attempts} спроб.")
                    break
                
                abz = secret - answer
                
                if 5 >= abz:
                    print("Гаряче")

                if 15 >= abz:
                    print("Тепло")

                else:
                    print("Холодно")
            else:
                print("Спроби закінчились")
                break

    if rehum == 2:
        secret = random.randint(1, 50)
        if attempts != 7:
            print("Я загадав число від 1 до 50.")
            answer = int(input("Твоя версія: "))


            guess = int(answer)
            attempts += 1

            if guess == secret:
                print(f"Точно. Ти знайшов число за {attempts} спроб.")
                break
            
            abz = secret - answer
            
            if 5 >= abz:
                print("Гаряче")

            if 15 >= abz:
                print("Тепло")

            else:
                print("Холодно")
        else:
            print("Спроби закінчились")
            break

    if rehum == 3:
        secret = random.randint(1, 100)
        if attempts != 7:
            print("Я загадав число від 1 до 100.")
            answer = int(input("Твоя версія: "))

            guess = int(answer)
            attempts += 1

            if guess == secret:
                print(f"Точно. Ти знайшов число за {attempts} спроб.")
                break
            
                abz = secret - answer
                
                if 5 >= abz:
                    print("Гаряче")

                if 15 >= abz:
                    print("Тепло")

                else:
                    print("Холодно")
        else:
            print("Спроби закінчились")
            break

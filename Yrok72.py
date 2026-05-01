import random

player_score = 0
computer_score = 0
rounds = 0

print("DICE DUEL")
a = int(input(f"\nВиберите кількість раундів от 1 до 20."))

if a == "":
    rounds = 5
    
elif a < 1:
    rounds = 1

elif a > 20:
    rounds = 20
else:
    rounds = a

for round_number in range(1, rounds + 1):
    input(f"\nРаунд {round_number}. Натисни Enter, щоб кинути кубик.")

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"Ти кинув: {player_roll}")
    print(f"Комп'ютер кинув: {computer_roll}")
    
    if player_roll == 6:
        player_score =+ 1
        print("У игрока додатковий балл")
    
    if computer_roll == 6:
        computer_roll =+ 1
        print("У игрока додатковий балл")
    
    if player_roll > computer_roll:
        print("Раунд за тобою.")
        player_score += 1
    elif computer_roll > player_roll:
        print("Раунд за комп'ютером.")
        computer_score += 1
    else:
        print("Нічия.")

print(f"\nФінальний рахунок: {player_score}:{computer_score}")

if player_score > computer_score:
    print("Ти виграв дуель.")
elif computer_score > player_score:
    print("Комп'ютер виграв дуель.")
else:
    print("Матч завершився нічиєю.")

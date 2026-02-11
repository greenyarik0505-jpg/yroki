club_name = "Привет"
print("=========================")
print("Ласкаво просимо до клубу:", club_name)
print("=========================")

guests = set()

while True:
    name = input("Хто заходить или введіть вихід: ")
    print("=========================")

    if name.lower() == "вихід":
        break

    guests.add(name)
print("=========================")
print("За сьогодні прийшли" , len(guests))
print("=========================")
if len(guests) > 0:
    print("Хто сьогодні приходив в клуб" , guests)
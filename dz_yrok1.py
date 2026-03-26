new_knuga = input("Введіть назву книги: ")
avtor = input("Введіть автора: ")

ctranuzu_input = input("Скільки сторінок у книзі? ")
ctranuzu = int(ctranuzu_input)

price_input = input("Яка ціна книги? ")
price = float(price_input)

doctypno_input = input("Книга доступна? (так/ні): ")
if doctypno_input == "так":
    doctypno = True
else:
    doctypno = False

print("\nДані про книгу:")
print(new_knuga)
print(avtor)
print(ctranuzu)
print(price)
print(doctypno)

print("\nРезультат пошуку:")
poisk = input("Яку книгу ви шукаєте? ")
if poisk == new_knuga:
    print("Книгу знайдено!")
    if doctypno == True:
        print("Вона доступна она є на полиці.")
    else:
        print("Книга зараз недоступна она видана другому читачю.")
else:
    print("Такої книги немає в базі.")

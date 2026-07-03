number = 1
user_input = 0

while (number != user_input):
    user_input = int(input("Введите загаданный номер: "))
    if (number != user_input):
        while (number != user_input):
            user_input = int(input("Попробуйте снова: "))
    else:
        break

print("Поздравляю! Вы угадали!")

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))


def universal_func(func):
    def wrapper(*args):
            number1 = args[0]
            number2 = args[1]

            if number1 == number2:
                operation = '+'
            if number1 > number2:
                operation = '-'
            if number2 > number1:
                operation = '/'
            if number2 < 0 or number1 < 0:
                operation = '*'

            return func(number1, number2, operation)

    return wrapper

@universal_func
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(number1, number2))

import sys
sys.set_int_max_str_digits(100000)


def fibonachiNums():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        old_num1 = num1
        num1 = num2
        num2 = old_num1 + num2


fibonachiNums = fibonachiNums()

for i in range(1, 100000000):
    fibbonachiNum = next(fibonachiNums)
    if i == 5:
        print(f"Пятое число: {fibbonachiNum}")
    if i == 200:
        print(f"Двухсотое число: {fibbonachiNum}")
    if i == 1000:
        print(f"Тысячное число: {fibbonachiNum}")
    if i == 100000:
        print(f"Cтотысячное число: {fibbonachiNum}")

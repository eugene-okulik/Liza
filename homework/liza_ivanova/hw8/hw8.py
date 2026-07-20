import random


def salaryBonusResult():
    salary = int(input("Введите зарплату: "))
    bonus = random.choice([True, False])
    if bonus:
        salary += random.randint(0, 30000)
        return salary
    else:
        return salary


print(f"${salaryBonusResult()}")

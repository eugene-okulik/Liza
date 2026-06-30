text = 'результат операции: 42'
print(int(text[19: ]) + 10)

text = 'результат операции: 514'
print(int(text[(text.find(':') + 1): ]) + 10)

text = 'результат работы программы: 9'
print(int(text[(text.index(':') + 1): ]) + 10)


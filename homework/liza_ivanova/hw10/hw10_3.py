PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

print({word.split()[0]: int(word.split()[1][: -1]) for word in PRICE_LIST.splitlines()})

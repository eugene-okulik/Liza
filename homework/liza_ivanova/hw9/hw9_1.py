temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]

hot_temp_list = list(filter(lambda t: t > 28, temperatures))
print(f"Список жарких дней:{(hot_temp_list)}")
print(f"Самая высокая температура из нового списка:{max(hot_temp_list)}")
print(f"Самая низкая температура из нового списка:{min(hot_temp_list)}")
print(f"Средняя температура из нового списка:{round(sum(hot_temp_list)/len(hot_temp_list))}")

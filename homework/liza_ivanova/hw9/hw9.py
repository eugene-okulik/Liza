import datetime

given_date = "Jan 15, 2023 - 12:05:33"
given_date_pyth_type = datetime.datetime.strptime(given_date, "%b %d, %Y - %H:%M:%S")
print(f"Месяц из даты: {given_date_pyth_type.strftime("%B")}")
print(f"Дата в формате из дз: {given_date_pyth_type.strftime('%d.%m.%Y, %H:%M')}")

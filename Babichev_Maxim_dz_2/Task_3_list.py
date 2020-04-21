# Решение через список
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
number_month = int(input('Введите номер месяца: '))
if number_month == 1 or number_month == 2 or number_month == 12:
    print(season_list[0])
elif number_month == 3 or number_month == 4 or number_month == 5:
    print(season_list[1])
elif number_month == 6 or number_month == 7 or number_month == 8:
    print(season_list[2])
elif number_month == 9 or number_month == 10 or number_month == 11:
    print(season_list[3])

# Решение через словарь
dictionary_month = {'Зима': (12, 1, 2),
                    'Весна': (3, 4, 5),
                    'Лето': (6, 7, 8),
                    'Осень': (9, 10, 11)
                    }
number_month = int(input('Введите номер месяца '))
for key_month in dictionary_month.keys():
    if number_month in dictionary_month[key_month]:
        print(key_month)

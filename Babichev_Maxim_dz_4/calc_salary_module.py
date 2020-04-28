from sys import argv

script_name, production, rate, bonus = argv


def calc_salary(production, rate, bonus):
    """ Функция возвращает итоговое значение заработной платы
        Все аргументы переведем в числа,
        так как в командной строке аргументы будут строковыми
    """
    production = int(production)
    rate = int(rate)
    bonus = int(bonus)
    salary = (production * rate) + bonus
    return salary


print(calc_salary(production, rate, bonus))

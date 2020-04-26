def calc_division_numbers(number1=0, number2=1):
    """Возвращает результат деления двух чисел.

    number1 - делимое
    number2 - делитель
    """
    try:
        division = number1 / number2
        print(f'Деление числа {number1} на число {number2} = {division}')
    except ZeroDivisionError:
        division = 0
        print(f'Вы пытаетесь поделить {number1} на {division} \nДелить на ноль запрещено!')
    return division


# num1 = float(input('Введите делимое число: '))
# num2 = float(input('Введите делитель: '))
calc_division_numbers(5, 0)

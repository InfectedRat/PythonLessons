def sum_two_max(number1, number2, number3):
    """Вычисляет два максимальных числа, и возвращает их сумму"""
    if number2 < number1 < number3:
        return number1 + number3
    elif number1 >= number3 and number2 >= number3:
        return number1 + number2
    else:
        return number2 + number3


print(sum_two_max(6, 10, 20))

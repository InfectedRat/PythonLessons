def my_func(x=1, y=1):
    """Возводит в степень через цикл"""
    result = 1
    for el in range(abs(y)):
        result = x * result
    return 1 / result


print(my_func(2, -5))

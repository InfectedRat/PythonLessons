#   Более удобный вариант программы
# result_day_first = int(input('Введите результат спортсмена в первый день '))
# result_check_exceed = int(input('Введите результат для поиска дня '))
# step_increase = 1.1  # 10% - шаг с которым увеличиваем каждый день результат спортсмена
# number_day = 1  # отправной номер дня по умолчанию
#
# while result_day_first < result_check_exceed:
#     result_day_first = result_day_first * step_increase
#     number_day = number_day + 1
# else:
#     print('Номер дня, когда спортсмен превысил', number_day)

#  Вариант со статичными данными
result_day_first = str(2)  # фейковые статичные данные результата первого дня, как будто из input
result_check_exceed = str(3)  # фейковые статичные данные для поиска превышения результата
step_increase = 1.1  # 10% - шаг с которым увеличиваем каждый день результат спортсмена
number_day = 1  # отправной номер дня по умолчанию

while float(result_day_first) < float(result_check_exceed):
    result_day_first = float(result_day_first) * step_increase
    number_day = number_day + 1
else:
    print(number_day)

# test commit 1
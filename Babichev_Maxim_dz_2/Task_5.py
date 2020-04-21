# Структура рейтинг
rating_list = [7, 5, 3, 3, 2, 1]
number_user = int(input('Введите число '))
for elem in rating_list:
    if number_user >= elem:
        rating_list.insert(rating_list.index(elem), number_user)
        break
print(rating_list)

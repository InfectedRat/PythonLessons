# Считываем строку от пользователя
user_string = input('Введите произвольную строку ')
user_string = user_string.split()
for num_elem, elem in enumerate(user_string):
    print(elem[:10:])

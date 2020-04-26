# dict_user = {'name': input('Введите Имя '),
#              'surname': input('Введите Фамилию '),
#              'year': input('Введите Год '),
#              'city': input('Введите Город '),
#              'email': input('Введите элеткронную почту '),
#              'phone': input('Введите Телефон ')}

dict_user = {'name': 'Иван',
             'surname': 'Иванов',
             'year': '1487',
             'city': 'Ivan_city',
             'email': 'Ivan.Ivanovich@mymail.com',
             'phone': '+78956541236'}


def show_user_information(name, surname, year, city, email, phone):
    """Выводит информацию о пользователе. Именованные аргументы"""
    return print(f'Данные о пользователе: {name}, {surname}, {year}, {city}, {email}, {phone}')


# show_user_information(*dict_user.values())
show_user_information(name=dict_user['name'], surname=dict_user['surname'], year=dict_user['year'],
                      city=dict_user['city'], email=dict_user['email'], phone=dict_user['phone'])

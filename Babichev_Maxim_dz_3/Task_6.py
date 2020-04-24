def int_func(u_str):
    """Возвращает слово с большой буквы"""
    return u_str.title()


print(int_func('памагите'))


def u_split_string(j_str):
    """Возвращает строку в которой каждое слово с большой буквы"""
    list1 = []
    user_string = j_str.split()
    for elem in user_string:
        list1.append(int_func(elem))  # Используем функцию int_func
    return ' '.join(list1)


print(u_split_string('строка состоит из слов начинающихся с большой буквы'))

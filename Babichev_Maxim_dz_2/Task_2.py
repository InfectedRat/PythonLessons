user_list = []
while True:  # Задаем произвольный список
    element = input('Введите каждый элемент спика нажимая "Enter", если закончили оставьте пустым и нажмите "Enter" ')
    if not element:
        break
    user_list.append(element)
tmp_list = user_list.copy()  # Сохраняем эталонную копию списка
if len(user_list) % 2 == 0:  # Проверям четное или не четное количество элементов в списке
    user_list[::2] = user_list[1::2]  # Меняем местами элементы списка
    user_list[1::2] = tmp_list[::2]
    print(user_list)
if len(user_list) % 2 != 0:
    last_element = user_list.pop(len(user_list) - 1)  # Сохраняем последний элемент, чтобы избежать ошибки срезов
    tmp_list = user_list.copy()
    user_list[::2] = user_list[1::2]
    user_list[1::2] = tmp_list[::2]
    user_list.append(last_element)
    print(user_list)

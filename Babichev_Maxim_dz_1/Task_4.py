# оставил ввод через input
user_num = int(input('Введите целое число '))
mod_num = user_num % 10  # остаток
int_num = user_num // 10  # целое
while int_num > 0:  # перебор
    if int_num % 10 > mod_num:
        mod_num = int_num % 10  # записываем новую потенциально максимальную цифру
    int_num = int_num // 10  # избавлаяемся орт предыдущей проверямой
print(mod_num)

from itertools import count
from math import factorial


# tmp_lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# tmp_lst = [1, 2, 3, 4]

# def fact():
#     tmp_lst_2 = [el * tmp_lst.index(el - 1) for el in tmp_lst]
#     yield tmp_lst_2

def fact():
    for el in count(1):
        yield factorial(el)


# print(fact())

uff = int(input('Введите число, чтобы узнать сколько лет будет карантин... '))
ff1 = 0
for i in fact():
    if ff1 < uff:
        print(i)
        ff1 += 1
    else:
        break

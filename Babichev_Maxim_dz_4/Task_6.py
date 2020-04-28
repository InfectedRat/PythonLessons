import random
import itertools

# it = int(input('Введите начальную границу генератора: '))
# en = int(input('Введите количество итераций: '))
# rand_lst = [random.randint(it, 500) for _ in itertools.count(en)]
# print(rand_lst)

num = int(input('Введите начальную границу '))
stp = 100  # стоп
for el in itertools.count(num):
    if el > stp:
        break
    else:
        print(el)

tmp_list = [20, 21, 40, 'A', 21, 40, False, 34.5]
iter1 = 0
iter2 = 100
for el in itertools.cycle(tmp_list):
    iter1 += 1
    if iter1 > iter2:
        break
    else:
        print(el)

from functools import reduce


def multiplication(prev_el, el):
    return prev_el * el


tmp_lst = [el for el in range(99, 1001) if el % 2 == 0]
print(reduce(multiplication, tmp_lst))

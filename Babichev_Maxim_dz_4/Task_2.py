import random

rand_lst = [random.randint(0, 500) for _ in range(20)]
new_lst = [el for el in rand_lst if el > rand_lst[rand_lst.index(el) - 1]]
print(rand_lst)
print(new_lst)

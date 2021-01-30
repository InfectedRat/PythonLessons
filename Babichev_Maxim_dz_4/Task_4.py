tmp_lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp_lst_2 = [el for el in tmp_lst if tmp_lst.count(el) > 1]
tmp_lst_3 = set(tmp_lst_2)

print(tmp_lst_3)

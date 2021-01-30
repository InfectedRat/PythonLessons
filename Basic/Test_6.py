tmp_lst = input().split()
# tmp_lst = [4, 8, 0, 3, 4, 2, 0, 3]
tmp_lst_2 = [el for el in tmp_lst if tmp_lst.count(el) > 1]
tmp_lst_3 = set(tmp_lst_2)
tmp_lst = list(tmp_lst_3)
for el in tmp_lst_3:
    print(el, end=' ')

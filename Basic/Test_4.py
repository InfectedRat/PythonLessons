s = input()
ns = ''
i = 0
j = 1
while i < (len(s) - 1):
    if s[i] == s[i + 1]:
        j += 1
    else:
        ns = ns + s[i] + str(j)
        j = 1
    i += 1
print(ns + s[i] + str(j))

 # put your python code
# s = input()
# i = 0
# count = 1
# out = ''
# while i< (len(s) - 1):
#     if s[i] == s[i+1]:
#         count += 1
#     else:
#         out = out + s[i] + str(count)
#         count = 1
#     i +=1
# print(out+ s[i] + str(count))
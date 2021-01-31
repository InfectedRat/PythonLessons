str1 = 'aCggtgttat'
str1 = str1.upper()
print((str1.count('G') + str1.count('C')) / len(str1) * 100)

str1 = 'aCggtgttat'
a = len(str1)
b = str1.lower().count('g')
d = str1.lower().count('c')
print((b + d) / a * 100)

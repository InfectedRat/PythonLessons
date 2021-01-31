a = int(input())
b = int(input())
d = 1
while d % a != 0 or d % b != 0:
    d += 1
    x1 = d % a
    x2 = d % b
    print(f'Пытаемся делить пирог на {d} / {a}, остаток {x1}')
    print(f'Пытаемся делить пирог на {d} / {b} остаток {x2}')
print(d)

# x1 = d % a
# x2 = d % b
# print(d, ' ', x1)
# print(d, ' ', x2)

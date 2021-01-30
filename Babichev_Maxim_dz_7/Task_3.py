class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print(
            'Отрицательный результат')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += f'{"*" * row} \\n'
        result += f'{"*" * (self.quantity % row)}'
        return result


cell1 = Cell(9)
cell2 = Cell(3)
print(cell1)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell2.make_order(9))
print(cell1.make_order(3))

class ComplexNumber:
    def __init__(self, number_1, number_2, *args):
        self.number_1 = number_1
        self.number_2 = number_2
        self.sum1 = 'number_1 + number_2 * n'

    def __add__(self, other):
        print(f'Сумма sum1 и sum2 равна')
        return f'sum1 = {self.number_1 + other.number_1} + {self.number_2 + other.number_2} * n'

    def __mul__(self, other):
        print(f'Произведение sum1 и sum2 равно')
        return f'sum1 = {self.number_1 * other.number_1 - (self.number_2 * other.number_2)} + {self.number_2 * other.number_1} * n'

    def __str__(self):
        return f'sum1 = {self.number_1} + {self.number_2} * n'


sumtotal_1 = ComplexNumber(1, -2)
sumtotal_2 = ComplexNumber(3, 4)
print(sumtotal_1)
print(sumtotal_1 + sumtotal_2)
print(sumtotal_1 * sumtotal_2)
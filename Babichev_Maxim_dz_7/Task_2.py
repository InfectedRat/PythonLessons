class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_coat_square(self):
        return self.size / 6.5 + 0.5

    def get_costume_square(self):
        return self.height * 2 + 0.3

    @property
    def get_full_square(self):
        return str(f'Общая площадь \n'
                   f' {(self.get_coat_square()) + (self.get_costume_square())}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round(self.get_coat_square())

    def __str__(self):
        return f'Необходимо для пальто {self.square_c}'


class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_cos = round(self.get_costume_square())

    def __str__(self):
        return f'Необходимо для костюма {self.square_cos}'


coat = Coat(1, 2)
costume = Costume(3, 4)
print(coat)
print(costume)
print(coat.get_full_square)
print(costume.get_full_square)
print(costume.get_coat_square())
print(costume.get_costume_square())

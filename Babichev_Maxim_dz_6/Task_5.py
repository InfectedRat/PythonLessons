class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Начинаем рисовать'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисуем инструментом {self.title}'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисуем инструментом {self.title}'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисуем инструментом {self.title}'


handle = Handle('Маркер')
pencil = Pencil('Карандаш')
pen = Pen('Ручка')

print(pen.draw())
print(pencil.draw())
print(handle.draw())

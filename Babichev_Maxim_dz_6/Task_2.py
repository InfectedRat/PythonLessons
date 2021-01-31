class Road:
    __depth = 0.70
    __tarmac = 100
    _width = None
    _length = None

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def mass(self):
        return self._length * self._width * self.__tarmac * self.__depth


road = Road(length=466000, width=212235)
print(road.mass())

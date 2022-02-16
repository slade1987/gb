class Road():
    def __init__(self, length, width):
        self._w = width
        self._l = length
        self.result()

    def result(self, weight=25, thickness=5):
        return print('Масса асфальта для покрытия всей дороги равна = ',
                     (self._l * self._w * weight * thickness) / 1000, ' т ')


newRoad = Road(100, 200)

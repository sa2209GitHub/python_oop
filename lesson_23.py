#
#   23
#
# Access Modes:
# piblic, _private, __protected

class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom class initializer was called on the {self.__class__}")
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def get_params(self):
        return (self._x1, self._y1, self._x2, self._y2)


class Line(Geom):
    name = 'Line'

    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        print(f"{self.name} class initializer was called")


class Rect(Geom):
    name = 'Rect'

    def __init__(self, x1, y1, x2, y2, fill='yedllow'):
        super().__init__(x1, y1, x2, y2)
        print(f"{self.name} class initializer was called")
        self._fill = fill

    def get_params(self):
        return (self._x1, self._y1, self._x2, self._y2, self._fill)


l = Line(0, 0, 10, 10)
r = Rect(20, 20, 40, 40, 'black')

print(l.get_params())
print(r.get_params())

print(l.__dict__)
print(r.__dict__)

#
#   26
#
# Collection '__slots__'

import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        del self.x, self.y
        self.x = self.y = 0


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        del self.x, self.y
        self.x = self.y = 0


p = Point(10, 20)
p2d = Point2D(10, 20)
t1 = timeit.timeit(p.reset)
t2 = timeit.timeit(p2d.reset)
print(f"t1: {t1}    t2: {t2}")

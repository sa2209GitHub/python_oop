#
#   5
#
# '@classmethod' and '@staticmethod' Decorators

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        else:
            print("wrong values")

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return (x * x) + (y * y)


v1 = Vector(1, 2)
print(v1.get_coord())
print(Vector.validate(100))
print(Vector.validate(101))

v2 = Vector(100, 101)
print(v2.get_coord())

print(Vector.norm2(5, 6))

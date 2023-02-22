#
# 13
#
# Magic Methods:
# '__str__()', '__repr__()',
# '__len__()' and '__abs__()'

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


class Point:
    def __init__(self, *args):
        print(f"__init__ method was called. *args: {args}")
        self.__coord = args

    def __len__(self):
        return len(self.__coord)

    def __abs__(self):
        return list(map(abs, self.__coord))


cat = Cat('Tom')
print(cat)
print(str(cat))
# ---------------------
p1 = Point(1, 2)
p2 = Point(10, 20, 30)
p3 = Point(100, 200, 300, 400)
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
print(len(p1))
print(len(p2))
print(len(p3))
print(abs(p1))
print(abs(p2))
print(abs(p3))

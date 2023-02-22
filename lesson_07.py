#
#   7
#
# Magic Methods:
# '__setattr__()', '__getattribute__()',
# '__getattr__()' and '__delattr__()'

class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD and self.MIN_COORD <= y <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        print("__getattribute__() mnethod was called")
        if item == 'x':
            raise ValueError("access denied")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print("__setattr__() method was called")
        if key == 'z':
            raise AttributeError("invalid attribute name")
        else:
            object.__setattr__(self, key, value)
            # or
            # self.__dict__[key] = value

    def __getattr__(self, item):
        print("__getattr__() method was called with", item)
        return False

    def __delattr__(self, item):
        print("__delattr__() method was called with", item)
        object.__delattr__(self, item)

    @classmethod
    def set_bounds(cls, min, max):
        cls.MIN_COORD = min
        cls.MAX_COORD = max


# print(Point.__dict__)
p1 = Point(1, 2)            # this will call __setattr__ twice
p2 = Point(10, 20)          # this will call __setattr__ twice
# p1.set_bounds(-100, 100)
# print(p1.__dict__)
# print(Point.__dict__)

p1.x = 4        # this will call __setattr__ once
# p1.z = 5      # this will call __setattr__ with 'invalid attribute name' error


y = p2.y      # this will call __getattribute__
# x = p1.x    # this will call __getattribute__ with 'access denied' error

z = p2.z    # this will call __getattr__
print(z)

del p1.x    # this will call __delattr__
print(p1.__dict__)  # this will call __getattribute__

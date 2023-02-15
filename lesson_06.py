# Encapsulation Mechanism

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coordinates should be integers")

    @classmethod
    def __check_value(cls, n):
        return type(n) is int

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coordinates should be integers")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
print(pt.__dict__)
pt.set_coord(10, 20)
print(pt.__dict__)
print(pt.get_coord())

# pt.set_coord('Hello', 2)
pt2 = Point('Hello', 2)

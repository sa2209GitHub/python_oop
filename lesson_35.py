#
#   35
#
# Custom Metaclasses.
# 'metaclass' Parameter


# Example 1


# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100

#     def get_coords(self):
#         return (self.MIN_COORD, self.MAX_COORD)
def create_class_point(name, base, attrs):
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (self.MIN_COORD, self.MAX_COORD, 'V1   *')


p = Point()
print(p.MIN_COORD, p.MAX_COORD)
print(p.get_coords())
del p, Point


# Example 2


class Meta(type):
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MIN_COORD = 0
        cls.MAX_COORD = 100


class Point(metaclass=Meta):
    def get_coords(self):
        return (self.MIN_COORD, self.MAX_COORD, "V2  **")


p = Point()
print(p.MIN_COORD, p.MAX_COORD)
print(p.get_coords())
del p, Point


# Example 3


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MIN_COORD = 0
    #     cls.MAX_COORD = 100


class Point(metaclass=Meta):
    def get_coords(self):
        return (self.MIN_COORD, self.MAX_COORD, "V3 ***")


p = Point()
print(p.MIN_COORD, p.MAX_COORD)
print(p.get_coords())
del p, Point

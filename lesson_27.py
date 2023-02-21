# How '__slots__' Works With
# @property and Inheritance

# class Point2D:
#     __slots__ = ('x', 'y', '__length')

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__length = (x * x + y * y) ** 0.5

#     @property
#     def length(self):
#         return self.__length

#     @length.setter
#     def length(self, value):
#         self.__length = value


# p = Point2D(10, 20)
# print(p.length)
# p.length = 10
# print(p.length)

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_points(self):
        return {'x': self.x, 'y': self.y}


class Point3D(Point2D):
    __slots__ = ('z')

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def get_points(self):
        points = super().get_points()
        points['z'] = self.z
        return points


p2d = Point2D(1, 2)
print(p2d.get_points())
p3d = Point3D(10, 20, 30)
print(p3d.get_points())

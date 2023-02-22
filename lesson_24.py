#
# 24
#
# Polymorphism

class Primitive:
    def get_perimeter(self):
        raise NotImplementedError(
            "The get_perimeter() method must be overridden in the child class")


class Rectangle(Primitive):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Primitive):
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return 4 * self.a


class Triangle(Primitive):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c


primitive = [
    Rectangle(10, 20), Rectangle(100, 200),
    Square(10), Square(100),
    Triangle(1, 2, 3), Triangle(10, 20, 30),
]

for figure in primitive:
    print(figure.get_perimeter())

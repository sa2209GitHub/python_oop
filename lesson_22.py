# Inheritance. 'super()' Function

class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom class initializer was called on the {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Drawing a primitive")


class Line(Geom):
    name = 'Line'

    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        print("Line class initializer")

    def draw(self):
        print("Line drawing")


class Rect(Geom):
    name = 'Rect'

    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print("Rect class initializer")
        self.fill = fill

    def draw(self):
        print("Drawing a rectangle")


l = Line(0, 0, 10, 10)
r = Rect(1, 1, 20, 20, 'black')

print(l.__dict__)
print(r.__dict__)

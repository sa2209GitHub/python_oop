#
#   20
#
# Inheritance

class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("drawing a primitive")


class Line(Geom):
    name = 'Line'

    def draw(self):
        print("line drawing")


class Rect(Geom):
    name = 'Rect'

    def draw(self):
        print("rectangle drawing")


g = Geom()
print(g.name)
g.set_coords(1, 1, 2, 2)
g.draw()

l = Line()
print(l.name)
l.set_coords(1, 1, 2, 2)
l.draw()

r = Rect()
print(r.name)
r.set_coords(1, 1, 2, 2)
r.draw()

# Class Methods

class Point:
    color = 'red'
    circle = 2

    def set_coord(self, x, y):
        print("set_coord() method was called:", str(self))
        self.x = x
        self.y = y

    def get_coord(self):
        return (self.x, self.y)


pt1 = Point()
pt2 = Point()

pt1.set_coord(1, 2)
pt2.set_coord(10, 20)

print(pt1.__dict__)
print(pt2.__dict__)

print(pt1.get_coord())
print(pt2.get_coord())

#
#   3
#
# Initializer and Finalizer

class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("finalizer method was called")

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


pt1 = Point()
print(pt1.__dict__)
pt2 = Point(1, 2)
print(pt2.__dict__)

del pt1
del pt2

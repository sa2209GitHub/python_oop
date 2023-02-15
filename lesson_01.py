# My First Class

class Point:
    "Class for representing points on a plane"
    color = 'red'
    circle = 2


a = Point()
b = Point()

Point.type = 'disc'

print(Point.__dict__)
print(a.__dict__)
print(b.__dict__)
print(b.__doc__)

a.color = 'green'
a.circle = 3
b.color = 'yellow'
b.circle = 4

print("class Point:", Point.color, Point.circle)
print("first instance:", a.color, a.circle)
print("second instance:", b.color, b.circle)
print(Point.__dict__)
print(a.__dict__)
print(b.__dict__)

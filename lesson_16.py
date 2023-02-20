# Object Hashes.
# Magic Methods: __eq__() and __hash__()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)

print(hash(p1), hash(p2), sep='\n')
print(hash(p1) == hash(p2))

# print(p1 == p2)

# Metaclasses (Dynamic Сlass Сreation)

class B1:
    pass


class B2:
    pass


def method1(self):
    print('method1:', self.__dict__)


# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100
A = type('Point', (), {'MIN_COORD': 0, 'MAX_COORD': 100})
point = A()
print(point.MIN_COORD, point.MAX_COORD)
print(point.__dict__)
del point, A

# class Point(B1, B2):
#     MIN_COORD = 0
#     MAX_COORD = 100
A = type('Point', (B1, B2), {'MIN_COORD': 0, 'MAX_COORD': 100})
point = A()
print(point.MIN_COORD, point.MAX_COORD)
print(point.__dict__)
print(A.__mro__)
del point, A


# class Point(B1, B2):
#     MIN_COORD = 0
#     MAX_COORD = 100

#     def method1(self):
#         print('method1:', self.__dict__)
A = type('Point', (B1, B2), {'MIN_COORD': 0,
         'MAX_COORD': 100, 'method1': method1})
point = A()
point.method1()
del point, A


# class Point(B1, B2):
#     MIN_COORD = 0
#     MAX_COORD = 100

#     lambda self: self.MAX_COORD
A = type('Point', (B1, B2), {'MAX_COORD': 100,
         'method1': lambda self: self.MAX_COORD})
point = A()
print(point.method1())
del point, A

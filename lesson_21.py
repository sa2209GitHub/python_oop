#
# 21
#
# Class Inheritance
# From Class object

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


class Integer(int):
    def __str__(self):
        return f"integer: {super().__str__()}"


class String(str):
    def __str__(self):
        return f"string: {super().__str__()}"


v = Vector([1, 2, 3, 4, 5])
print(v)

i = Integer(5)
print(i)

s = String('python 3')
print(s)

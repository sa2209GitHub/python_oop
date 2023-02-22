#
#   18
#
# Magic Methods:
# '__getitem__()', '__setitem__()', '__delitem__()'

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        print("__getitem__() method was called")
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("requested index out of range")

    def __setitem__(self, item, value):
        print("__setitem__() method was called")
        if not isinstance(item, int) or item < 0:
            raise TypeError("index shoud be a positive integer")
        if item >= len(self.marks):
            off = item + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[item] = value

    def __delitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("index shoud be a positive integer")
        del self.marks[item]


s = Student('John', [5, 5, 3, 2, 5])
print(s[2])
s[0] = 3
s[2] = 4
s[10] = 5
print(s.marks)
del s[0]
print(s.marks)

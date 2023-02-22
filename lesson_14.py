#
#   14
#
# Magic Methods of Arithmetic Operations:
# '__add__()', '__sub__()', '__mul__()', '__truediv__()'

class Integer:
    def __init__(self, number: int):
        if not isinstance(number, int):
            raise TypeError("number should be represented as an integer")
        self.__number = number
        self.__swap_operands = False

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Integer)):
            raise ArithmeticError(
                "right operand should be an integer or an instance of the Clock class")
        return other if isinstance(other, int) else other.__number

    def get_number(self):
        return self.__number

    def __add__(self, other):
        return Integer(self.__number + self.__verify_data(other))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.__number += self.__verify_data(other)
        return self

    def __sub__(self, other):
        if self.__swap_operands:
            self.__swap_operands = False
            return Integer(self.__verify_data(other) - self.__number)
        else:
            return Integer(self.__number - self.__verify_data(other))

    def __rsub__(self, other):
        self.__swap_operands = True
        return self - other

    def __isub__(self, other):
        self.__number -= self.__verify_data(other)
        return self

    def __mul__(self, other):
        return Integer(self.__number * self.__verify_data(other))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.__number *= self.__verify_data(other)
        return self

    def __floordiv__(self, other):
        if self.__swap_operands:
            self.__swap_operands = False
            return Integer(self.__verify_data(other) // self.__number)
        else:
            return Integer(self.__number // self.__verify_data(other))

    def __rfloordiv__(self, other):
        self.__swap_operands = True
        return self // other

    def __ifloordiv__(self, other):
        self.__number //= self.__verify_data(other)
        return self


class Clock:
    __DAY = 86400   # number of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("seconds should be represented as an integer")
        self.seconds = seconds % self.__DAY
        self.__swap_operands = False

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    def get_seconds(self):
        return self.seconds

    def get_minutes(self):
        return self.seconds / 60

    def get_hours(self):
        return self.seconds / 3600

    @ classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(
                "right operand should be an integer or an instance of the Clock class")
        return other if isinstance(other, int) else other.seconds

    @ classmethod
    def __get_formated(cls, n):
        return str(n).rjust(2, '0')

    def __add__(self, other):
        print("__add__() method was called")
        return Clock(self.seconds + self.__verify_data(other))

    def __radd__(self, other):
        print("__radd__() method was called")
        return self + other

    def __iadd__(self, other):
        print("__iadd__() method was called")
        self.seconds += self.__verify_data(other)
        return self

    def __sub__(self, other):
        print("__sub__() method was called")
        if self.__swap_operands:
            self.__swap_operands = False
            return Clock(self.__verify_data(other) - self.seconds)
        else:
            return Clock(self.seconds - self.__verify_data(other))

    def __rsub__(self, other):
        print("__rsub__() method was called")
        self.__swap_operands = True
        return self - other

    def __isub__(self, other):
        print("__isub__() method was called")
        self.seconds -= self.__verify_data(other)
        return self


# Integer

a = Integer(10)
b = Integer(20)

print(a.get_number(), b.get_number())

# __add__()
print("# __add__()")
a = a + 10
b = b + 10
print(a.get_number(), b.get_number())

# __radd__()
print("# __radd__()")
a = 10 + a
b = 10 + b
print(a.get_number(), b.get_number())

# __iadd__()
print("# __iadd__()")
a += 10
b += 10
print(a.get_number(), b.get_number())

# __add__()
print("# __add__()")
a = a + b
print(a.get_number(), b.get_number())
del a, b

a = Integer(100)
b = Integer(200)

print(a.get_number(), b.get_number())

# __sub__()
print("# __sub__()")
a = a - 10
b = b - 10
print(a.get_number(), b.get_number())

# __rsub__()
print("# __rsub__()")
a = 10 - 15 - a
b = 20 - 25 - b
print(a.get_number(), b.get_number())

# __isub__()
print("# __isub__()")
a -= 5
b -= 5
print(a.get_number(), b.get_number())
del a, b

a = Integer(100)
b = Integer(200)
print(a.get_number(), b.get_number())

# __mul__()
print("# __mul__()")
a = a * 2
b = b * 2
print(a.get_number(), b.get_number())

# __rmul__()
print("# __rmul__()")
a = 2 * a
b = 2 * b
print(a.get_number(), b.get_number())

# __imul__()
print("# __imul__()")
a *= 2
b *= 2
print(a.get_number(), b.get_number())
del a, b

a = Integer(800)
b = Integer(1600)
print(a.get_number(), b.get_number())

# __floordiv__()
print('__floordiv__()')
a = a // 2
b = b // 2
print(a.get_number(), b.get_number())

# __ifloordiv__()
print('__ifloordiv__()')
a //= 100
b //= 100
print(a.get_number(), b.get_number())

# __rfloordiv__()
print('__rfloordiv__()')
a = 400 // a
b = 800 // b
print(a.get_number(), b.get_number())
del a, b


# Clock

# __add__()
print("\n*** __add__() ***")
c = Clock(1000)
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
c = c + 100         # __add__()
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
c = 100 + c         # __radd__()
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
c += 100            # __iadd__()
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
del c

# __sub__()
print("\n*** __sub__() ***")
c = Clock(600)
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
c = c - 100         # __sub__()
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
c = 600 - c         # __rsub__()
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
c -= 100            # __isub__()
print(f"{c.get_time()}. hours: {round(c.get_hours(), 2)}, minutes: {round(c.get_minutes(), 2)}, seconds: {c.get_seconds()}")
del c

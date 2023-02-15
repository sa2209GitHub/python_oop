# Magic Methods of Arithmetic Operations:
# __add__(), __sub__(), __mul__(), __truedev__()

class Clock:
    __DAY = 86400   # number of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("seconds should be represented as an integer")

        self.seconds = seconds % self.__DAY

    def __add__(self, n):
        print("__add__() method was called")
        if not isinstance(n, (int, Clock)):
            raise ArithmeticError("right operand shoud be an integer or Clock")

        s = n
        if isinstance(n, Clock):
            s = n.seconds

        return Clock(self.seconds + s)

    def __radd__(self, n):
        print("__radd__() method was called")
        return self + n

    def __iadd__(self, n):
        print("__iadd__() method was called")
        if not isinstance(n, (int, Clock)):
            raise ArithmeticError("right operand shoud be an integer or Clock")

        s = n
        if isinstance(n, Clock):
            s = n.seconds

        self.seconds += s
        return self

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    @classmethod
    def __get_formated(cls, n):
        return str(n).rjust(2, "0")


c1 = Clock(1000)
c2 = Clock(2000)
print(c1.get_time())
print(c2.get_time())
c1 = c1 + 100
c2 = c2 + 200
c1 = 100 + c1
print(c1.get_time())
print(c2.get_time())
c3 = c1 + c2
print(c3.get_time())
c2 += 100

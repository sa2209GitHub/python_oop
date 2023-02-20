# Magic Methods of Comparisons:
# __eq__(), __ne__(), __lt__(),
# __le__(), __gt__(), __ge__()


class Clock:
    __DAY = 86400   # number of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("seconds should be represented as an integer")

        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError(
                "right operand must be an integer or an instance of the Clock class")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        print("__eq__() method was called")
        return self.seconds == self.__verify_data(other)

    def __lt__(self, other):
        print("__lt__() method was called")
        return self.seconds < self.__verify_data(other)

    def __le__(self, other):
        print("__le__() method was called")
        return self.seconds <= self.__verify_data(other)


c1 = Clock(1000)
c2 = Clock(1000)
c3 = Clock(2000)

# __eq__()
print(c1 == c2)
print(c2 == c3)
print(c3 == 2000)
print(c3 == 2002)
print(2000 == c3)
print(c3 != 1000)

# __lt__()
print(c1 < c3)
print(c3 > c1)

# __le__()
print(c1 <= c3)
print(c3 >= c1)

# Magic Methods of Comparisons:
# __eq__(), __ne__(), __lt__(),
# __le__(), __gt__(), __ge__()


class Clock:
    __DAY = 86400   # number of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("seconds should be represented as an integer")

        self.seconds = seconds % self.__DAY

    def __eq__(self, another):
        pass


c1 = Clock(1000)
c2 = Clock(1000)
print(c1 == c2)

# Magic Method '__call__()'.
# Functors and Decorator Classes

import math


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print(f"__call__ method was called. *args: {args}, **kwargs: {kwargs}")
        self.__counter += step
        return self.__counter


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        print(f"__call__ method was called. *args: {args}, **kwargs: {kwargs}")
        if not isinstance(args[0], str):
            raise TypeError("the argument should be a string")

        return args[0].strip(self.__chars)


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        print(f"__call__ method was called. *args: {args}, **kwargs: {kwargs}")

        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


counter = Counter()
print(counter.__dict__)
counter()
counter()
counter()
print(counter(3))
# -----------------
s1 = StripChars("?:!.; ")
result = s1(" Hello World!  ;")
print(result)
# -----------------
print(df_sin(math.pi / 3))
# df_sin = Derivate(df_sin)
# print(df_sin(math.pi / 3))

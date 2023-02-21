# Magic Methods:
# '__iter__()' and '__next__()'

class FloatRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step <= self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FloatRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.float_range = FloatRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.float_range)
        else:
            raise StopIteration


fr = FloatRange(start=0.0, stop=8.0, step=0.5)
print(fr.__dict__)
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
for item in fr:
    print(item)

fr_2d = FloatRange2D(start=0.0, stop=8.0, step=0.5, rows=2)
for row in fr_2d:
    for item in row:
        print(item, end=" ")
    print()

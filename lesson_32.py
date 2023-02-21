# 'with' Context Manager

# without 'with' context manager:
print("# without 'with' context manager:\n")
data_stream = None
try:
    data_stream = open("./myfile.txt")
    for text in data_stream:
        print(text)
except Exception as e:
    print(e)
finally:
    if data_stream is not None:
        data_stream.close()

# with 'with' context manager:
print("\n# with 'with' context manager:\n")
try:
    with open("myfile.txt") as data_stream:
        for text in data_stream:
            print(text)
except Exception as e:
    print(e)


# example 1
class DefenderVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False


v1 = [1, 2, 3]
v2 = [4, 5]

try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except Exception as e:
    print(e)

print(v1)

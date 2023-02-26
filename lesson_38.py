#
#   38
#
# Introduction to Data Classes. Part 2
#
# https://docs.python.org/3/library/dataclasses.html


import math
from dataclasses import dataclass, field, InitVar


# Regular class (Example 1)


class Vector3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        # self.length = (x * x + y * y + z * z) ** 0.5
        self.length = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))


v3d = Vector3D(10, 20, 30)
print(v3d.__dict__)
del v3d, Vector3D


# Regular class (Example 2)


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        # self.length = (x * x + y * y + z * z) ** 0.5
        self.length = math.sqrt(
            pow(x, 2) + pow(y, 2) + pow(z, 2)) if calc_len else 0


v3d = Vector3D(10, 20, 30)
print(v3d.__dict__)
del v3d, Vector3D


# Data class (Example 1)


@dataclass
class Vector3D:
    x: int
    y: int
    z: int
    length: float = field(init=False)

    def __post_init__(self):
        self.length = math.sqrt(
            pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))


v3d = Vector3D(10, 20, 30)
print(v3d.__dict__)
del v3d, Vector3D


# Data class (Example 2)


@dataclass
class Vector3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, compare=False)

    def __post_init__(self):
        self.length = math.sqrt(
            pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))


v3d = Vector3D(10, 20, 30)
v3d2 = Vector3D(10, 20, 50)
print(v3d.__dict__)
print(v3d2.__dict__)
print(v3d == v3d2)
del v3d, Vector3D


# Data class (Example 3)


@dataclass
class Vector3D:
    x: int
    y: int
    z: int
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = math.sqrt(
                pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))


v3d = Vector3D(10, 20, 30)
v3d2 = Vector3D(10, 20, 50, False)
print(v3d.__dict__)
print(v3d2.__dict__)
print(v3d, v3d2, sep='\n')
del v3d, Vector3D


# Data class parameters (Example 4)


@dataclass(repr=True, eq=True, order=True)
class Vector3D:
    x: int
    y: int
    z: int
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = math.sqrt(
                pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))


v3d = Vector3D(10, 20, 30)
v3d2 = Vector3D(10, 20, 30)
print(v3d.__dict__)
print(v3d2.__dict__)
print(v3d >= v3d2)
del v3d, Vector3D

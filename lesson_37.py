#
#   37
#
# Introduction to Data Classes. Part 1.


from dataclasses import dataclass, field
from pprint import pprint


# Regular class


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self) -> str:
        return f"Thing: {self.__dict__}"


t = Thing("Python Tutorial", 100, 1024)
print(t)
del t, Thing


# Data class


@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)

    # def __eq__(self, other):
    #     return self.weight == other.weight


td = ThingData("Python Tutorial", 100, 1024)
td.dims.append(10)
td2 = ThingData("Python OOP", 80, 512)
td3 = ThingData("Python OOP", 80, 512)
# td3.dims.append(12)

print(td)
print(td2)
print(td3)
# pprint(ThingData.__dict__)

print(td == td2)
print(td2 == td3)

del td, ThingData

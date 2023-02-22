# Introduction to Data Classes


from dataclasses import dataclass
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


td = ThingData("Python Tutorial", 100, 1024)
print(td)
pprint(ThingData.__dict__)
del td, ThingData

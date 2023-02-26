#
#   39
#
# Using Data Classes in Inheritance
# and 'make_dataclass()' Method
#
# https://docs.python.org/3/library/dataclasses.html


# Example 1


from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: __post_init__() method was called")
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        super().__post_init__()
        print("Book: __post_init() method was called")


b = Book()
b2 = Book(1000, 100, "Pythop OOP", "Programmer Joe")
b3 = Book(1024, 128, "Just Book", "Just Name")
b4 = Book(1024, 128, "Just Book", "Just Name", [210, 297, 5])

print(b)
print(b2)
print(b3)
print(b4)


# Example 2 ('make_dataclass()' method)


class Car:
    def __init__(self, brand: str, model: str, year_of_issue: int, max_speed: int, engine_hp: int, price: int):
        self.brand = brand
        self.model = model
        self.year_of_issue = year_of_issue
        self.max_speed = max_speed
        self.engine_hp = engine_hp
        self.price = price

    def get_info(self):
        return {
            'brand': self.brand,
            'model': self.model,
            'year_of_issue': self.year_of_issue,
            'max_speed': self.max_speed,
            'engine_hp': self.engine_hp,
            'price': self.price}


car = Car(brand='Toyota', model='Camry', year_of_issue=2021,
          max_speed=210, engine_hp=180, price=12000)
print(car.get_info())
del car, Car


# Same class using 'make_dataclass()' method


Car = make_dataclass("Car", [('brand', str),
                             ('model', str),
                             ('year_of_issue', int),
                             ('max_speed', int),
                             ('engine_hp', int),
                             ('price', int, field(default=0))
                             ],
                     namespace={'get_info': lambda self: {
                         'brand': self.brand,
                         'model': self.model,
                         'year_of_issue': self.year_of_issue,
                         'max_speed': self.max_speed,
                         'engine_hp': self.engine_hp,
                         'price': self.price
                     }
})


car = Car(brand='BMW', model='X6', year_of_issue=2022,
          max_speed=250, engine_hp=280, price=99000)
print(car.get_info())
del car, Car

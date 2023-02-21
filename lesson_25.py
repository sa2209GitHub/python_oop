# Multiple Inheritance

import datetime


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("Init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def get_info(self):
        return {'name': self.name, 'weight': self.weight, 'price': self.price}


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print(f"Init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def write_sell_log(self):
        print(f"log {self.id}: the item was sold at {datetime.datetime.now()}")

    def get_info(self):
        print("MixinLog info")


class Notebook(Goods, MixinLog):
    # Overriding a base class method as needed
    # def get_info(self):
    #     MixinLog.get_info(self)

    pass


class SSD:
    pass


class CPU:
    pass


class GPU:
    pass


n = Notebook("Apple", 1.3, 120988)
print(n.get_info())
# MixinLog.get_info(n)
n.write_sell_log()
print(Notebook.__mro__)

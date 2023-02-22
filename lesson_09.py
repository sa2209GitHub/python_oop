#
# 9
#
# Getting To Know The '@property' Object

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


p1 = Person('Noah', 20)
print(p1.__dict__)
# # p1.set_age(35)
p1.age = 35
p1.name = 'John'
# print(p1.get_age())
print(p1.name, p1.age, p1.__dict__)
del p1.age
print(p1.__dict__)

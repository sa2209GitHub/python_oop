# '@property' Object Example

from string import ascii_letters


class Person:
    RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    RUS_UPPER = RUS.upper()

    def __init__(self, full_name, age, passport, weight):
        self.full_name = full_name
        self.age = age
        self.passport = passport
        self.weight = weight

    @classmethod
    def verify_full_name(cls, full_name):
        print(f"full_name: {full_name}")
        if type(full_name) != str:
            raise TypeError("full name should be a string")

        processed_name = full_name.split()
        if len(processed_name) != 3:
            raise TypeError("invalid full name format")

        letters = ascii_letters + cls.RUS + cls.RUS_UPPER
        for part in processed_name:
            if len(part) < 1:
                raise TypeError(
                    "the full name part should contain at least one character")
            if len(part.strip(letters)) != 0:
                raise TypeError(
                    "full name should contain only valid characters")

    @classmethod
    def verify_age(cls, age):
        print(f"age: {age}")
        if type(age) != int or age < 14 or age > 120:
            raise TypeError("age should be an integer from 0 to 120")

    @classmethod
    def verify_passport(cls, passport):
        print(f"passport: {passport}")
        if type(passport) != str:
            raise TypeError("passport series should be a string")

        processed_passport = passport.split()
        if len(processed_passport) != 2 or len(processed_passport[0]) != 4 or len(processed_passport[1]) != 6:
            raise TypeError("invalid passport series format")

        for part in processed_passport:
            if not part.isdigit():
                raise TypeError("passport series should contain only numbers")

    @classmethod
    def verify_weight(cls, weight):
        print(f"weight: {weight}")

        if type(weight) == str:
            try:
                weight = float(weight)
            except:
                raise TypeError("wrong weight format")

        if type(weight) == int:
            weight = float(weight)

        if type(weight) != float or weight < 20:
            raise TypeError("weight should be a real number of 20 or more")

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.verify_full_name(full_name)
        self.__full_name = full_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p = Person(full_name="Иванов Милаил Николаевич",
           passport='1234 567890', age=30, weight=80)

# print(p.full_name, p.passport, p.age, p.weight)
print(p.__dict__)

p.full_name = "Иванова Татьяна Игоревна"
p.passport = '9876 543210'
p.age = 33
p.weight = 52

# print(p.full_name, p.passport, p.age, p.weight)
print(p.__dict__)

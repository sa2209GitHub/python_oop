# Magic Method __new__()

class Point:
    def __new__(cls, *args, **kwargs):
        print("__new__() method was called", str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("__init__() method was called", str(self))
        self.x = x
        self.y = y


pt1 = Point(1, 2)
print(pt1.__dict__)


# Singleton Example

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, password, port) -> None:
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(
            f"database connection: {self.user}, {self.password}, {self.port}")

    def close(self):
        print("close database connection")

    def read(self):
        return 'DATA'

    def write(self, data):
        print(f"writing to the database: {data}")


db1 = DataBase('root', '12345', 4430)
db2 = DataBase('user', 'password', 5555)
print(db1.__dict__)
print(db2.__dict__)
db1.connect()
db2.connect()

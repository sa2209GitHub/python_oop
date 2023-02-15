# Monostate Pattern

class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
th3 = ThreadData()

print(th1.__dict__)
print(th2.__dict__)
print(th3.__dict__)

th1.attr = 'new_attr'
th2.id = 3

print(th1.__dict__)
print(th2.__dict__)
print(th3.__dict__)

class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    def set_bound1(self, left):  # не меняет атрибут класса MAX_COORD
        self.MAX_COORD = left  # создаст атрибут в обьекте

    @classmethod
    def set_bound(cls, left):  # меняет атрибут в классе
        cls.MAX_COORD = left

    # def __getattribute__(self, item):
    #     print('__getattrubute__')
    #     return object.__getattribute__(self, item)

    def __getattribute__(self, item): # Вызывается при обращении к атрибуту класса
        print('__getattrubute__')
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value): # Вызавается при установке значения атрибута
        print('__setattr')
        if key == 'z':
            raise AttributeError('Недопустимое значение')
        else:
            object.__setattr__(self, key, value)
            # self.x =value # recursion
            # self.__dict__[key] = value

    def __getattr__(self, item): #Вызывается при отсутсвие атрибута к которому пытаются обратиться
        print('__getattr__: ' + item)
        return False
    def __delattr__(self, item): # Вызывается при удалении даже если удалять нечего
        print('__delattr__')
        object.__delattr__(self, item)


pt = Point(2, 3)
a = pt.c
# pt.z = 123
del pt.x
print(pt.__dict__)
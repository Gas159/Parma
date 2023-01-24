class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        print(self.__coords)
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -12)
print(p.__dict__)
print(len(p))
print(abs(p))

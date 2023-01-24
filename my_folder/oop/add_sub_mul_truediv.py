class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Sek must be interger')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other): # + !!
        # print(self, self.__class__, __class__,  sep='\n')
        if not isinstance(other, (int, self.__class__)):
            raise ArithmeticError('must be int or Clock')
        if isinstance(other, self.__class__):
            other = other.seconds
        return self.__class__(self.seconds + other)

    def __radd__(self, other): # chager place
        return self + other

    def __iadd__(self, other): # +=
        print('__iadd__')
        if not isinstance(other, (int, __class__)):
            raise ArithmeticError('Must be int')
        if isinstance(other, self.__class__):
            other = other.seconds
            self.seconds + other
        return self


c1 = Clock(1125)
c2 = Clock(2222)
c3 = Clock(3333)
c4 = 222 + c1 + 100 + c2 + c3 + 123
print(c4.get_time())
print(id(c1))
c1 += 100
print(id(c1))
# print(c1.get_time())
# c1.seconds = c1.seconds  + 100
# print(c1.get_time())
# c1 = c1 + 100
# print(c1.get_time())
# print(c1.__class__)

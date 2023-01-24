class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.y = y
        else:
            raise ValueError('Координаты должны быть числами')
    # @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int,float)

    def set_coord(self, x, y):
        # if type(x) in (int, float) and type(y) in (int, float):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.y


pt = Point(1, 2)
pt.set_coord(2, 22)
print(pt.get_coord())
print(dir(pt))
print(pt._Point__x)
Point.__check_value
pt.__check_value

# print(pt.__x)
# print(pt.__x, pt.y)
# pt.x = 123
# pt.y = 'fdsa'
# print(pt.__x, pt.y)

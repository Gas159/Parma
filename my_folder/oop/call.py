# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs): # функтор
#         print('__call__')
#         print(args)
#         if not isinstance(args[0], str):
#             raise TypeError('Аргумент должен быть строкой ')
#         # self.__counter += step
#         # return self.__counter
#         return args[0].strip(self.__chars)
#
# s1 = StripChars('!@#$%^&*",Ю!"№;%:?')
# print(s1.__dict__)
# res = s1('Hello wolrd&@!')
# print(res)
import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs): # функтор
        print('__call__')
        return (self.__fn(x +dx) - self.__fn(x)) / dx
@Derivate # тоже самое что и df_sin = Derivate(df_sin)
def df_sin(x):
    return math.sin(x)

# print(df_sin(math.pi/3))
# df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))
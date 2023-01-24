from string import ascii_letters


class Person:
    S_RUS = 'абвгдежзийкомнлопрстуфчцхшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weigth):
        self.verify_fio(fio)
        # self.verify_old(old) # это тоже можно убрать
        # self.verify_weigth(weigth)
        # self.verify_ps(ps)

        self.__fir = fio.split()
        # self.__old = old
        # self.__passport = ps
        # self.__weigth = weigth # setter проверяет присвоение
        self.old = old
        self.passport = ps
        self.weigth = weigth

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('FIO must be string')
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('must be greater than one!')
            if len(s.strip(letters)) != 0:
                for i in s:
                    if i not in letters:
                        # print(i)
                        raise TypeError(f'В ФИО можно юзать только буквы и дефис {i}')

    @classmethod
    def verify_old(cls, old):
        if not isinstance(old, int) or old < 14 or old > 120:
             raise TypeError('возраст должен быть целым числом в диапазоне [14 - 120]')

    @classmethod
    def verify_weigth(cls, w):
        if type(w) not in (int, float) or w < 20:
            raise TypeError("Вес должеть быть вещественным числом от 20 и выше.")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('PS not Stirng!')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) !=6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и норме паспорта должны быть целыми числами')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.__fio = fio

    @fio.deleter
    def fio(self):
        del self.__fio


    @property
    def old (self):
        return self.__old
    
    @old.setter
    def old (self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weigth(self):
        return self.__weigth

    @weigth.setter
    def weigth(self, weigth):
        self.verify_weigth(weigth)
        self.__weigth = weigth

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps


p = Person('Сахапов Ринат Ильдарович', 20, '1234 454343', 80.0)
print(p.__dict__)
p.old = 100
p.passport = '3454 232323'
p.weigth = 44
print(p.__dict__)

# @property
# def old(self):
#     return self.__old
#
# @old.setter
# def old(self, old):
#     self.__old = old
#
# @old.deleter
# def old(self):
#     del self.__old

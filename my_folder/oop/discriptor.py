class ReadIntx: # non Data Descriptor
    def __set_name__(self, owner, name):
        self.name = '_x'
    def __get__(self, instance, owner):
        return getattr(instance, self.name )

    # def __set__(self, instance, value):  # instance экземпляр класса Point3D
    #     print(f'__set__: {self.name} = {value}') # превратит его в Дескриптор данных
    #     setattr(instance, self.name, value)


class Interger: # Дескрипиов данных, высокий приоритет
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('coord not interger')
    def __set_name__(self, owner, name): #owner class Point3d
        self.name = '_' + name
    def __get__(self, instance, owner):
        # return instance.__dict__[self.name] or
        return getattr(instance,self.name)

    def __set__(self, instance, value): # instance экземпляр класса Point3D
        print(f'__set__: {self.name} = {value}')
        self.verify_coord(value)
        # instance.__dict__[self.name] = value # or
        setattr(instance, self.name, value)
class Point3d:

    x = Interger()
    z = Interger()
    y = Interger()
    xr = ReadIntx()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # @classmethod
    # def verify_coord(cls, coord):
    #     if type(coord) != int:
    #         raise TypeError('coord not interger')



    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, coord):
    #     self.verify_coord(coord)
    #     self._x = coord
    #
    # #
    # @property
    # def y(self):
    #     return self._y
    #
    # @y.setter
    # def y(self, coord):
    #     self.verify_coord(coord)
    #     self._y = coord
    #
    # @property
    # def z(self):
    #     return self._z
    #
    # @z.setter
    # def z(self, coord):
    #     self.verify_coord(coord)
    #     self._z = coord


p = Point3d(1, 2, 3)
print(p.xr, p.__dict__)
p.x = 123
p.__dict__['xr'] = 5
print(p.xr, p.__dict__)
print(p.__dir__())

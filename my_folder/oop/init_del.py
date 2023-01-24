class Point:
    '''Class for view coord'''
    color ='red'
    cirlce = 2

    def __init__(self, x, y=0):
        print('Вызов __init__')
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра; " + str(self))
    def set_coords(self, x, y):
        print('Вызов метода сет_коордс ' + str(self))
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt=Point(1)
print(pt.__dict__)
pt = Point(1)
print(pt)

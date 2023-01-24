class Point:
    '''Class for view coord'''
    color ='red'
    cirlce = 2

    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ ', str(cls))
        return super().__new__(cls)

    def __init__(self, x, y=0):
        print('Вызов __init__ ' + str(self))
        self.x = x
        self.y = y

pt = Point(1,2)
print(pt)
class Point:
    '''Class for view coord'''
    color ='red'
    cirlce = 2

    def set_coords(self, x, y):
        print('Вызов метода сет_коордс ' + str(self))
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt=Point()

pt.set_coords(1,2) # or Point.set_coords(pt)
print(pt.__dict__)

print(pt.get_coords())

f = getattr(pt, 'get_coords')
print(f)
print(f())
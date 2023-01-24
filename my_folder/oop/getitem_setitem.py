class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('index out of range!!!')

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('must be int')
        # if 0 <= key < len(self.marks):
        #     self.marks[key] = value
        if key >= len(self.marks):
            off =  key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('must be int')
        del self.marks[key]

s1 = Student('sergey', [1,2,3])
s1[22] = 4
print(s1.marks[1])
print(s1[2])
del s1[2]
print(s1.marks)


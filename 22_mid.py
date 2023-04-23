class A:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    def __str__(self):
        return self._x

class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.__y = y

    def change(self, other):
        self._x = other.x

    def __str__(self):
        return f'{super().__str__()}, {self.__y}'

if __name__ == '__main__':
    a, b = A(1), B(10, 100)
    b.change(a)
    print(b)
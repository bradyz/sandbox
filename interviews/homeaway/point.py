class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return str((self._x, self._y))


class Line:
    def __init__(self, p1=Point(), p2=Point()):
        self._p1 = p1
        self._p2 = p2

    def __str__(self):
        return str(self._p1) + " " + str(self._p2)

if __name__ == "__main__":
    a = Point(0, 0)
    b = Point(1, 1)
    c = Line(a, b)
    print(c)

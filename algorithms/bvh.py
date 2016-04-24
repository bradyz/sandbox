from random import randrange
from matplotlib import pyplot as plt


N = 3
B = 10


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        plt.plot(self.x, self.y, "ro")


class Triangle:
    def __init__(self, v0, v1, v2):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

        minx = min((v0, v1, v2), key=lambda x: x.x)
        miny = min((v0, v1, v2), key=lambda x: x.y)
        maxx = max((v0, v1, v2), key=lambda x: x.x)
        maxy = max((v0, v1, v2), key=lambda x: x.y)

        self.box = Box(minx, miny, maxx, maxy)

    def area(self):
        a = self.v0.x * (self.v1.y - self.v2.y)
        b = self.v1.x * (self.v2.y - self.v0.y)
        c = self.v2.x * (self.v0.y - self.v1.y)
        return abs((a + b + c) / 2)

    def draw(self):
        plt.plot([self.v0.x, self.v1.x], [self.v0.y, self.v1.y], "r-")
        plt.plot([self.v1.x, self.v2.x], [self.v1.y, self.v2.y], "r-")
        plt.plot([self.v2.x, self.v0.x], [self.v2.y, self.v0.y], "r-")


class Box:
    def __init__(self, minx=1e9, miny=1e9, maxx=-1e9, maxy=-1e9):
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.empty = (minx != 1e9)

    def merge(self, box):
        if box.empty:
            return
        self.empty = False
        self.minx = min(self.minx, box.minx)
        self.miny = min(self.miny, box.miny)
        self.maxx = min(self.maxx, box.maxx)
        self.maxy = min(self.maxy, box.maxy)


class Node:
    def __init__(self, objects):
        self.objects = objects
        self.box = Box()


if __name__ == "__main__":
    objects = list()

    while len(objects) < N:
        verts = (Point(randrange(B), randrange(B)) for _ in range(3))
        tmp = Triangle(*verts)
        if tmp.area() <= 5 and tmp.area() > 0:
            objects.append(tmp)

    plt.ylim(0, B)
    plt.xlim(0, B)

    for obj in objects:
        obj.draw()

    plt.show()

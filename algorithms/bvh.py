from random import randrange
from matplotlib import pyplot as plt


EPS = 10
N = 8
B = 1000


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        plt.plot(self.x, self.y, "ro")

    def __add__(self, b):
        return Point(self.x + b.x, self.y + b.y)

    def __truediv__(self, b):
        return Point(self.x / b, self.y / b)

    def __str__(self):
        return str(self.x) + " " + str(self.y)


class Triangle:
    def __init__(self, v0, v1, v2):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

        minx = min(map(lambda x: x.x, (v0, v1, v2)))
        miny = min(map(lambda x: x.y, (v0, v1, v2)))
        maxx = max(map(lambda x: x.x, (v0, v1, v2)))
        maxy = max(map(lambda x: x.y, (v0, v1, v2)))

        self.box = Box(minx, miny, maxx, maxy)

    def area(self):
        a = self.v0.x * (self.v1.y - self.v2.y)
        b = self.v1.x * (self.v2.y - self.v0.y)
        c = self.v2.x * (self.v0.y - self.v1.y)
        return abs((a + b + c) / 2)

    def centroid(self):
        return (self.v0 + self.v1 + self.v2) / 3

    def draw(self):
        plt.plot([self.v0.x, self.v1.x], [self.v0.y, self.v1.y], "c-")
        plt.plot([self.v1.x, self.v2.x], [self.v1.y, self.v2.y], "c-")
        plt.plot([self.v2.x, self.v0.x], [self.v2.y, self.v0.y], "c-")

    def __str__(self):
        return "v0: " + str(self.v0) + " v1: " + str(self.v1) + \
            " v2: " + str(self.v2)


class Box:
    def __init__(self, minx=1e9, miny=1e9, maxx=-1e9, maxy=-1e9):
        self.minx = minx - EPS
        self.miny = miny - EPS
        self.maxx = maxx + EPS
        self.maxy = maxy + EPS
        self.empty = (minx == 1e9)

    def merge(self, box):
        if box.empty:
            return
        self.empty = False
        self.minx = min(self.minx, box.minx)
        self.miny = min(self.miny, box.miny)
        self.maxx = max(self.maxx, box.maxx)
        self.maxy = max(self.maxy, box.maxy)

    def draw(self, color="b-"):
        plt.plot([self.minx, self.minx], [self.miny, self.maxy], color)
        plt.plot([self.minx, self.maxx], [self.miny, self.miny], color)
        plt.plot([self.maxx, self.maxx], [self.miny, self.maxy], color)
        plt.plot([self.minx, self.maxx], [self.maxy, self.maxy], color)

    def __str__(self):
        return "minx: " + str(self.minx) + " miny: " + str(self.miny) + \
            " maxx: " + str(self.maxx) + " maxy: " + str(self.maxy)


class Node:
    def __init__(self, objects, root=False):
        self.objects = objects
        self.box = Box()
        self.left = None
        self.right = None
        self.root = root

        if not self.objects:
            return

        for obj in self.objects:
            self.box.merge(obj.box)

        print(self.box)

        centroids = [(obj.centroid(), obj) for obj in self.objects]

        minx = min(cent.x for cent, obj in centroids)
        maxx = max(cent.x for cent, obj in centroids)

        miny = min(cent.y for cent, obj in centroids)
        maxy = max(cent.y for cent, obj in centroids)

        if (maxy - miny) > (maxx - minx):
            centroids.sort(key=lambda x: x[0].y)
        else:
            centroids.sort(key=lambda x: x[0].x)

        left = centroids[:len(centroids) // 2]
        right = centroids[len(centroids) // 2:]

        if left and right:
            self.left = Node([x[1] for x in left])
            self.right = Node([x[1] for x in right])

    def draw(self):
        if self.root and not self.box.empty:
            self.box.draw("k--")

        if self.left and not self.left.box.empty:
            self.left.box.draw("r-")
            self.left.draw()

        if self.right and not self.right.box.empty:
            self.right.draw()
            self.right.box.draw("b-")


if __name__ == "__main__":
    objects = list()

    while len(objects) < N:
        seed = Point(randrange(B), randrange(B))
        verts = (seed + Point(randrange(B / 10), randrange(B / 10))
                 for _ in range(3))
        tmp = Triangle(*verts)
        if tmp.area() > 5:
            objects.append(tmp)

    bvh = Node(objects, root=True)

    plt.ylim(0, B + B / 10)
    plt.xlim(0, B + B / 10)

    for obj in objects:
        obj.draw()

    bvh.draw()

    plt.savefig("bvh.png")
    plt.show()

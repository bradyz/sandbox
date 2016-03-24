from math import sqrt

from random import randrange

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


eye = np.array([0, 0, 0])
look = np.array([0, 0, 1])
up = np.array([0, 1, 0])


class Ray:
    def __init__(self, origin, vector):
        self.origin = np.array(origin)
        self.vector = np.array(vector)
        self.vector = self.vector / np.linalg.norm(self.vector)

    def __str__(self):
        return "o: " + str(self.origin) + " v: " + str(self.vector)


class Sphere:
    def __init__(self, origin, radius):
        self.origin = np.array(origin)
        self.radius = radius

    def __str__(self):
        return "s: " + str(self.origin) + " r: " + str(self.radius)


# r == dist(o + vt, c)
# d_x = o_x + v_x * t - c_x
# d_y = o_y + v_y * t - c_y
# d_z = o_z + v_x * t - c_z
# r == sqrt(d_x ** 2 + d_y ** 2 + d_z ** 2)
# r ** 2 == d_x ** 2 + d_y ** 2 + d_z ** 2
# 0 == d_x ** 2 + d_y ** 2 + d_z ** 2 - r ** 2
# d_i ** 2 = ((o_i - c_i) + v_i * t)
# d_i ** 2 = (o_i - c_i) ** 2 + 2 * (o_i - c_i) * (v_i * t) + (v_i * t) ** 2
# d_i ** 2 = (v_i ** 2) * t ** 2 +
#            (2 * o_i * v_i - 2 * c_i * v_i) * t +
#            (o_i - c_i) ** 2
def ray_sphere_intersect(ray, sphere):
    o = ray.origin
    v = ray.vector
    r = sphere.radius
    s = sphere.origin
    a = 0
    b = 0
    c = -(r ** 2)
    for v_i, o_i, s_i in zip(v, o, s):
        a += v_i ** 2
        b += (2 * o_i * v_i - 2 * s_i * v_i)
        c += (o_i - s_i) ** 2
    if b ** 2 - 4 * a * c <= 0:
        return None
    x_p = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x_m = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x = None
    if x_m > 0:
        x = x_m
    if x_p > 0 and (x is None or x_p < x):
        x = x_p
    return x


def process():
    intersections = list()

    for ray in rays:
        min_time = None
        for sphere in spheres:
            time = ray_sphere_intersect(ray, sphere)
            if time is not None:
                intersections.append(ray.origin + time * ray.vector)
            if time is not None and (min_time is None or time < min_time):
                min_time = time
        if min_time is not None:
            # intersections.append(ray.origin + min_time * ray.vector)
            print(ray)
            print(ray.origin + min_time * ray.vector)

    setup_plot(rays, spheres, intersections)


def setup_plot(rays, spheres, intersections):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(-10, 10)

    for ray in rays:
        o = ray.origin
        p = ray.origin + 20 * ray.vector
        ax.plot([o[0], p[0]], [o[1], p[1]], [o[2], p[2]], "r-")
        ax.scatter(o[0], o[1], o[2])

    for sphere in spheres:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        r = sphere.radius
        o = sphere.origin

        x = np.linspace(o[0], o[0], 100) + r * np.outer(np.cos(u), np.sin(v))
        y = np.linspace(o[1], o[1], 100) + r * np.outer(np.sin(u), np.sin(v))
        z = np.linspace(o[2], o[2], 100) +r * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, rstride=4, cstride=4, alpha=0.05)

    for intersect in intersections:
        o = intersect
        ax.scatter(o[0], o[1], o[2], c="y")

    plt.show()


if __name__ == "__main__":
    rays = list()
    spheres = list()

    num_rays = int(input())
    for _ in range(num_rays):
        a, b, c, x, y, z = map(int, input().split())
        rays.append(Ray((a, b, c), (x, y, z)))

    num_spheres = int(input())
    for _ in range(num_spheres):
        x, y, z, radius = map(int, input().split())
        spheres.append(Sphere((x, y, z), radius))

    for _ in range(3):
        x, y, z = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        radius = randrange(1, 5)
        spheres.append(Sphere((x, y, z), radius))

    for _ in range(10):
        a, b, c = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        x, y, z = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        rays.append(Ray((a, b, c), (x, y, z)))

    process()

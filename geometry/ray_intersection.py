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
        self.vector /= np.linalg.norm(self.vector)

    def __str__(self):
        return "ray: o: " + str(self.origin) + " v: " + str(self.vector)


class Sphere:
    def __init__(self, origin, radius):
        self.origin = np.array(origin)
        self.radius = radius

    def __str__(self):
        return "sphere: s: " + str(self.origin) + " r: " + str(self.radius)


class Plane:
    def __init__(self, origin, vector):
        self.origin = np.array(origin)
        self.vector = np.array(vector)
        self.vector /= np.linalg.norm(self.vector)

    def __str__(self):
        return "plane o: " + str(self.origin) + " v: " + str(self.vector)


class Triangle:
    def __init__(self, v1, v2, v3):
        self.points = np.array([v1, v2, v3])

    def __str__(self):
        return "v1: " + str(self.points[0]) + \
               "v2: " + str(self.points[1]) + \
               "v3: " + str(self.points[2])


# r == dist(o + vt, c)
# d_i = o_i + v_i * t - c_i
# r == sqrt(d_x ^ 2 + d_y ^ 2 + d_z ^ 2)
# r ^ 2 == d_x ^ 2 + d_y ^ 2 + d_z ^ 2
# 0 == d_x ^ 2 + d_y ^ 2 + d_z ^ 2 - r ^ 2
# d_i ^ 2 = ((o_i - c_i) + v_i * t)
# d_i ^ 2 = (o_i - c_i) ^ 2 + 2 * (o_i - c_i) * (v_i * t) + (v_i * t) ^ 2
# d_i ^ 2 = (v_i ^ 2) * t ^ 2 +
#           (2 * (o_i - c_i) * v_i) * t +
#           (o_i - c_i) ^ 2
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
        b += 2 * (o_i - s_i) * v_i
        c += (o_i - s_i) ** 2
    if b ** 2 - 4 * a * c <= 0:
        return None
    x_p = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x_m = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if min(x_p, x_m) < 0 and max(x_p, x_m) > 0:
        return None
    elif x_p < 0 and x_m < 0:
        return None
    return min(x_p, x_m)


# 0 == dot((o + vt) - p_o, p_n)
# 0 == dot((o - p_o) + v_t, p_n)
# 0 == sum((o_i - p_o) * (p_n_i) + v_i * (p_n_i) * t)
def ray_triangle_intersect(ray, triangle):
    v1, v2, v3 = triangle.points
    o = ray.origin
    v = ray.vector
    p = v1
    n = np.cross(np.array([v1, v2], [v1, v3]))
    n /= np.linalg.norm(n)
    s = 0
    c = 0
    for o_i, v_i, p_i, n_i in zip(o, v, p, n):
        s += (o_i - p_i) * (n_i)
        c += v_i * (n_i)
    intersect = (-s) / c
    return None


def ray_plane_intersect(ray, plane):
    o = ray.origin
    v = ray.vector
    p = plane.origin
    n = plane.vector
    s = 0
    c = 0
    for o_i, v_i, p_i, n_i in zip(o, v, p, n):
        s += (o_i - p_i) * (n_i)
        c += v_i * (n_i)
    if abs(c - 0) < 1e-5:
        print("parallel lines")
        print(ray)
        print(plane)
        return None
    intersect = (-s) / c
    if intersect <= 0:
        return None
    return intersect


def process():
    intersections = list()
    hit_rays = set()
    hit_spheres = set()

    for ray in rays:
        min_time = None
        for sphere in spheres:
            time = ray_sphere_intersect(ray, sphere)
            if time is not None and (min_time is None or time < min_time):
                min_time = time
            if time is not None:
                intersections.append(ray.origin + time * ray.vector)
                hit_rays.add(ray)
                hit_spheres.add(sphere)
        for plane in planes:
            time = ray_plane_intersect(ray, plane)
            if time is not None and (min_time is None or time < min_time):
                min_time = time
            if time is not None:
                intersect = ray.origin + time * ray.vector
                if intersect[0] <= 10 and intersect[0] >= -10 and \
                   intersect[1] <= 10 and intersect[1] >= -10 and \
                   intersect[2] <= 10 and intersect[2] >= -10:
                    intersections.append(intersect)
                    print(intersect)
                    hit_rays.add(ray)

    setup_plot(hit_rays, hit_spheres, intersections)
    # setup_plot(rays, spheres, intersections)


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
        z = np.linspace(o[2], o[2], 100) + \
            r * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, rstride=4, cstride=4, alpha=0.05)

    # for triangle in triangles:
    #     x = [c[0] for c in triangle.points]
    #     y = [c[1] for c in triangle.points]
    #     z = [c[2] for c in triangle.points]
    #     ax.plot_trisurf(x, y, z)

    for intersect in intersections:
        o = intersect
        ax.scatter(o[0], o[1], o[2], c="y")

    for plane in planes:
        p = plane.origin
        n = plane.vector
        xx, yy, zz = None, None, None
        if abs(n[0] - 0) > 1e-5:
            yy = np.arange(-15, 15, 1)
            zz = np.arange(-15, 15, 1)
            xx, yy = np.meshgrid(xx, yy)
            xx = (np.dot(p, n) - n[1] * yy - n[2] * zz) / n[0]
        elif abs(n[1] - 0) > 1e-5:
            xx = np.arange(-15, 15, 1)
            zz = np.arange(-15, 15, 1)
            xx, zz = np.meshgrid(xx, zz)
            yy = (np.dot(p, n) - n[0] * xx - n[2] * zz) / n[1]
        elif abs(n[2] - 0) > 1e-5:
            xx = np.arange(-15, 15, 1)
            yy = np.arange(-15, 15, 1)
            xx, yy = np.meshgrid(xx, yy)
            zz = (np.dot(p, n) - n[0] * xx - n[1] * yy) / n[2]
        else:
            raise ValueError("plane has zero vector normal")
        ax.plot_surface(xx, yy, zz, alpha=0.1)

    plt.show()


if __name__ == "__main__":
    rays = list()
    spheres = list()
    triangles = list()
    planes = list()

    num_rays = int(input())
    for _ in range(num_rays):
        a, b, c, x, y, z = map(float, input().split())
        rays.append(Ray((a, b, c), (x, y, z)))

    num_spheres = int(input())
    for _ in range(num_spheres):
        x, y, z, radius = map(float, input().split())
        spheres.append(Sphere((x, y, z), radius))

    num_triangles = int(input())
    for _ in range(num_triangles):
        x1, x2, x3, y1, y2, y3, z1, z2, z3 = map(float, input().split())
        v1 = np.array([x1, x2, x3])
        v2 = np.array([y1, y2, y3])
        v3 = np.array([z1, z2, z3])
        triangles.append(Triangle(v1, v2, v3))

    num_planes = int(input())
    for _ in range(num_planes):
        a, b, c, x, y, z = map(float, input().split())
        planes.append(Plane((a, b, c), (x, y, z)))

    for _ in range(3):
        x, y, z = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        radius = randrange(1, 5)
        spheres.append(Sphere((x, y, z), radius))

    for _ in range(10):
        a, b, c = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        x, y, z = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        x, y, z = float(x), float(y), float(z)
        rays.append(Ray((a, b, c), (x, y, z)))

    process()

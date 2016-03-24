import numpy as np
from math import sqrt


eye = np.array([0, 0, 0])
look = np.array([0, 0, 1])
up = np.array([0, 1, 0])


class Ray:
    def __init__(self, origin, vector):
        self.origin = np.array(origin)
        self.vector = np.array(vector)

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
    if x_p > 0 and x_p < x:
        x = x_p
    return x


def process():
    for ray in rays:
        min_time = None
        for sphere in spheres:
            time = ray_sphere_intersect(ray, sphere)
            if time is not None and (min_time is None or time < min_time):
                min_time = time
        if min_time is not None:
            print(ray)
            print(ray.origin + min_time * ray.vector)

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

    process()

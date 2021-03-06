from math import sqrt


def go_to(p, v, t):
    return tuple(p_i + t * v_i for p_i, v_i in zip(p, v))


def minus(x, y):
    return tuple(x_i - y_i for x_i, y_i in zip(x, y))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])

def dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


def norm_sq(x):
    return sum(y ** 2 for y in x)


ORIGIN = (0, 0, 0)

x_vel = tuple(map(float, input().split()))
y_vel = tuple(map(float, input().split()))
t = float(input())

y_t = go_to(ORIGIN, y_vel, t)
x_t = go_to(ORIGIN, x_vel, t)

a = norm_sq(x_vel) - norm_sq(y_vel)
b = 2 * dot(minus(x_t, y_t), y_vel)
c = -norm_sq(minus(x_t, y_t))

t1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
t2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

end1 = go_to(y_t, y_vel, t1)
end2 = go_to(y_t, y_vel, t2)

result = 0.0
result += sqrt(norm_sq(cross(minus(y_t, end1), minus(x_t, end1)))) / 2.0
result += sqrt(norm_sq(cross(minus(y_t, end2), minus(x_t, end2)))) / 2.0

print("%.1f" % result)

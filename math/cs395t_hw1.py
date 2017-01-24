from random import random
from math import sqrt, sin, cos


def f1(x_1, x_2, x_3, x_4):
    return (x_1 - x_3) ** 2 + (x_2 - x_4) ** 2


def f2(x_1, x_2):
    n = sqrt((x_1 ** 2) + (x_2 ** 2))
    return (x_1 / n, x_2 / n)


def f3(x_1, x_2, x_3):
    def cross(u_1, u_2, u_3, v_1, v_2, v_3):
        return (u_2 * v_3 - u_3 * v_2,
                u_3 * v_1 - u_1 * v_3,
                u_1 * v_2 - u_2 * v_1)
    return cross(0, 0, 1, x_1, x_2, x_3)


def f5(x_1):
    return (cos(x_1), sin(x_1))


###############################################################################
# Problem 1a.
###############################################################################
s = 1e-5

q_1 = random() * 100
q_2 = random() * 100
q_3 = random() * 100
q_4 = random() * 100

w_1 = random() * 100
w_2 = random() * 100
w_3 = random() * 100
w_4 = random() * 100

f_1 = f1(q_1, q_2, q_3, q_4)
f_2 = f1(q_1 + s * w_1,
         q_2 + s * w_2,
         q_3 + s * w_3,
         q_4 + s * w_4)

# Numerical.
r = (f_2 - f_1) / s

# Analytic.
a = 2 * ((q_1 - q_3) * (w_1 - w_3) + (q_2 - q_4) * (w_2 - w_4))

print("Problem 1a:")
print("Numeric: %.6f" % r)
print("Analytic: %.6f" % a)

###############################################################################
# Problem 1b.
###############################################################################
s = 1e-5

q_1 = random() * 100
q_2 = random() * 100

w_1 = random() * 100
w_2 = random() * 100

f_1 = f2(q_1, q_2)
f_2 = f2(q_1 + s * w_1, q_2 + s * w_2)

# Numerical.
r = [(y - x) / s for x, y in zip(f_1, f_2)]
a = [0 for _ in r]

# Analytic.
hi = q_1
dhi = w_1
lo = sqrt(q_1 ** 2 + q_2 ** 2)
dlo = 1 / 2 * ((q_1 ** 2 + q_2 ** 2) ** (-1/2)) * (2 * q_1 * w_1 + 2 * q_2 * w_2)

a[0] = (lo * dhi - hi * dlo) / (lo ** 2)

hi = q_2
dhi = w_2
lo = sqrt(q_1 ** 2 + q_2 ** 2)
dlo = 1 / 2 * ((q_1 ** 2 + q_2 ** 2) ** (-1/2)) * (2 * q_1 * w_1 + 2 * q_2 * w_2)

a[1] = (lo * dhi - hi * dlo) / (lo ** 2)

print("Problem 1b:")
print("Numeric: %s" % r)
print("Analytic: %s" % a)

###############################################################################
# Problem 1c.
###############################################################################
s = 1e-5

q_1 = random() * 100
q_2 = random() * 100
q_3 = random() * 100

w_1 = random() * 100
w_2 = random() * 100
w_3 = random() * 100

f_1 = f3(q_1, q_2, q_3)
f_2 = f3(q_1 + s * w_1, q_2 + s * w_2, q_3 + s * w_3)

# Numerical.
r = [(y - x) / s for x, y in zip(f_1, f_2)]

# Analytic.
a = [-w_2, w_1, 0]

print("Problem 1c:")
print("Numeric: %s" % r)
print("Analytic: %s" % a)

###############################################################################
# Problem 1e.
###############################################################################
s = 1e-5

q_1 = random() * 100

w_1 = random() * 100

f_1 = f5(q_1)
f_2 = f5(q_1 + s * w_1)

# Numerical.
r = [(y - x) / s for x, y in zip(f_1, f_2)]

# Analytic.
a = [-sin(q_1) * w_1, cos(q_1) * w_1]

print("Problem 1e:")
print("Numeric: %s" % r)
print("Analytic: %s" % a)

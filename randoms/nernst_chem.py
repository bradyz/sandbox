from math import log

# http://laude.cm.utexas.edu/courses/ch301/worksheet/HW10sol.pdf

R = 8.31446
F = 9.64853 * 1e4
T = 298.15

reactM = (5.03)
prodM = (2.81)

reactV = 0.337
prodV = -0.763

n = 2

e = max(prodV - reactV, reactV - prodV)
ret = e - (R * T) / (n * F) * log(prodM / reactM)

# print(ret)

n = 10
red = 1.359
ox = 1.51
e = red - ox
ret = - n * F * e

print(ret / 1000)

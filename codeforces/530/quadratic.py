from math import sqrt

a, b, c = map(int, input().split())
x = int(-b + sqrt(b**2-4*a*c)) // (2 * a)
y = int(-b - sqrt(b**2-4*a*c)) // (2 * a)
print(" ".join(map(str, list(sorted(list(set([x, y])))))))

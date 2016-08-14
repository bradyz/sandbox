from math import sqrt


x, y = map(int, input().split())
r = int(1e9)
for _ in range(int(input())):
    a, b, v = map(int, input().split())
    r = min(r, sqrt((x - a) ** 2 + (y - b) ** 2) / v)
print(r)

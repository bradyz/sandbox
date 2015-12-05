from math import sqrt
mod = 2147483647
for t in range(int(input())):
    a, b, n = map(int, input().split())
    x = (a+sqrt(b))**n
    y = (a-sqrt(b))**n
    r = int(x + y) % mod
    print("Case: " + str(t+1) + ": " + str(r))

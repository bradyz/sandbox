from math import factorial

n = int(input())
c = [int(input()) for _ in range(n)]

r, s = 1, 0

for i in range(n):
    r *= factorial(s+c[i]-1) // factorial(s) // factorial(c[i]-1)
    r %= 1000000007
    s += c[i]

print(r)

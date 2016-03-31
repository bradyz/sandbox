n, a, b = map(int, input().split())
c = [i for i in range(1, n+1)]
x = c.index(a)
print(c[(x + b) % n])

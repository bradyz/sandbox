n = 1000001
c = [0 for _ in range(n)]
c[1] = 1
m = 0
v = 0


def collatz(x):
    if x < n:
        if c[x] == 0:
            if x % 2 == 0:
                c[x] = collatz(x // 2) + 1
            else:
                c[x] = collatz(3*x + 1) + 1
        return c[x]
    else:
        if x % 2 == 0:
            return collatz(x // 2) + 1
        else:
            return collatz(3*x + 1) + 1

for i in range(1, n):
    t = collatz(i)
    if collatz(i) > m:
        v = i
        m = t

print(v)

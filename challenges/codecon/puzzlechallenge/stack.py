n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(x)]
r = 0

def m1(n, m, c):
    for i in range(n):
        for j in range(m):
            for k in range(1, n-i+1):
                for l in range(1, m-j+1):
                    t = [c[a][j:j+l] for a in range(i, i+k)]
                    yield t

for a in m1(n, m, c):
    for b in m1(x, y, d):
        if a == b:
            r = max(r, sum(map(lambda x: sum(x), a)))

print(r)

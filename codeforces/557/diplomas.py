n = int(input())
c = list(list(map(int, input().split())) for _ in range(3))
d = list(x[0] for x in c)
r = sum(d)

for i in range(3):
    if r < n:
        d[i] = min(d[i] + n-r, c[i][1])
        r += c[i][0] - d[i]

print(" ".join(map(str, d)))

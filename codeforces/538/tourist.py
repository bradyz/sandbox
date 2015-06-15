n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(m)]
d = [-1 for _ in range(n+1)]
f = False
for i in range(m):
    d[c[i][0]] = c[i][1]
for i in range(1, c[0][0]):
    d[i] = c[0][0] - c[0][1] - i
i = 1
while i < m:
    if abs(c[i][0] - c[i-1][0]) < abs(c[i][1] - c[i-1][1]):
        f = True
        break
    j = 1
    while abs(c[i][1] - (c[i-1][1] + j)) < abs(c[i][0] - (c[i-1][0] + j)):
        d[c[i-1][0]+j] = d[c[i-1][0]+j-1] + 1
        j += 1
    while c[i-1][0] + j < c[i][0]:
        if d[c[i-1][0]+j-1] < d[c[i][1]]:
            d[c[i-1][0]+j] = d[c[i-1][0]+j-1] + 1
        else:
            d[c[i-1][0]+j] = d[c[i-1][0]+j-1] - 1
        j += 1
    i += 1
if f:
    print("IMPOSSIBLE")
else:
    print(max(d))

n, k = map(int, input().split())
g = [[0 for _ in range(n)] for _ in range(n)]
x = 1
for i in range(n):
    for j in range(k-1):
        g[i][j] = x
        x += 1
for i in range(n):
    for j in range(k-1, n):
        g[i][j] = x
        x += 1
ret = 0
for i in range(n):
    ret += g[i][k-1]
print(ret)
print("\n".join(map(lambda x: " ".join(map(str, x)), g)))

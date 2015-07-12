n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
g = [[0 for j in range(101)] for i in range(101)]

for v in c:
    for i in range(v[0], v[2]+1):
        for j in range(v[1], v[3]+1):
            g[i][j] += 1

print(sum(sum(v) for v in g))

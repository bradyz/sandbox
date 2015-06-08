n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(m)]
r = [[True for j in range(n+1)] for i in range(n+1)]

for v in c:
    r[v[0]][v[1]] = False
    r[v[1]][v[0]] = False

node = -1

for i in range(1, n+1):
    cont = True
    for j in range(1, n+1):
        cont &= r[i][j]
        if not cont:
            break
    if cont:
        node = i
        break

print(n-1)

for i in range(1, n+1):
    if i != node:
        print(node, i)

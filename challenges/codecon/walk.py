from sys import maxsize as MAXINT


r, c = map(int, input().split())
r = 2*r+1
c = 2*c+1
g = [[-MAXINT for _ in range(c)] for _ in range(r)]
for i in range(r):
    row = list(map(int, input().split()))
    if i % 2 == 0:
        for j in range(c):
            g[i][j] = 0
        for j in range(len(row)):
            g[i][j*2+1] = row[j]
    else:
        for j in range(len(row)):
            g[i][j*2] = row[j]
cost = [[g[i][j] for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            cost[i][j] += cost[i][j-1]
        elif j == 0:
            cost[i][j] += cost[i-1][j]
        else:
            cost[i][j] += max(cost[i-1][j], cost[i][j-1])
print(cost[r-1][c-1])

import sys
from pprint import PrettyPrinter
pp = PrettyPrinter()

for i, line in enumerate(sys.stdin):
    if i == 0:
        n = int(line)
        g = [[False for j in range(n+1)] for i in range(n+1)]
    elif i == 1:
        c = [0] + list(map(int, line.split()))
        d = [[999 for j in range(n+1)] for i in range(n+1)]
        for i in range(1, n+1):
            d[i][i] = c[i]
    else:
        t = list(map(int, line.split()))
        g[t[0]][t[1]] = g[t[0]][t[1]] = True

l = []

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][j]:
                d[i][j] = d[j][i] = min(d[i][j], d[i][i] + c[j])
            d[i][j] = d[j][i] = min(d[i][j], d[i][k] + d[k][j] - c[k])
            pp.pprint(d)

n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
b = [(i, j) for i in range(n) for j in range(m) if g[i][j] == "*"] or [(0, 0)]
if n * m * len(b) < 1000000:
    found = None
    for i in range(n):
        for j in range(m):
            yes = True
            for x, y in b:
                if x != i and y != j:
                    yes = False
            if yes:
                found = (i + 1, j + 1)
    if found:
        print("YES")
        print(" ".join(map(str, found)))
    else:
        print("NO")
else:
    x = dict()
    y = dict()
    for i, j in b:
        x[i] = x.get(i, 0) + 1
        y[j] = y.get(j, 0) + 1
    max_x = max(x, key=lambda v: (x[v], y.get(v, 0)))
    max_y = max(y, key=lambda v: (y[v], x.get(v, 0)))
    for i, j in b:
        if i != max_x and j != max_y:
            print("NO")
            break
    else:
        print("YES")
        print(max_x+1, max_y+1)

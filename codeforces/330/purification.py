n = int(input())
c = [list(input()) for _ in range(n)]
r = set()
s = set()
rows = set()
cols = set()
for i in range(n):
    for j in range(n):
        if c[i][j] == "." and (i not in rows):
            r.add((i+1, j+1))
            rows.add(i)
            break
for i in range(n):
    for j in range(n):
        if c[j][i] == "." and (i not in cols):
            s.add((j+1, i+1))
            cols.add(i)
            break
if not set(range(n)) - rows:
    print("\n".join(map(lambda x: str(x[0]) + " " + str(x[1]), r)))
elif not set(range(n)) - cols:
    print("\n".join(map(lambda x: str(x[0]) + " " + str(x[1]), s)))
else:
    print(-1)

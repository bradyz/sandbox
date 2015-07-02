n = int(input())
c = [tuple(map(float, input().split(","))) for _ in range(2*n)]
v = {}
r = []

for i in range(2*n):
    if c[i] in v:
        v[c[i]].append(i-n)
    else:
        v[c[i]] = [i]

c.sort(key=lambda x: sum(x))

for i in range(0, 2*n, 2):
    if c[i] == c[i+1]:
        r.append(",".join(map(str, v[c[i]])))
    else:
        if v[c[i]][0] > v[c[i+1]][0]:
            r.append(str(v[c[i+1]][0])+","+str(v[c[i]][0]-n))
        else:
            r.append(str(v[c[i]][0])+","+str(v[c[i+1]][0]-n))

print("\n".join(sorted(r)))

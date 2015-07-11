from sys import maxsize

n = int(input())
c = list(map(int, input().split()))
d = list(map(int, input().split()))
x = dict()
v = list((c[i], d[i]) for i in range(n))
r = maxsize
s = sum(d)
vis = set()

v.sort()

for i in range(n):
    if v[i][0] in x:
        x[v[i][0]].append(v[i][1])
    else:
        x[v[i][0]] = [v[i][1]]

for i in range(n):
    if v[i][0] in vis:
        continue

    vis.add(v[i][0])

    t = sum(x[v[i][0]])

    if len(x[v[i][0]]) > 1:
        t += sum(sorted(v[j][1] for j in range(i))[-len(x[v[i][0]])+1:])

    r = min(r, s-t)

print(r)

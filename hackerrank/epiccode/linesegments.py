n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
c.sort(key=lambda x: (x[0], x[1]-x[0]))
r = [c[0]]
for i in range(1, len(c)):
    if not c[i][0] == r[-1][0] and c[i][1] > r[-1][1]:
        r.append(c[i])
c.sort(key=lambda x: (x[1], x[1]-x[0]))
s = [c[-1]]
for i in range(n-2, -1, -1):
    if not c[i][1] == s[-1][1] and c[i][0] < s[-1][0]:
        s.append(c[i])
print(max(len(r), len(s)))

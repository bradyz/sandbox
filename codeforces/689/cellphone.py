p = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [-1, 0, -1]]

n = int(input())
d = [int(x) for x in input()]
s = [(i, j) for i in range(4) for j in range(3) if p[i][j] != -1]
c = [True for _ in s]
m = {((i+1) % 10): s[i] for i in range(len(s))}
for i in range(1, n):
    for j in range(len(s)):
        if not c[j]:
            continue
        try:
            sji = s[j][0] + (m[d[i]][0] - m[d[i-1]][0])
            sjj = s[j][1] + (m[d[i]][1] - m[d[i-1]][1])
            s[j] = (sji, sjj)
            if s[j][0] < 0 or s[j][1] < 0 or p[s[j][0]][s[j][1]] == -1:
                c[j] = False
        except Exception as e:
            c[j] = False
if sum(c) > 1:
    print("NO")
else:
    print("YES")

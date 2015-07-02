n = int(input())
c = [tuple(map(float, input().split(","))) for _ in range(2*n)]
u = [-1 for _ in range(2*n)]

for i in range(n):
    m = 999999
    m_j = -1
    for j in range(n, 2*n):
        if u[j] != -1:
            continue
        t = abs(c[i][0]-c[j][0])+abs(c[i][1]-c[j][1])
        t += abs(c[i][2]-c[j][2])+abs(c[i][3]-c[j][3])
        if t < m:
            m = t
            m_j = j
    u[i] = m_j - n
    u[m_j] = i

for i in range(n):
    print(str(i)+","+str(u[i]))

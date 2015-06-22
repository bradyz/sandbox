n, m = map(int, input().split())
c = [0 for _ in range(n+1)]
a = False
for _ in range(m):
    t = list(map(int, input().split()))
    if t[0] == 1:
        c[t[1]] += 2
        x = 2
        for i in range(1, t[2] - t[1] + 1):
            x += (i+1) * (i+2)
            if not a:
                c[t[1]+i] = (i+1) * (i+2)
            else:
                c[t[1]+i] += x
        for i in range(t[2]+1, n+1):
            if a:
                c[i] += x
        if not a:
            for i in range(1, n+1):
                c[i] += c[i-1]
        a = True
    if t[0] == 2:
        print(c[t[2]] - c[t[1]-1])

import sys
for i, line in enumerate(sys.stdin):
    if i == 0:
        n = int(line)
    elif i == 1:
        c = [sys.maxsize] + list(map(int, line.split()))
        d = [0] + c[1:]
    else:
        t = list(map(int, line.split()))
        d[t[0]] += c[t[1]]
        d[t[1]] += c[t[0]]
        print(d)
m = 0
for i in range(1, n):
    if d[i] < d[m]:
        m = i
print(m)

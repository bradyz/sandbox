n, m = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(m)]
a = {}
t = 0
for i in range(len(x)):
    tmp = x[i]
    if tmp[1] in a:
        a[tmp[1]].append(tmp[0])
    else:
        a[tmp[1]] = [tmp[0]]


def solve(d, c):
    global t

    if c not in d:
        return 1

    r = 0

    for i in d[c]:
        tmp = solve(d, i)
        if tmp % 2 == 0:
            t += 1
        else:
            r += tmp

    return r + 1


solve(a, x[0][1])
print(t)

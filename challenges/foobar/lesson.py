import sys


def answer(c):
    v = {}

    def construct(i, d):
        if not d or i >= len(d):
            return
        for j in range(len(d)):
            for k in range(j+1, len(d)):
                if i < len(d[j]) and i < len(d[k]) and d[j][i] != d[k][i]:
                    if d[j][i] in v:
                        v[d[j][i]].add(d[k][i])
                    else:
                        v[d[j][i]] = set([d[k][i]])
        j = 0
        while j < len(d):
            k = j+1
            while k < len(d):
                if i >= len(d[j]) or i+1 >= len(d[k]) or d[j][i] != d[k][i]:
                    break
                if d[j][i] in v:
                    v[d[j][i]].add(d[k][i+1])
                else:
                    v[d[j][i]] = set([d[k][i+1]])
                k += 1
            construct(i+1, d[j:k])
            j += 1

    def dfs(x, y):
        y.append(x)
        if x not in v:
            return y
        for b in v[x]:
            z = y[:]
            e = dfs(b, z)
            if len(e) > len(x):
                x = e
        return x

    construct(0, c)
    print(v)
    r = []
    for a in v:
        l = []
        t = dfs(a, l)
        if len(t) > len(r):
            r = t
    return "".join(r)


sys.setrecursionlimit(10)
print(answer(raw_input().split()))

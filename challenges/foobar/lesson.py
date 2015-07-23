import sys


def answer(c):
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
                if i >= len(d[j]) or i >= len(d[k]) or d[j][i] != d[k][i]:
                    break
                k += 1
            construct(i+1, d[j:k])
            j = k

    def dfs(x, y):
        y.append(x)
        if x not in v:
            return y
        new_r = y[:]
        for new_x in v[x]:
            if x != new_x:
                new_y = y[:]
                e = dfs(new_x, new_y)
                if len(e) > len(new_r):
                    new_r = e
        return new_r

    v = {}
    r = []
    construct(0, c)
    for a in v:
        l = []
        t = dfs(a, l)
        if len(t) > len(r):
            r = t

    return "".join(r)


sys.setrecursionlimit(10)
print(answer(raw_input().split()))

def answer(c):
    def comparator(x, y):
        def dfs(z):
            t = (z == y)
            if t:
                return t
            for new_z in v[z]:
                if new_z != z:
                    t |= dfs(new_z)
            return t

        if dfs(x):
            return -1
        else:
            return 1

    def comparatorV2(x, y):
        if y in w[x]:
            return -1
        else:
            return 1

    v = {}
    w = {}

    def seed():
        def dfs(x):
            w[k] |= v[x]
            for y in v[x]:
                dfs(y)

        for i in range(len(c)):
            for j in range(len(c[i])):
                if c[i][j] not in v:
                    v[c[i][j]] = set()
                if c[i][j] not in w:
                    w[c[i][j]] = set()

        for i in range(len(c)):
            for j in range(i+1, len(c)):
                k = 0
                while k < min(len(c[i]), len(c[j])) and c[i][k] == c[j][k]:
                    k += 1
                if k < min(len(c[i]), len(c[j])):
                    v[c[i][k]].add(c[j][k])

        for k in v:
            dfs(k)

    seed()

    return "".join(sorted(v.keys(), cmp=comparatorV2))


print(answer(raw_input().split()))

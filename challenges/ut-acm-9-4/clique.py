def powerset(u, v):
    for i in range(len(v)):
        for x in powerset(u+[v[i]], v[i+1:]):
            yield x
    yield u

for _ in range(int(input())):
    n, m = map(int, input().split())
    c = dict()
    r = []

    for _ in range(m):
        u, v = map(int, input().split())
        c[u] = c.get(u, set([u])) | set([v])
        c[v] = c.get(v, set([v])) | set([u])

    for v in powerset([], list(i+1 for i in range(n))):
        t = 0

        for i in range(len(v)):
            for j in range(i+1, len(v)):
                if v[j] not in c or v[i] not in c[v[j]]:
                    t += 1

        if t <= 1 and len(v) > len(r):
            r = v

    print(len(r))

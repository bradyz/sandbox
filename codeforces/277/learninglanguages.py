n, m = map(int, input().split())
lang = [set(list(map(int, input().split()))[1:]) for _ in range(n)]
v = []
r = 0
for i in range(n):
    c = []
    for j in range(len(v)):
        if lang[i] & v[j]:
            v[j] |= lang[i]
            c.append(j)
    if not c and lang[i]:
        v.append(lang[i])
    else:
        for j in list(reversed(c))[1:]:
            v[c[0]] |= v[j]
            v.remove(v[j])

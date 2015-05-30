n, m = map(int, input().split())
lang = [frozenset(list(map(int, input().split()))[1:]) for _ in range(n)]
lang = list(sorted(lang, key=lambda x: -len(x)))
v = [lang[0]]
r = lang.count(frozenset())
for i in range(1, n):
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
print(v)
print(len(v) - 1 + (r - 1 + len(v) if r > 0 else 0))

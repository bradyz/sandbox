for _ in range(int(input())):
    b, w = map(int, input().split())
    c = list()
    for _ in range(b):
        n, m, v = map(int, input().split())
        c.append((n * m, v))
    c.sort(key=lambda x: -x[1])
    r = 0
    for x, y in c:
        if w > 0:
            r += y * min(w, x)
            w -= min(w, x)
    print(r)

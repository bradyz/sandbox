def check():
    for i in range(1, len(c)):
        if c[i] != "?" and c[i-1] != "?":
            if c[i] < c[i-1]:
                return False
    return True


def bf(v):
    global r

    if not v:
        if check():
            r += 1
        return

    for val in u:
        c[v[0]] = val
        if check():
            bf(v[1:])
        c[v[0]] = "?"


for _ in range(int(input())):
    c = list(input())
    q = list()
    u = list(map(str, range(1, 10)))
    r = 0

    for i in range(len(c)):
        if c[i] == "?":
            q.append(i)

    bf(q)

    print(r)

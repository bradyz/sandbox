def solve(n):
    t = 0
    v = 1
    while v < n:
        v *= 3
        t += 1
    c = [0 for _ in range(t+1)]

    def s(r, k):
        t = 3 ** k
        if t < 1:
            return

        if t > r:
            s(r, k-1)
        elif 2*t > r:
            c[k] += 1
            s(r-t, k-1)
        else:
            c[k] -= 1
            c[k+1] += 1
            s(r-2*t, k-1)

    s(n, t)

    for i in range(len(c)):
        if c[i] == -1:
            c[i] = "L"
        elif c[i] == 0:
            c[i] = "-"
        elif c[i] == 1:
            c[i] = "R"
        elif c[i] == 2:
            c[i] = "L"
            c[i+1] += 1

    if c[-1] == "-":
        c.pop()

    return c


def check(n, c):
    x = n
    y = 0
    for i in range(len(c)):
        if c[i] == "R":
            y += 3 ** i
        elif c[i] == "L":
            x += 3 ** i
    print(n, c)
    return x == y

for i in range(1, 20):
    print(check(i, solve(i)))

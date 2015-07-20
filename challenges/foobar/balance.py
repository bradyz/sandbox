def solve(c):
    t = 0
    while 3**t < c:
        t += 1
    r = ["-" for _ in range(t+1)]

    def s(n):
        if n == 0:
            return

        t = 0
        while 3**(t+1) <= abs(n):
            t += 1

        if 3 ** t <= abs(n) and 2 * 3 ** t > abs(n):
            if n < 0:
                r[t] = "L"
                s(n + 3 ** t)
            else:
                r[t] = "R"
                s(n - 3 ** t)
        else:
            if n < 0:
                r[t+1] = "L"
                s(n + 3 ** (t+1))
            else:
                r[t+1] = "R"
                s(n - 3 ** (t+1))

    s(c)

    i = len(r)-1

    while i >= 0 and r[i] == "-":
        i -= 1

    return r

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

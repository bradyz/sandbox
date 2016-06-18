import sys

e = 47
t = 1466253000.000
c = "red green blue yellow orange pink".split()
s = [
    (75, 75),
    (75, 175),
    (75, 275),
    (180, 75),
    (180, 175),
    (180, 275)
]
r = [
    (300, 75),
    (300, 175),
    (300, 275),
    (500, 75),
    (500, 175),
    (500, 275)
]


def h():
    global e
    a = list(range(6))
    for b in range(1, 6):
        e *= 53
        e %= 1000000009
        k = e % (b + 1)
        d = a[b]
        a[b] = a[k]
        a[k] = d
    return a


if __name__ == "__main__":
    tmp = list()
    print("5 5 %s" % t)
    for line in sys.stdin:
        cur_s = h()
        cur_r = h()
        print("next %s" % t)
        for expr in line.lower().strip().split("then"):
            if "seconds" in expr:
                wait = [int(x) for x in expr.split() if x.isdigit()][0]
                t += wait
            elif "background" in expr:
                print("5 5 %s" % t)
            else:
                for i, color in enumerate(c):
                    if color not in expr:
                        continue
                    tmp = dict()
                    if "rectangle" in expr:
                        for j in range(6):
                            tmp[c[cur_r[j]]] = r[j]
                    else:
                        for j in range(6):
                            tmp[c[cur_s[j]]] = s[j]
                    pos = tmp[color]
                    times = 1
                    if "times" in expr:
                        times = [int(x) for x in expr.split() if x.isdigit()][0]
                    for _ in range(times):
                        print("%s %s %s" % (pos[0], pos[1], t))
    print("done %s" % t)

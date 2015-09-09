import sys

for line in sys.stdin:
    a = str(int(line))
    vis = set()
    h = True
    c = a
    r = 0

    while c != "1":
        if c in vis:
            print("unhappy " + str(r))
            h = False
            break
        vis.add(c)
        t = 0
        for v in c:
            t += int(v)**2
        c = str(t)
        r += 1

    if h:
        print("happy " + str(r))

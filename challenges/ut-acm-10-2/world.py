from queue import Queue
from sys import maxsize as MAXINT


def solve():
    v = set()
    q = Queue()
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i, j in d:
        q.put((s_x, s_y, i, j, 1))

    while not q.empty():
        x, y, i, j, k = q.get()

        if (x, y, i, j) in v:
            continue

        v.add((x, y, i, j))

        if x == f_x:
            f = True
            for t_x, t_y in a:
                if (j == 1 and y < t_y and t_y < f_y) or \
                        (j == -1 and y > t_y and t_y > f_y):
                    f = False
            if f and ((y <= f_y and j == 1) or (y >= f_y and j == -1)):
                return k
        elif y == f_y:
            f = True
            for t_x, t_y in a:
                if (i == 1 and x < t_x and t_x < f_x) or \
                        (i == -1 and x > t_x and t_x > f_x):
                    f = False
            if f and ((x <= f_x and i == 1) or (x >= f_x and i == -1)):
                return k

        min_x = MAXINT
        min_y = MAXINT
        f = False

        for t_x, t_y in a:
            if x == t_x:
                if y <= t_y and j == 1:
                    if not f or abs((x-t_x)+(y-t_y)) < abs((x-min_x)+(y-min_y)):
                        min_x = t_x
                        min_y = t_y-1
                        f = True
                elif y >= t_y and j == -1:
                    if not f or abs((x-t_x)+(y-t_y)) < abs((x-min_x)+(y-min_y)):
                        min_x = t_x
                        min_y = t_y+1
                        f = True
            elif y == t_y:
                if x <= t_x and i == 1:
                    if not f or abs((x-t_x)+(y-t_y)) < abs((x-min_x)+(y-min_y)):
                        min_x = t_x-1
                        min_y = t_y
                        f = True
                elif x >= t_x and i == -1:
                    if not f or abs((x-t_x)+(y-t_y)) < abs((x-min_x)+(y-min_y)):
                        min_x = t_x+1
                        min_y = t_y
                        f = True

        if f:
            for o, p in d:
                q.put((min_x, min_y, o, p, k+1))

    return -1


for i in range(int(input())):
    s_x, s_y, f_x, f_y, n = map(int, input().split())
    a = set(tuple(map(int, input().split())) for _ in range(n))
    r = solve()

    if r != -1:
        print("Case " + str(i+1) + ": " + str(r))
    else:
        print("Case " + str(i+1) + ": LOST IN SPACE")

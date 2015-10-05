from queue import Queue
from sys import maxsize as MAXINT


def hit(x1, y1, i, j, x2, y2):
    if x1 == x2:
        if j == 1 and y1 <= y2:
            return True
        elif j == -1 and y1 >= y2:
            return True
    elif y1 == y2:
        if i == 1 and x1 <= x2:
            return True
        elif i == -1 and x1 >= x2:
            return True
    return False


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


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

        if hit(x, y, i, j, f_x, f_y):
            f = False
            for t_x, t_y in a:
                if hit(x, y, i, j, t_x, t_y) and \
                        dist(x, y, t_x, t_y) < dist(x, y, f_x, f_y):
                    f = True
            if not f:
                return k

        min_x = MAXINT
        min_y = MAXINT

        for t_x, t_y in a:
            if hit(x, y, i, j, t_x, t_y) and \
                    (dist(x, y, t_x, t_y) < dist(x, y, min_x, min_y) + 1):
                min_x = t_x
                min_y = t_y
                if i == 1:
                    min_x = t_x - 1
                elif i == -1:
                    min_x = t_x + 1
                elif j == 1:
                    min_y = t_y - 1
                else:
                    min_y = t_y + 1

        if min_x != MAXINT and min_y != MAXINT:
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

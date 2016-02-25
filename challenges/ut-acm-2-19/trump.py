DIR = [(-1, 0), (0, -1), (-1, -1)]


def memo(func):
    cache = dict()

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return wrapper


@memo
def can_make(t, x, y, k):
    if g[x][y] == "0":
        return False
    elif k == 1:
        return True
    elif x - 1 < 0 or y - 1 < 0:
        return False
    for dx, dy in DIR:
        if not can_make(t, x+dx, y+dy, k-1):
            return False
    return True


if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        g = [input() for _ in range(n)]
        to_vis = list()
        for i in range(n):
            for j in range(n):
                if not can_make(t, i, j, 1):
                    continue
                to_vis.append((i, j))
        ret = {0: 0}
        for k in range(1, n+1):
            if k-1 not in ret:
                break
            next_to_vis = list()
            while to_vis:
                i, j = to_vis.pop()
                if can_make(t, i, j, k):
                    ret[k] = ret.get(k, 0) + 1
                    next_to_vis.append((i, j))
            to_vis = next_to_vis
        for i in range(2, max(ret)+1):
            print(i, ret[i])

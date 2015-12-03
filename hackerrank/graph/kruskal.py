import sys


def union(x, y):
    p[find(x)] = find(y)


def find(i):
    if p[i] == -1:
        return i
    return find(p[i])


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    n, m = map(int, input().split())
    p = [-1 for _ in range(n+1)]
    g = [list(map(int, input().split())) for _ in range(m)]
    g.sort(key=lambda x: x[2])
    r = 0
    for u, v, w in g:
        if find(u) != find(v):
            union(u, v)
            r += w
    print(r)

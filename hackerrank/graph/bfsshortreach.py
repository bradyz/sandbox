from queue import Queue


def bfs():
    q = Queue()
    q.put((s, 0, set([s])))

    while not q.empty():
        x = q.get()
        if r[x[0]] == -1 or x[1] < r[x[0]]:
            r[x[0]] = x[1]
        if x[1] > r[x[0]]:
            continue
        for v in c:
            if v[0] == x[0] and v[1] not in x[2]:
                if r[x[1]] == -1 or x[1]+w < r[v[1]]:
                    q.put((v[1], x[1]+w, set([v[1]]) | x[2]))
            elif v[1] == x[0] and v[0] not in x[2]:
                if r[x[0]] == -1 or x[0]+w < r[v[0]]:
                    q.put((v[0], x[1]+w, set([v[0]]) | x[2]))
        print(q.qsize())


def bfsV2():
    q = Queue()
    q.put((s, 0))
    vis = set()

    while not q.empty():
        x = q.get()
        if r[x[0]] == -1 or x[1] < r[x[0]]:
            r[x[0]] = x[1]
        for v in c:
            if v[0] == x[0] and v[1] not in vis and \
                    (r[v[1]] == -1 or x[1]+w < r[v[1]]):
                vis.add(v[1])
                q.put((v[1], x[1]+w))
            elif v[1] == x[0] and v[0] not in vis and \
                    (r[v[0]] == -1 or x[1]+w < r[v[0]]):
                vis.add(v[0])
                q.put((v[0], x[1]+w))


if __name__ == "__main__":
    t = int(input())
    w = 6

    for _ in range(t):
        n, m = map(int, input().split())
        c = set(tuple(int(v) for v in input().split()) for j in range(m))
        s = int(input())
        r = [-1 for j in range(n+1)]
        bfsV2()
        print(" ".join(str(r[i]) for i in range(1, n+1) if i != s))

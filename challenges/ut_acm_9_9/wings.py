from queue import Queue


for _ in range(int(input())):
    n, b, m = map(int, input().split())    
    h = [int(input()) for _ in range(m)]

    q = Queue()
    v = set()
    q.put((0, 0))
    v.add(0)

    r = -1

    while not q.empty():
        x, y = q.get()
        if x == n:
            r = y
            break
        for xx in range(x-b, 0, -b):
            if xx in v:
                break
            v.add(xx)
            q.put((xx, y))
        for w in h:
            if x + w in v:
                continue
            v.add(x + w)
            q.put((x + w, y + 1))

    print(r)


from queue import Queue


for _ in range(int(input())):
    a, b, c, x, y, z = map(int, input().split())
    ret = 0

    q = Queue()
    v = set()
    q.put((x, 0))
    while not q.empty():
        num, k = q.get()
        if num == a:
            ret += k
            break
        if num in v:
            continue
        v.add(num)
        if num % 2 == 0:
            q.put((num // 2, k+1))
        q.put((num + 1, k+1))

    q = Queue()
    v = set()
    q.put((y, 0))
    while not q.empty():
        num, k = q.get()
        if num == b:
            ret += k
            break
        if num in v:
            continue
        v.add(num)
        if num % 2 == 0:
            q.put((num // 2, k+1))
        q.put((num + 1, k+1))

    q = Queue()
    v = set()
    q.put((z, 0))
    while not q.empty():
        num, k = q.get()
        if num == c:
            ret += k
            break
        if num in v:
            continue
        v.add(num)
        if num % 2 == 0:
            q.put((num // 2, k+1))
        q.put((num + 1, k+1))

    print(ret)

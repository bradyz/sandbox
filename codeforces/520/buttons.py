def solve1(n, m):
    c = 0
    while n < m:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        c += 1
    print(n - m + c)


def solve2(n, m):
    from queue import Queue
    q = Queue()
    q.put((n, 0))

    while not q.empty():
        c, d = q.get()
        if c == m:
            print(d)
            break
        q.put((c-1, d+1))
        q.put((c*2, d+1))


a, b = map(int, input().split())
# solve1(a, b)
solve2(a, b)

from queue import PriorityQueue

for _ in range(int(input())):
    k, n = map(int, input().split())
    c = dict()
    a = list(map(int, input().split()))
    q = PriorityQueue()
    for i in range(k):
        q.put(a[i])
        c[a[i]] = c.get(a[i], 0) + 1
    m = q.get()
    q.put(m)
    r = [m]
    for i in range(k, n):
        q.put(a[i])
        c[a[i]] = c.get(a[i], 0) + 1
        c[a[i-k]] -= 1
        p = q.get()
        while p in c and c[p] <= 0:
            p = q.get()
        q.put(p)
        r.append(p)
    print(" ".join(map(str, r)))

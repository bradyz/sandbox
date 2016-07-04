from queue import Queue
g = dict()
for _ in range(int(input())):
    v, _, u = map(lambda x: x.lower(), input().split())
    if u not in g:
        g[u] = list()
    g[u].append(v)
q = Queue()
q.put(("polycarp", 1))
r = 0
while not q.empty():
    u, w = q.get()
    r = max(r, w)
    for v in g.get(u, []):
        q.put((v, w + 1))
print(r)

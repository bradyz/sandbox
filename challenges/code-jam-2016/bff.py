def foo(x, vis):
    r = 0
    for i in range(1, n+1):
        if i in vis:
            continue
        vis1 = set()
        cur = i
        while True:
            vis1.add(cur)
            if c[cur] in vis1 or c[cur] in vis:
                if c[cur] == x:
                    r = max(r, len(vis1))
                break
            cur = c[cur]
    return r


for t in range(1, int(input()) + 1):
    n = int(input())
    c = [0] + list(map(int, input().split()))
    r = 0
    for i in range(1, n+1):
        vis = set()
        cur = i
        pre = -1
        while True:
            vis.add(cur)
            if c[cur] in vis:
                if c[cur] == pre:
                    r = max(r, len(vis) + foo(cur, vis))
                elif c[cur] == i:
                    r = max(r, len(vis))
                break
            pre = cur
            cur = c[cur]
    print("Case #%d: %d" % (t, r))

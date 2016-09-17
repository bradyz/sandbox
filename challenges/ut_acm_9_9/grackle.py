for _ in range(int(input())):
    n = int(input())
    g = set(map(int, input().split()))
    iam = dict()
    orig = dict()
    # move to the left
    l = set()
    # move to the right
    r = set()
    for v in g:
        iam[v] = v
        orig[v] = v
        if v+1 in g and (v-1 not in g) and not (v-2 in g and v-3 in g):
            l.add(v)
        if v-1 in g and (v+1 not in g) and not (v+2 in g and v+3 in g):
            r.add(v)
    while l or r:
        for v in l | r:
            g.remove(v)
        for v in r:
            iam[v+1] = iam.pop(v)
            g.add(v+1)
        for v in l:
            iam[v-1] = iam.pop(v)
            g.add(v-1)
        l = set()
        r = set()
        for v in g:
            if v+1 in g and (v-1 not in g) and not (v-2 in g and v-3 in g):
                l.add(v)
            if v-1 in g and (v+1 not in g) and not (v+2 in g and v+3 in g):
                r.add(v)
    print(max(abs(v - orig[iam[v]]) for v in iam))

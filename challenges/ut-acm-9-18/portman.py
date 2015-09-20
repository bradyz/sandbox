for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(input().split())
    r = list()

    for i in range(len(c)):
        for j in range(i+1, len(c)):
            if len(c[i]) < k or len(c[j]) < k:
                continue

            if c[i][:k] == c[j][-k:]:
                r.append(c[j]+c[i][k:])
            if c[i][-k:] == c[j][:k]:
                r.append(c[i]+c[j][k:])

    print(len(r))

    if r:
        print("\n".join(sorted(v for v in r if v not in c)))

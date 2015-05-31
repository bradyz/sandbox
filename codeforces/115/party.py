if __name__ == "__main__":
    t = int(input())
    c = [int(input()) for _ in range(t)]
    v = [[] for _ in range(t+1)]

    for i in range(t):
        if c[i] == -1:
            v[0].append(i+1)
        else:
            v[c[i]].append(i+1)

    s = [(val, 1) for val in v[0]]
    m = 0

    while s:
        cur = s.pop()
        m = max(cur[1], m)
        for n in v[cur[0]]:
            s.append((n, cur[1]+1))

    print(m)

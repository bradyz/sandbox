for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input().split())
    c = dict()
    r = int(1e9)
    i, j = 0, 0
    while i < n and j <= n:
        if j < n and len(c) < k:
            c[s[j]] = c.get(s[j], 0) + 1
            j += 1
        else:
            c[s[i]] -= 1
            if c[s[i]] == 0:
                c.pop(s[i])
            i += 1
        if len(c) == k and j - i < r:
            r = j - i
    if r == int(1e9):
        print(-1)
    else:
        print(r)

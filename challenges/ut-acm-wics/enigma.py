for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    v = [1 for _ in range(n)]
    w = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if c[i] > c[j]:
                if v[j] + 1 > v[i]:
                    v[i] = v[j] + 1
                    w[i] = w[j]
                elif v[j] + 1 == v[i]:
                    w[i] += w[j]
    x = max(v)
    y = sum(w[i] for i in range(n) if v[i] == x)
    print(x, y)

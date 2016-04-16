for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    r = list()
    for i in range(n):
        r.append((c[2 * i], c[2 * i] + c[2 * i + 1]))
    r.sort(key=lambda x: x[1])
    ret = [r[0]]
    for i in range(1, n):
        if r[i][0] >= ret[-1][1]:
            ret.append(r[i])
    print(len(ret))

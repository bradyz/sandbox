for _ in range(int(input())):
    a, b, c = map(int, input().split())
    s = [input() for _ in range(a)]
    x = {input().lower() for _ in range(b)}
    y = {input().lower() for _ in range(c)}
    ret1 = -1e9
    ret2 = ""
    for m in s:
        l = m.lower()
        tmp = sum(f in l for f in x) - sum(f in l for f in y)
        if tmp > ret1:
            ret1 = tmp
            ret2 = m
    print(ret2)

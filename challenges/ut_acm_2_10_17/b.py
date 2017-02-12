for _ in range(int(input())):
    m, n = map(int, input().split())
    c = list(sorted(map(int, input().split())))
    result = 0
    for i in range(m - n):
        result += c[i]
    print(result)

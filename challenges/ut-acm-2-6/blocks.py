for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    s = sum(c)
    a = s // n
    for i in range(s - s // n * n):
        c[c.index(max(c))] -= 1
    r = 0
    for x in c:
        r += abs(a - x)
    print(s - s // n * n, r // 2)

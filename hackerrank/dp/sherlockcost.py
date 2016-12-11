def solve(n, c):
    dp1 = [0 for _ in range(101)]
    dp2 = [0 for _ in range(101)]

    for i in range(1, n):
        for j in [1, c[i]]:
            a = abs(1 - j) + dp1[1]
            b = abs(c[i-1] - j) + dp1[c[i-1]]
            dp2[j] = max(a, b)
        for j in [1, c[i]]:
            dp1[j] = dp2[j]

    print(max(dp1))


for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    solve(n, c)

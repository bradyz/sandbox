def solve(v):
    if v[0] == 1:
        print(dp1[v[2]] - dp1[v[1]-1])
    else:
        print(dp2[v[2]] - dp2[v[1]-1])

if __name__ == "__main__":
    n = int(input())
    c = list(map(int, input().split()))

    dp1 = [0 if i == 0 else c[i-1] for i in range(n+1)]
    dp2 = [0] + list(sorted(c))

    for i in range(1, n+1):
        dp1[i] += dp1[i-1]
        dp2[i] += dp2[i-1]

    for _ in range(int(input())):
        solve(list(map(int, input().split())))

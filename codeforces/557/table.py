n = int(input())
c = list(map(int, input().split()))
d = list(map(int, input().split()))
v = [[c[i], d[i]] for i in range(n)]
v.sort(key=lambda x: (x[0], -x[1]))
for i in range(1, n):
    v[i][1] += v[i-1][1]
print(v)
dp = [999 for _ in range(n+1)]
i = 1
while i < n+1:
    j = 0
    while i-1+j < n and v[i-1][0] == v[i-1+j-1][0]:
        if j == 1:
            if i-1 == 0:
                dp[j] = v[n-1][1] - v[i-1][1]
            else:
                print(v[i-1][1], v[i-2][1])
                dp[j] = min(dp[j], v[n-1][1] - (v[i-2][1] - v[i-3][1]))
        elif j == 2:
            dp[j] = min(dp[j], v[i-1+j-1][1]-v[i-2][1])
        else:
            print(i, j)
            t = v[n-1][1]
            t -= v[min(i-2, j)][1]
            t -= v[n-1][1] - v[i-1+j-1][1]
            dp[j] = min(dp[j], t)
        j += 1
    i += max(1, j)
print(dp)

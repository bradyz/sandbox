from collections import Counter

n = int(input())
c = Counter(list(map(int, input().split())))
m = max(c)
dp = [0 for _ in range(m+1)]

for i in range(1, m+1):
    if i == 1:
        dp[i] = c[i]
    else:
        dp[i] = max(dp[i-1], dp[i-2]+i*c[i])

print(dp[-1])

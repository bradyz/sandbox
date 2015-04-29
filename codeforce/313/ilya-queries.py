# 313B: Ilya Queries
# Start Time: 12:46 a.m. 4-28-15
# End Time: 1:59 a.m. 4-28-15

query = input()

dp = [0 for _ in range(len(query) + 1)]

for i in range(1, len(query)+1):
    if i > 1:
        dp[i] = dp[i-1] + int(query[i-1] == query[i-2])

for _ in range(int(input())):
    q = list(map(int, input().split()))
    print(dp[q[1]] - dp[q[0]])

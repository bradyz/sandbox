n = int(input())

values = [int(input()) for _ in range(n)]

counts = list({x: values.count(x) for x in values}.items())
counts.sort()

to_get = int(input())

dp = [[0 for _ in range(len(counts)+1)] for _ in range(to_get+1)]
dp[0][0] = 1

for i in range(to_get+1):
    for j in range(1, len(counts)+1):
        coin, count = counts[j-1]

        dp[i][j] = dp[i][j-1]

        for k in range(1, count+1):
            if i - k * coin < 0:
                continue

            dp[i][j] += dp[i - k * coin][j-1]
            dp[i][j] %= int(1e9 + 7)
#
# print(counts)
#
# for row in dp:
#     print(row)

print(dp[to_get][len(counts)])

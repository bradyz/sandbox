# 489C: Given Length and Sum of Digits
# Start: 2:41 p.m. 4-29-15
# End: 3:54 p.m. 4-29-15

# from pprint import PrettyPrinter
# pp = PrettyPrinter(indent=1)

args = list(map(int, input().split()))
m = args[0]
s = args[1]

dp = [[-1 for i in range(s+1)] for j in range(m+1)]
dp1 = [[float('inf') for i in range(s+1)] for j in range(m+1)]

for i in range(m+1):
    for j in range(s+1):
        for k in range(10):
            if j == 0 and i == 0:
                dp[i][j] = 0
                dp1[i][j] = 0
            elif j == 0:
                dp[i][j] = -1
                dp1[i][j] = float('inf')
            elif j-k >= 0:
                if dp[i-1][j-k] >= 0:
                    dp[i][j] = max(dp[i-1][j-k]*10+k, dp[i][j])
                if dp1[i-1][j-k] < float('inf'):
                    dp1[i][j] = min(dp1[i-1][j-k]*10+k, dp1[i][j])

if m == 1 and s == 0:
    print("0 0")
elif dp[m][s] == -1:
    print("-1 -1")
else:
    print(str(dp1[m][s]) + " " + str(dp[m][s]))

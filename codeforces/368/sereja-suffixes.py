# 268B: Sereja and Suffixes
# Start Time: 9:01 a.m. 4-29-15
# End Time: 9:13 a.m. 4-29-15 (TLE)


args = list(map(int, input().split()))
n = args[0]
m = args[1]

a = list(map(int, input().split()))

dp = [0 for _ in range(n)]

dis = set()

for i in range(n-1, -1, -1):
    if i == n-1:
        dp[i] = 1
        dis.add(a[i])
    elif a[i] not in dis:
        dp[i] = dp[i+1] + 1
        dis.add(a[i])
    else:
        dp[i] = dp[i+1]

for _ in range(m):
    print(dp[int(input()) - 1])

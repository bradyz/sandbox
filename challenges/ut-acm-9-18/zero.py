import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

n = int(input())
c = list(map(int, input().split()))
dp = [0] + type(c)(c)
d = {}
for i in range(n):
    if i > 0:
        dp[i+1] += dp[i]
    d[dp[i+1]] = d.get(dp[i+1], 0) + 1
r = d.get(0, 0)
for v in d:
    if d[v] >= 2:
        r += nCr(d[v], 2)
print(int(r))

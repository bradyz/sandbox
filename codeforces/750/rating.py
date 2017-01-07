INF = float('inf')

n = int(input())

# Rating before round.
dp1 = [0 for _ in range(n+1)]
dp2 = [0 for _ in range(n+1)]

d = list()
c = list()

for _ in range(n):
    x, y = map(int, input().split())
    c.append(x)
    d.append(y)

if d[0] == 1:
    dp1[0] = 1900
    dp2[0] = INF
else:
    dp1[0] = -INF
    dp2[0] = 1899

impossible = False

for i in range(1, n):
    if d[i-1] == 1 and d[i] == 1:
        dp1[i] = max(1900, dp1[i-1] + c[i-1])
        dp2[i] = dp2[i-1] + c[i-1]
    elif d[i-1] == 2 and d[i] == 2:
        dp1[i] = dp1[i-1] + c[i-1]
        dp2[i] = min(1899, dp2[i-1] + c[i-1])
    elif d[i-1] == 1 and d[i] == 2:
        dp1[i] = max(1899 + c[i-1], dp1[i-1] + c[i-1])
        dp2[i] = min(1899, dp2[i-1] + c[i-1])
    elif d[i-1] == 2 and d[i] == 1:
        dp1[i] = max(1900, dp1[i-1] + c[i-1])
        dp2[i] = dp2[i-1] + c[i-1]

    if dp1[i] > dp2[i]:
        impossible = True

dp2[n] = dp2[n-1] + c[n-1]

if impossible:
    print("Impossible")
elif dp2[n] == INF:
    print("Infinity")
else:
    print(dp2[n])

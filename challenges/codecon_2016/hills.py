n = int(input())
c = [int(input()) for _ in range(n)]
dp1 = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(1, 3):
        if i - j < 0:
            continue
        elif c[i] > c[i-j]:
            continue
        dp1[i] = max(dp1[i], dp1[i-j] + 1)
dp2 = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(1, 3):
        if i - j < 0:
            continue
        elif c[i] < c[i-j]:
            continue
        dp2[i] = max(dp2[i], dp2[i-j] + 1)
print(c)
print(dp1)
print(dp2)
print(max(dp1 + dp2) - 1)

n = int(input())
c = list(map(int, input().split()))

l = dict()
r = dict()

for i in range(n):
    r[c[i]] = i
    if c[i] not in l:
        l[c[i]] = i

dp = [0 for _ in range(n)]

if l[c[0]] == r[c[0]]:
    dp[0] = c[0]

if n >= 2 and c[0] == c[1] and l[c[0]] == 0 and r[c[1]] == 1:
    dp[1] = c[0]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1])

    if i != r[c[i]]:
        continue

    seen = set([c[i]])
    min_l = i
    max_r = i
    xor = c[i]

    for j in range(i, 0, -1):
        min_l = min(min_l, l[c[j]])
        max_l = max(max_r, r[c[j]])

        if c[j] not in seen:
            seen.add(c[j])
            xor ^= c[j]

        if j == l[c[i]] and j <= min_l and i >= max_l:
            dp[i] = max(dp[i], xor + dp[j-1])

print(dp[n-1])

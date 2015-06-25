from pprint import PrettyPrinter
pp = PrettyPrinter()
n = int(input())
c = [2, 3, 7]
dp = [[set() for j in c] for i in range(n+1)]
for i in range(n+1):
    for j in range(len(c)):
        if i == c[j]:
            dp[i][j].add(tuple([c[j]]))
        if i - c[j] >= 0:
            for v in dp[i-c[j]][j]:
                dp[i][j].add(v + tuple([c[j]]))
        if i - c[j] >= 0 and j - 1 >= 0:
            for v in dp[i-c[j]][j-1]:
                dp[i][j].add(v + tuple([c[j]]))
        if j > 1:
            for v in dp[i][j-1]:
                dp[i][j].add(v)
s = []
print(dp[n][2])
for v in dp[n][2]:
    t = [0 for _ in range(3)]
    t[0] = v.count(7)
    t[1] = v.count(3)
    t[2] = v.count(2)
    s.append(t)
s.sort()
for v in s:
    print(" ".join(map(str, v)))

from pprint import PrettyPrinter
pp = PrettyPrinter()

c = list(sorted(map(int, input().split())))
k = int(input())
dp = [[False for j in range(len(c))] for i in range(k+1)]

for i in range(k+1):
    for j in range(len(c)):
        if i == 0 or c[j] == i:
            dp[i][j] = True
        elif j == 0:
            continue
        elif i-c[j] >= 0:
            dp[i][j] = dp[i][j] | dp[i-c[j]][j-1] | dp[i][j-1]
        else:
            dp[i][j] = dp[i][j] | dp[i][j-1]

pp.pprint(dp)
print(dp[k][len(c)-1])

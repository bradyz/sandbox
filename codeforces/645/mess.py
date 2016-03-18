n, k = map(int, input().split())
c = [i for i in range(1, n+1)]
ret = 0
m = n
for i in range(min(k, n // 2)):
    ret += m - 1 + m - 2
    m -= 2
print(ret)

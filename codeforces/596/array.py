n = int(input())
val = [0] + [int(x) for x in input().split()]
res = 0
for i in range(1, n+1):
    res += abs(val[i]-val[i-1])
print(res)

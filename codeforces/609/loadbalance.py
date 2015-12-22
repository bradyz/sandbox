from math import ceil, floor
n = int(input())
a = list(map(int, input().split()))
avg = sum(a) / n
res = 0
for val in a:
    if val < avg:
        res += abs(floor(avg) - val)
    else:
        res += abs(ceil(avg) - val)
print(res // 2)

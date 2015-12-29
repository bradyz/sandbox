from math import ceil, floor
n = int(input())
a = list(map(int, input().split()))
avg = sum(a) / n
a.sort()
res = 0
i = 0
j = n-1
while i < j:
    if abs(avg - a[i]) < 1:
        i += 1
    elif abs(avg - a[j]) < 1:
        j -= 1
    else:
        a[i] += 1
        a[j] -= 1
        res += 1
print(res)

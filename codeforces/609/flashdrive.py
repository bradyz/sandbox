n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]
a.sort(key=lambda x: -x)
i = 0
while m > 0:
    m -= a[i]
    i += 1
print(i)

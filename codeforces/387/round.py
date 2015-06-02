n, m = map(int, input().split())
c = list(sorted(map(int, input().split())))
d = list(sorted(map(int, input().split())))
i, j = 0, 0
while i < n and j < m:
    if c[i] <= d[j]:
        i += 1
    j += 1
print(n-i)

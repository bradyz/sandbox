n, k = map(int, input().split())
c = list(sorted(map(int, input().split())))

r = 0
i, j = 0, 0

while i < n and j < n:
    m = i
    while m+1 < n and c[i] + k >= c[m+1]:
        m += 1
    j = m
    while j+1 < n and c[m] + k >= c[j+1]:
        j += 1
    r += 1
    i = j + 1

print(r)

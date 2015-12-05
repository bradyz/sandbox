n, t = map(int, input().split())
values = [int(input()) for _ in range(n)]
for i in range(n):
    if values[i] < t:
        values[i] = -1
    else:
        values[i] = 1
prefix = values[::]
prefix[0] = values[0]
for i in range(1, n):
    prefix[i] += prefix[i-1]
prefix = [0] + prefix
r = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        if prefix[j] - prefix[i] == 0:
            r += 1
print(r+prefix.count(0))

N, K = map(int, input().split())
a = list(map(int, input().split()))
i, j = 0, 0
x, y = 0, 0
count = dict()
while i < N and j < N:
    if len(count) <= K:
        count[a[j]] = count.get(a[j], 0) + 1
        if len(count) <= K and j - i > y - x:
            x, y = i, j
        j += 1
    else:
        count[a[i]] -= 1
        if count[a[i]] == 0:
            count.pop(a[i])
        i += 1
print(x+1, y+1)

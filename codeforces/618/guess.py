n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = list()
used = set()

for i in range(n):
    count = dict()
    for j in range(n):
        if i == j:
            continue
        if a[i][j] not in count:
            count[a[i][j]] = 0
        count[a[i][j]] += 1
    for c in count:
        if n - count[c] == c:
            if c in used:
                res.append(c+1)
            else:
                res.append(c)
            used.add(c)

print(" ".join(map(str, res)))

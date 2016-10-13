def intersect(s, t):
    return s[1] >= t[0]


def merge(row, t):
    row.append(t)

    can = True

    while can:
        can = False
        row.sort(key=lambda x: x[1])
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if intersect(row[i], row[j]):
                    row.append((min(row[i][0], row[j][0]), row[j][1]))
                    row.pop(j)
                    row.pop(i)
                    can = True
                    break
            if can:
                break
    return row


n, m, k = map(int, input().split())
rows = dict()
for _ in range(k):
    r, c1, c2 = map(lambda x: int(x)-1, input().split())
    if r in rows:
        rows[r] = merge(rows[r], (c1, c2))
    else:
        rows[r] = [(c1, c2)]
result = n * m
for row in rows:
    for segment in rows[row]:
        result -= segment[1] - segment[0] + 1
print(result)

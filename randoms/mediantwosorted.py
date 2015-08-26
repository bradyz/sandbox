c = list(map(int, input().split()))
d = list(map(int, input().split()))

i, j = 0, 0
r = None

while i + j < (len(c) + len(d)) // 2:
    if i < len(c) and c[i] < d[j]:
        r = c[i]
        i += 1
    else:
        r = d[j]
        j += 1

print(r)
print(list(sorted(c + d)))

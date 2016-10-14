def recur(i, used):
    best = 0
    final = [c[i]]
    for j in range(-2, 3):
        if i+j < 0 or i+j >= n:
            continue
        elif i+j in used:
            continue
        elif c[i] <= c[i+j]:
            continue
        used.add(i+j)
        tmp, tmp_final = recur(i+j, used)
        if tmp > best:
            best = tmp
            final = [c[i]] + tmp_final
        used.remove(i+j)
    return best + 1, final


r = -1
n = int(input())
c = [int(input()) for _ in range(n)]
for i in range(n):
    tmp, tmp_final = recur(i, set([i]))
    if tmp > r:
        r = tmp
        final = tmp_final
print(r-1)
# print(final)

n = int(input())
m = [n // 3, n // 3, n // 3]

while (sum(m) != n):
    m[m.index(min(m))] += 1

print(m[0] * m[1] * m[2])

a, b = map(int, input().split())
b -= 1
c = [list(map(int, input().split())) for _ in range(a)]
c = list(reversed(sorted(c, key=lambda x: (x[0], -x[1]))))
count = 1
i = 1
j = 1
while b-i >= 0:
    if c[b-i] == c[b]:
        i += 1
        count += 1
    else:
        break
while b+j < a:
    if c[b+j] == c[b]:
        j += 1
        count += 1
    else:
        break
print(count)

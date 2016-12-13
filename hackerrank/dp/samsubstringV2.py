c = list(map(int, list(input())))
total = c[0]
current = c[0]
for i in range(1, len(c)):
    current = current * 10 + (i + 1) * c[i]
    total += current
print(total % (int(1e9) + 7))

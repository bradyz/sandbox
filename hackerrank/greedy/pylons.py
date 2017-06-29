n, k = map(int, input().split())
c = [i for i, x in enumerate(map(int, input().split())) if x == 1]

result = 0
i = 0
j = 0

while i < n:
    found = False

    while j < len(c) and i + k > c[j]:
        j += 1
        found = True

    if found:
        i = c[j-1] + k
        result += 1
    else:
        result = -1
        break

print(result)

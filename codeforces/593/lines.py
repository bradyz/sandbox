n = int(input())
x1, x2 = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

one = list()
two = list()

for i in range(n):
    k, b = points[i]
    one.append((k * (x1 + 1e-10) + b, i))
    two.append((k * (x2 - 1e-10) + b, i))

one.sort()
two.sort()

overlap = False

for i in range(n):
    if one[i][1] != two[i][1]:
        overlap = True
        break

if overlap:
    print("YES")
else:
    print("NO")

segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

a, b = map(int, input().split())
count = 0
for x in range(a, b):
    while x > 0:
        count += segments[x % 10]
        x //= 10
print(count)

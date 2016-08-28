a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = 0
for x, y in zip(a, b):
    if y > x:
        r += min(y - x, (x - y) % 10)
    else:
        r += min(x - y, (y - x) % 10)
print(r)

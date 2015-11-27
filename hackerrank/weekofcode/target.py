k, n = map(int, input().split())
r = list(map(int, input().split()))
total = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(k-1, -1, -1):
        if x * x + y * y <= r[i] * r[i]:
            total += i+1
            break
print(total)

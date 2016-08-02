n, m = map(int, input().split())
b = list(map(int, input().split()))
a = list(map(int, input().split()))
r = 0
i = 0
for v in b:
    while a[i] < v and i + 1 < len(a):
        i += 1
    r = max(r, min(abs(a[i] - v), abs(a[i-1] - v)))
print(r)

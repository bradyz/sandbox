from collections import Counter
n, m = map(int, input().split())
a = Counter(map(int, input().split()))
b = list(a.values())
r = 0
for i in range(len(b)):
    for j in range(i+1, len(b)):
        r += b[i] * b[j]
print(r)

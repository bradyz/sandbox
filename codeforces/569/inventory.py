from collections import Counter
n = int(input())
c = list(map(int, input().split()))
count = Counter(c)
unused = list(set(range(1, n+1)) - set(count.keys()))
for i in range(n):
    if count[c[i]] > 1 or c[i] > n or c[i] <= 0:
        count[c[i]] -= 1
        c[i] = unused.pop()
print(" ".join(map(str, c)))

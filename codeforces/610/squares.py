n = int(input())
a = list(map(int, input().split()))
minA = min(a)
a = a + a
consecutive_nonzero = [0 for _ in a]
consecutive_nonzero[0] = int(a[0] > minA)
for i in range(1, len(a)):
    if a[i] > minA:
        consecutive_nonzero[i] = consecutive_nonzero[i-1] + 1
res = minA * n + max(consecutive_nonzero)
print(res)

n, k = map(int, input().split())
c = list(map(int, input().split()))
r = 0
for i in range(n):
    for j in range(i+1, n):
        r += ((c[i] + c[j]) % k == 0)
print(r)

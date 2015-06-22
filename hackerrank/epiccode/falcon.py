import sys
n = int(input())
c = list(map(int, input().split()))
m = -sys.maxsize
for i in range(n):
    t = 0
    j = 0
    while n-1-j > i+j:
        print(c[i+j], c[n-1-j])
        t += c[i+j] * c[n-1-j]
        j += 1
    m = max(t, m)
print(m)

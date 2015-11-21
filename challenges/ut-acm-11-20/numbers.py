n = int(input())
c = [0] + list(map(int, input().split()))
r = 0
for i in range(1, n+1):
    r += abs(c[i]-c[i-1])
print(r)

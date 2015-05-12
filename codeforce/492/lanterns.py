a, b = map(int, input().split())
c = sorted(list(map(int, input().split())))
m = c[0]
for i in range(1, a):
    m = max(m, (c[i]-c[i-1])/2)
m = max(m, b-c[a-1])
print(m)

n = int(input())
a = list(map(int, input().split()))
c = dict()
ret = 0
for v in a:
    c[v] = c.get(v, 0) + 1
for i in range(1, n+1):
    tmp = 0
    for v in c.values():
        tmp += (v >= i)
    if tmp == 0:
        break
    ret += tmp - 1
print(ret)

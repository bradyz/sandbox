n, x = map(int, input().split())
a = list(map(int, input().split()))
ret = 0
if x not in a:
    a.append(x)
    ret += 1
a.sort()
while a[(len(a) + 1) // 2 - 1] != x:
    a.append(x)
    a.sort()
    ret += 1
print(ret)

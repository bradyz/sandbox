a, b = map(int, input().split())
ret = 0
while a > 0 and b > 0:
    if a < b:
        a += 1
        b -= 2
    else:
        a -= 2
        b += 1
    if a >= 0 and b >= 0:
        ret += 1
print(ret)

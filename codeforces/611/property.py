def gen():
    upper = bin(int(10e18)).lstrip("0b")
    for i in range(len(upper)):
        for j in range(1, i+1):
            tmp = "1" * j + "0" + (i - j) * "1"
            yield tmp

a, b = map(int, input().split())
res = 0
for x in gen():
    if int(x, 2) >= a and int(x, 2) <= b:
        res += 1
print(res)

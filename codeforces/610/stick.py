n = int(input())
res = 0
if n % 4 == 0:
    res -= 1
if n % 2 == 0:
    res += n // 4
print(res)

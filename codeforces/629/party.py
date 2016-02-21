m = [0 for _ in range(400)]
f = [0 for _ in range(400)]

n = int(input())

for i in range(n):
    g, a, b = input().split()
    a = int(a)
    b = int(b)

    if g == "M":
        for j in range(a, b+1):
            m[j] += 1
    else:
        for j in range(a, b+1):
            f[j] += 1

ret = 0

for i in range(1, 400):
    ret = max(ret, min(m[i], f[i]) * 2)

print(ret)

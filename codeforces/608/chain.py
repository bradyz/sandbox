n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: x[0])
des = [False for _ in range(n)]
res = n
for i in range(n):
    for j in range(i+1):
        des[j] = False
    for j in range(i+1, n):
        des[j] = True
    j = i
    while j >= 0:
        if des[i]:
            j -= 1
            continue
        for k in range(j-1, -1, -1):
            if a[j][0] - a[k][0] > a[j][1]:
                j = k + 1
                break
            des[k] = True
        j -= 1
    res = min(res, des.count(True))
print(res)

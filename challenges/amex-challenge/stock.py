k = 3
n = int(input())
val = [0 for _ in range(n)]
for i in range(n):
    x, y, z = input().split()
    val[i] = z
for i in range(n):
    try:
        float(val[i])
    except:
        around = list()
        for j in range(i, max(0, i-k), -1):
            try:
                float(val[j])
            except:
                continue
            around.append(val[j])
        for j in range(i, min(n, i+k)):
            try:
                float(val[j])
            except:
                continue
            around.append(val[j])
        print(sum(map(float, around)) / len(around))

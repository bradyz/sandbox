def area():
    for i in range(len(val)):
        for j in range(1, len(val)):
            tmp = abs(val[i][0]-val[j][0]) * abs(val[i][1]-val[j][1])
            if tmp != 0:
                return tmp
    return -1

n = int(input())
val = [list(map(int, input().split())) for _ in range(n)]
print(area())

from math import factorial


def choose(n, k):
    return factorial(n) // factorial(n-k) // factorial(k)

for T in range(int(input())):
    N = int(input())
    dot = [list(map(int, input().split())) for _ in range(N)]
    distance = {i: {} for i in range(N)}
    for i in range(N):
        for j in range(i+1, N):
            dist = (dot[i][0] - dot[j][0]) ** 2 + (dot[i][1] - dot[j][1]) ** 2
            if dist in distance[i]:
                distance[i][dist] += 1
            else:
                distance[i][dist] = 1
            if dist in distance[j]:
                distance[j][dist] += 1
            else:
                distance[j][dist] = 1
    result = 0
    for i in distance:
        for dist in distance[i]:
            if distance[i][dist] < 2:
                continue
            result += choose(distance[i][dist], 2)
    print("Case #" + str(T+1) + ": " + str(result))

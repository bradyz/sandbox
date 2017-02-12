for _ in range(int(input())):
    values = [list(map(int, input().split())) for _ in range(int(input()))]
    total_time = sum(x[1] for x in values)
    distances = list(map(lambda x: x[0] * x[1], values))
    print("%.0f" % (sum(distances) / total_time))

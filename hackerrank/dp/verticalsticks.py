for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    greater = {x: i+1 for i, x in enumerate(reversed(sorted(c)))}
    result = 0
    for x in c:
        result += (n + 1) / (greater[x] + 1)
    print("%.2f" % result)

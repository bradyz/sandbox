def ways(n):
    res = 1
    n = sorted(n)
    for i, val in enumerate(n):
        ways = max(0, i+1-val)
        if ways > 0:
            res = res * ways % 1000000007
        else:
            return 0
    return res

if __name__ == "__main__":
    for _ in range(int(input())):
        s = int(input())
        c = [int(x) for x in input().split()]
        print(ways(c))

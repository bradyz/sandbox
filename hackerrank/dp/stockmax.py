def stockmax(s, c):
    maxval = [0 for _ in range(s+1)]
    profit = 0
    for i in range(s-1, -1, -1):
        maxval[i] = max(maxval[i+1], c[i])
        profit += maxval[i] - c[i]
    print(profit)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = [int(x) for x in input().split()]
        stockmax(n, v)
